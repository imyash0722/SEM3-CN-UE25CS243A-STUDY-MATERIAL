# Unit 3: Network Layer and Internet Protocol (Chapters 4-5)

## Overview
This unit covers Chapters 4-5 of Kurose & Ross (9th Edition):
- Chapter 4: The Network Layer - Data Plane
- Chapter 5: The Network Layer - Control Plane

**Course Hours**: 14 hours

---

## 4.1 Overview of Network Layer

### Network Layer Services and Protocol
**Transport segment from sending to receiving host**:
- Sender: encapsulates segments into datagrams, passes to link layer
- Receiver: delivers segments to transport layer protocol

**Network layer protocols in every Internet device**: hosts, routers

### Two Key Network-layer Functions
1. **Forwarding**: Move packets from a router's input link to appropriate router output link
2. **Routing**: Determine route taken by packets from source to destination
   - Routing algorithms

**Analogy**: Taking a trip
- Forwarding: process of getting through single interchange
- Routing: process of planning trip from source to destination

### Interplay between Routing and Forwarding
- Routing algorithm determines end-end path through network
- Local forwarding table determines local forwarding at this router

### Network Layer: Data Plane, Control Plane

**Data plane**: Local, per-router function - determines how datagram arriving on router input port is forwarded to router output port

**Control plane**: Network-wide logic - determines how datagram is routed among routers along end-end path from source host to destination host

Two control-plane approaches:
1. **Traditional routing algorithms**: Implemented in routers
2. **Software-Defined Networking (SDN)**: Implemented in (remote) servers

### Per-router Control Plane
Individual routing algorithm components in each and every router interact in the control plane

### Software-Defined Networking (SDN) Control Plane
Remote controller computes, installs forwarding tables in routers

### Network Service Model
**Q**: What service model for "channel" transporting datagrams from sender to receiver?

| Network Architecture | Service Model | Bandwidth | Loss | Order | Timing |
|---------------------|---------------|-----------|------|-------|--------|
| Internet (best effort) | None | No | No | No | No |
| ATM (Constant Bit Rate) | Constant rate | Yes | Yes | Yes | Yes |
| ATM (Available Bit Rate) | Guaranteed min | No | Yes | No | No |
| Internet (Intserv Guaranteed) | Yes | Yes | Yes | Yes | Yes |
| Internet (Diffserv) | Possible | Possibly | Possibly | Yes | No |

**Internet "best effort" service model**: No QoS guarantees. Simplicity of mechanism has allowed Internet to be widely deployed. Sufficient provisioning of bandwidth allows performance of real-time applications to be "good enough" for "most of the time".

---

## 4.2 What's Inside a Router?

### Router Architecture Overview
High-level view of generic router architecture:
- **Routing processor**: Routing, management control plane (software) operates in millisecond time frame
- **High-speed switching fabric**: Forwarding data plane (hardware) operates in nanosecond timeframe
- **Router input/output ports**

### Input Port Functions
- **Physical layer**: Bit-level reception
- **Link layer**: e.g., Ethernet
- **Lookup, forwarding**: Decentralized switching using header field values, lookup output port using forwarding table in input port memory ("match plus action")
  - Destination-based forwarding: forward based only on destination IP address (traditional)
  - Generalized forwarding: forward based on any set of header field values
- **Queueing**: If datagrams arrive faster than forwarding rate into switch fabric

### Longest Prefix Matching
When looking for forwarding table entry for given destination address, use **longest address prefix** that matches destination address.

Example:
```
Destination Address Range         Link Interface
11001000 00010111 00010*** ********   0
11001000 00010111 00011000 ********   1
11001000 00010111 00011*** ********   2
otherwise                                        3
```

For address `11001000 00010111 00010110 10100001` → matches interface 0 (longest prefix `/20`)
For address `11001000 00010111 00011000 10101010` → matches interface 1 (longest prefix `/19`)

**Implementation**: Often performed using ternary content addressable memories (TCAMs)

### Switching Fabrics
Three major types:
1. **Memory**: First generation; packet copied to system's memory; speed limited by memory bandwidth
2. **Bus**: Datagram from input port memory to output port memory via shared bus; bus contention limits speed
3. **Interconnection network**: Crossbar, Clos networks; multistage switch exploits parallelism

**Input port queuing**: If switch fabric slower than input ports combined → queueing at input queues. Head-of-the-Line (HOL) blocking: queued datagram at front prevents others from moving forward.

**Output port queuing**: Buffering required when datagrams arrive from fabric faster than link transmission rate. Drop policy and scheduling discipline choose among queued datagrams.

**Buffer sizing**: RFC 3439 rule of thumb: average buffering = RTT × link capacity C. More recent: RTT × C / √N for N flows.

### Buffer Management
- **Drop policies**: Tail drop, priority-based drop
- **Marking**: ECN, RED for congestion signaling

---

## 4.3 The Internet Protocol (IP)

### IPv4 Datagram Format
```
 0                   15 16                  31
+----------------------+----------------------+
| ver | head.len | type of service | length |
+----------------------+----------------------+
| 16-bit identifier | flgs | fragment offset |
+----------------------+----------------------+
| time to live | upper layer | header checksum |
+----------------------+----------------------+
| 32-bit source IP address                       |
+----------------------+----------------------+
| 32-bit destination IP address                  |
+----------------------+----------------------+
| options (if any)                               |
+----------------------+----------------------+
| payload data (variable length, typically TCP/UDP) |
+--------------------------------------------------+
```

**Key Fields**:
- **Version** (4 bits): 4 for IPv4
- **Header Length** (4 bits): In 32-bit words (typically 5 = 20 bytes)
- **Type of Service** (8 bits): DiffServ (6 bits) + ECN (2 bits)
- **Total Length** (16 bits): Total datagram length in bytes (max 64KB)
- **Identification** (16 bits): For fragmentation/reassembly
- **Flags** (3 bits): DF (Don't Fragment), MF (More Fragments)
- **Fragment Offset** (13 bits): Offset in 8-byte units
- **TTL** (8 bits): Max hops (decremented at each router)
- **Protocol** (8 bits): Upper layer (TCP=6, UDP=17)
- **Header Checksum** (16 bits): Error detection
- **Source/Dest IP** (32 bits each)

**Overhead**: 20 bytes IP + 20 bytes TCP = 40 bytes + app layer overhead
**Typical MTU**: 1500 bytes

### IPv4 Fragmentation
**Network links have MTU** (max transfer size) - largest possible link-level frame
**Different link types, different MTUs**
**Large IP datagram divided** ("fragmented") within net
**One datagram becomes several datagrams**
**"Reassembled" only at final destination**
**IP header bits used to identify, order related fragments**

**Example**: 4000 byte datagram, MTU = 1500 bytes
- 1480 bytes in data field per fragment
- Fragment 1: length=1500, ID=x, fragflag=1, offset=0
- Fragment 2: length=1500, ID=x, fragflag=1, offset=185 (1480/8)
- Fragment 3: length=1060, ID=x, fragflag=0, offset=370 (2960/8)

**Why fragmentation is avoided**:
1. One lost fragment loses them all (IP never resends)
2. TCP sizes segments to fit (1500 - 20 - 20 = 1460 bytes)
3. Senders set DF bit; routers drop and send ICMP "packet too big"
4. IPv6 routers never fragment (only sender may split)

---

## 4.4 IPv4 Addressing

### IP Addressing: Introduction
- **IP address**: 32-bit unique ID associated with each host or router interface
- **Interface**: Connection between host/router and physical link
- **Router**: Typically has multiple interfaces
- **Host**: Typically has one or two interfaces (wired + wireless)

**Dotted-decimal notation**: 223.1.1.1 = 11011111 00000001 00000001 00000001

### Subnets
**What's a subnet?** Device interfaces that can physically reach each other without passing through an intervening router

**IP addresses have structure**:
- **Subnet part**: Devices in same subnet have common high-order bits
- **Host part**: Remaining low-order bits

**Subnet mask**: `/24` (high-order 24 bits = subnet part of IP address)
Example: 223.1.1.0/24

### CIDR (Classless InterDomain Routing)
- **CIDR**: Subnet portion of address of arbitrary length
- **Address format**: a.b.c.d/x, where x = # bits in subnet portion

### Why Not Classful Addressing?
- Class A (/8): Up to 16,777,214 hosts (too large)
- Class B (/16): Up to 65,536 hosts (too large for many)
- Class C (/24): Only 254 hosts (too small for many)
- **Classful addressing replaced with classless addressing (CIDR)**

### Hierarchical Addressing: Route Aggregation
Hierarchical addressing allows efficient advertisement of routing information:
- ISP advertises single prefix covering multiple organizations
- Example: `200.23.16.0/20` covers 8 `/23` organizations
- **Address aggregation** (route summarization)

### Getting IP Addresses
- **Network gets subnet part**: Allocated portion of provider ISP's address space
- **ISP gets block**: From ICANN (Internet Corporation for Assigned Names and Numbers) through 5 regional registries
- **ICANN allocated last IPv4 chunk to RRs in 2011**
- **NAT helps IPv4 exhaustion**
- **IPv6 has 128-bit address space**

---

## 4.5 NAT (Network Address Translation)

### NAT Overview
**NAT**: All devices in local network share just one IPv4 address as far as outside world is concerned

**Private IP address spaces** (RFC 1918):
- 10.0.0.0/8 (10/8)
- 172.16.0.0/12 (172.16/12)
- 192.168.0.0/16 (192.168/16)

### Advantages of NAT
1. Just one IP address needed from provider ISP for all devices
2. Can change addresses of hosts in local network without notifying outside world
3. Can change ISP without changing addresses of devices in local network
4. Security: devices inside local net not directly addressable/visible by outside world

### Implementation
NAT router must (transparently):
1. **Outgoing datagrams**: Replace (source IP, port) with (NAT IP, new port)
2. **Remember** in NAT translation table every (source IP, port) to (NAT IP, new port) pair
3. **Incoming datagrams**: Replace (NAT IP, new port) with corresponding (source IP, port) from table

### NAT Traversal Problem
What if client wants to connect to server behind NAT?
**Solution**: Statically configure NAT to forward incoming connection requests at given port to server
Example: (123.76.29.7, port 25000) always forwarded to 10.0.0.1 port 25000

---

## 5.1 Routing Algorithms

### Graph Abstraction
- **Graph**: G = (N, E)
- N: Set of routers
- E: Set of links
- c(x,y): Cost of direct link connecting x and y (∞ if not direct neighbors)

### Routing Algorithm Classification
| Classification | Description |
|----------------|-------------|
| **Global (Link State)** | All routers have complete topology, link cost info |
| **Decentralized (Distance Vector)** | Iterative process; routers initially only know link costs to attached neighbors |

| Dynamics | Description |
|----------|-------------|
| **Static** | Routes change slowly over time |
| **Dynamic** | Routes change quickly; periodic updates or in response to link cost changes |

---

## 5.2 Link-State Routing (Dijkstra's Algorithm)

### Dijkstra's Link-State Routing Algorithm
- **Centralized**: Network topology, link costs known to all nodes (accomplished via "link state broadcast")
- **Computes least cost paths** from one node ("source") to all other nodes
- **Gives forwarding table** for that node
- **Iterative**: After k iterations, know least cost path to k destinations

**Notation**:
- c(x,y): Direct link cost from node x to y (∞ if not direct neighbors)
- D(v): Current estimate of cost of least-cost-path from source to destination v
- p(v): Predecessor node along path from source to v
- N': Set of nodes whose least-cost-path definitively known

**Algorithm**:
```
1. Initialization:
   N' = {u}
   for all nodes v:
     if v adjacent to u: D(v) = c(u,v)
     else D(v) = ∞

2. Loop:
   find w not in N' such that D(w) is minimum
   add w to N'
   update D(v) for all v adjacent to w and not in N':
     D(v) = min( D(v), D(w) + c(w,v) )
   until all nodes in N'
```

### Example
For network:
```
u --2-- v --1-- x --1-- y --2-- z
|       |       |       |
5       3       1       5
|       |       |       |
w --1-- 5 --1-- 1 --1-- 4
```

**Resulting forwarding table in u**:
| Destination | Outgoing Link |
|-------------|---------------|
| v           | (u,v)         |
| x           | (u,x)         |
| y           | (u,x)         |
| w           | (u,x)         |
| z           | (u,x)         |

Route from u to v directly; route from u to all other destinations via x.

---

## 5.3 Distance Vector Routing (Bellman-Ford Algorithm)

### Bellman-Ford Equation
Let Dx(y): cost of least-cost path from x to y.
Then: **Dx(y) = minᵥ { c(x,v) + Dᵥ(y) }**
- min taken over all neighbors v of x
- c(x,v): direct cost of link from x to v
- Dᵥ(y): v's estimated least-cost-path cost to y

### Distance Vector Algorithm
**Key idea**: Each node sends its own distance vector estimate to neighbors. When x receives new DV estimate from neighbor, it updates its own DV using B-F equation:
```
Dx(y) ← minᵥ { c(x,v) + Dᵥ(y) } for each node y ∈ N
```

Under minor conditions, estimate Dx(y) converges to actual least cost dx(y).

**Node behavior**:
- Wait for (change in local link cost or msg from neighbor)
- Recompute DV estimates using DV received from neighbor
- If DV to any destination has changed, notify neighbors
- Iterative, asynchronous: local iteration caused by local link cost change or DV update from neighbor
- Distributed, self-stopping: each node notifies neighbors only when its DV changes

### Example Iteration
Network with nodes a,b,c,d,e,f,g,h,i and various link costs.

**t=0**: All nodes know only direct neighbors
**t=1**: Nodes exchange DVs with neighbors, recompute
**t=2**: Information propagates 2 hops
**t=3**: Information propagates 3 hops
**t=4**: Convergence

### Link Cost Changes
- **Good news travels fast**: Decrease in link cost propagates quickly
- **Bad news travels slow**: Count-to-infinity problem
  - y sees direct link to x cost increase, but z says it has path at cost 5
  - y computes "my new cost to x = 6 via z", notifies z
  - z learns path via y now cost 6, computes "my new cost = 7 via y"
  - Continues incrementally until infinity

### Distance Vector vs Link State
| Aspect | Distance Vector | Link State |
|--------|-----------------|------------|
| Primary principle | Send entire routing table to neighbors | Only provide link state information |
| Learning about network | From neighbors only | From all routers |
| Building routing table | Based on inputs from neighbors | Based on complete database from all routers |
| Advertisement of updates | Periodic (every 30-90 sec) - Broadcast | Triggered (on change) - Multicast |
| Routing loops | Vulnerable | Less prone |
| Convergence | Slow | Fast |
| Resources | Less CPU/memory | More CPU/memory required |
| Cost | Less | More |
| Scalability | Less scalable | More scalable |
| Examples | RIP, IGRP | OSPF, IS-IS |

---

## 4.6/5.4 SDN (Software-Defined Networking)

### Motivation
Traditional: Monolithic router with proprietary OS (Cisco IOS), distributed control plane
~2005: Renewed interest in rethinking network control plane

### Key Characteristics of SDN
1. **Generalized "flow-based" forwarding** (e.g., OpenFlow):
   - Packet forwarding based on any header field values (transport, network, link layer)
   - 11 different header field values in OpenFlow
   - Contrast: Traditional only destination IP address

2. **Control and Data plane separation**:
   - Data plane: Simple, fast switches executing "match plus action" rules
   - Control plane: Servers/software determining and managing switches' flow tables

3. **Network control functions external to data-plane switches**:
   - SDN controller (network OS) + network-control applications
   - Controller maintains network state, provides APIs
   - Logically centralized (typically distributed for scalability)

4. **Programmable control applications**:
   - "Brains" of control plane
   - Unbundled: can be 3rd party, distinct from routing vendor

### SDN Architecture
```
Network-control applications (routing, access control, load balance)
        ↓ Northbound API
SDN Controller (network OS)
        ↓ Southbound API (OpenFlow)
SDN-controlled switches (data plane)
```

### OpenFlow Protocol
- Operates between controller & switch over TCP (port 6653)
- Three message classes:
  - Controller-to-switch: features, configure, modify-state (add/delete/modify flow entries), packet-out
  - Switch-to-controller: packet-in, flow-removed, port-status
  - Symmetric: hello, echo, experimenter

### Flow Table Abstraction
- **Flow**: Defined by header field values (link, network, transport layer)
- **Match**: Pattern values in packet header fields
- **Actions**: Forward, drop, modify, send to controller
- **Priority**: Disambiguate overlapping patterns
- **Counters**: #bytes and #packets

### OpenFlow Examples
1. **Destination-based forwarding**: Match IP Dst = 51.6.0.8 → forward port 6
2. **Firewall**: Match TCP Dst Port = 22 → drop
3. **NAT**: Match IP address and port → rewrite address and port

### P4 (Programming Protocol-independent Packet Processors)
- Domain-specific language to program data plane
- Unlike SDN controllers (decide where packets go), P4 defines how packets are processed
- Protocol-independent: define your own protocol
- Components: Parser, ingress match-action, buffer, egress match-action, deparser

---

## 4.7 Data Center Networking

### Datacenter Characteristics
- 10's to 100's of thousands of hosts, closely coupled, in close proximity
- **North-South traffic**: User → Internet → Data Center → Server
- **East-West traffic**: Server ↔ Server ↔ Database ↔ Storage (very important for distributed apps)

### Traditional 3-Tier Architecture
- Access layer → connects servers
- Aggregation layer → combines access switches
- Core layer → provides high-speed connectivity
- **Limitation**: Bottlenecks for east-west traffic

### Leaf-Spine Architecture (Modern)
- **Leaf switches**: Top of rack (ToR), connect to servers, every leaf connects to every spine
- **Spine switches**: High-speed backbone, connect to all leaves, no direct server connections
- **ECMP (Equal-Cost MultiPath)**: Hash flows across multiple spines

### Oversubscription
- Ratio of server-facing bandwidth to uplink bandwidth
- Example: 40 servers × 25 Gbps = 1000 Gbps; 4 uplinks × 100 Gbps = 400 Gbps → 2.5:1 oversubscription
- Common: ~3:1

### Scaling: Pods and Super-Spines
- Spine port limit constrains leaf count
- Group racks into pods, join pods with super-spines
- Same concept, one level up (leaf-spine of leaf-spines)

### Multipath Routing & ECMP
- Multiple routing paths between sender/receiver
- Hash flow (src/dst IP, port, protocol) → pick path
- Per-flow hashing avoids packet reordering
- Spine failure: re-hash onto remaining paths

### Application-Layer Routing
- Load balancer at edge: receives external requests, directs workload within DC

### Protocol Innovations for Datacenters
| Layer | Innovation | Why it works in DC |
|-------|-----------|-------------------|
| Link | RoCE (RDMA over Converged Ethernet): NIC writes directly to remote memory, bypassing CPU/OS | Single vendor, single admin domain → can run PFC for lossless fabric |
| Transport | DCTCP/DCQCN: Use fraction of ECN-marked packets as multi-bit signal, scale window cut proportionally | Homogeneous switches all support ECN consistently; short stable queues for μs RTTs |
| Transport | Hop-by-hop backpressure: Each switch signals upstream to slow down | Same operator owns all switches → can hold state, react faster than RTT |
| Routing/Mgmt | SDN: Centralized controller computes routes; switches just forward | One operator, uniform hardware → global traffic engineering |
| Placement | Locality-aware placement: Keep chatty services/data in same/nearby rack | Clos topology oversubscribed higher up; staying under one ToR avoids core links |

---

## IPv6 (Chapter 4/5)

### IPv6 Rationale
- **Larger address space**: 128-bit (340 undecillion addresses)
- **Better header format**: 40-byte fixed length header
- **No checksum**: Removed to speed processing
- **No fragmentation/reassembly**: Only sender fragments
- **Options**: Available as extension headers (Next Header field)
- **Flow label**: Identify datagrams in same "flow"
- **ICMPv6**: New version of ICMP

### IPv6 Datagram Format
```
32 bits
ver | pri | flow label (20 bits) | payload len | next hdr | hop limit
128-bit source address
128-bit destination address
payload
```
**Missing from IPv4**: No checksum, no fragmentation, no options in base header

### IPv6 Address Notation
- 128 bits = eight 16-bit blocks (hextets)
- Separated by colons ':'
- Hexadecimal (each hex char = 4 bits)
- **Compression rules**:
  1. Discard leading zeros in each block
  2. Replace consecutive all-zero blocks with `::` (only once!)
  3. Example: `2001:0db8:0000:0000:0000:ff00:0042:8329` → `2001:db8::ff00:42:8329`

### IPv6 Address Types
1. **Unicast** (one-to-one): Single interface
2. **Multicast** (one-to-many): Group of interfaces
3. **Anycast** (one-to-nearest): Group sharing address; delivered to closest
4. **No broadcast**: Implemented via multicast

### Transition from IPv4 to IPv6
- **Tunneling**: IPv6 datagram carried as payload in IPv4 datagram among IPv4 routers
- **Dual stack**: Nodes run both IPv4 and IPv6
- **NAT64/DNS64**: Translation mechanisms

---

## ICMP (Internet Control Message Protocol)

### Services
- Used by hosts and routers to communicate network-layer information
- Error reporting: unreachable host/network/port/protocol
- Echo request/reply (used by ping)
- Carried as IP payloads (network-layer "above" IP)

### Common ICMP Types
| Type | Code | Description |
|------|------|-------------|
| 0 | 0 | Echo reply (ping) |
| 3 | 0 | Destination network unreachable |
| 3 | 1 | Destination host unreachable |
| 3 | 2 | Destination protocol unreachable |
| 3 | 3 | Destination port unreachable |
| 8 | 0 | Echo request (ping) |
| 11 | 0 | TTL expired (used by traceroute) |
| 12 | 0 | Bad IP header |

### Utilities
- **ping**: Uses ICMP echo request/reply
- **traceroute**: Uses ICMP TTL expired messages

---

## DHCP (Dynamic Host Configuration Protocol)

### Goal
Host dynamically obtains IP address from network server when it "joins" network
- Can renew lease on address in use
- Allows reuse of addresses (only hold while connected/on)
- Supports mobile users

### DORA Process
1. **DHCP Discover**: Client broadcasts (src: 0.0.0.0, dst: 255.255.255.255)
2. **DHCP Offer**: Server responds with IP offer (yiaddr, lease time)
3. **DHCP Request**: Client requests offered IP
4. **DHCP ACK**: Server confirms assignment

### DHCP Returns
- Allocated IP address
- Address of first-hop router (default gateway)
- Name and IP address of DNS server
- Network mask

---

## Key Formulas (Network Layer)

| Formula | Equation |
|---------|----------|
| IPv4 Header Checksum | 1's complement sum of 16-bit header words |
| Longest Prefix Match | Choose entry with longest matching prefix |
| Subnet Address | IP AND Subnet Mask |
| Broadcast Address | Subnet Address OR (NOT Subnet Mask) |
| Number of Hosts | 2^(32 - prefix_length) - 2 |
| Dijkstra Update | D(v) = min(D(v), D(w) + c(w,v)) |
| Bellman-Ford | Dx(y) = minᵥ { c(x,v) + Dᵥ(y) } |

---

## Complete Questions, Examples, and MCQs from Slides and Textbook

### Numerical Problems (Exam Practice)

**Q1. Longest Prefix Matching**: Given forwarding table:
```
11001000 00010111 00010*** ******** → 0
11001000 00010111 00011000 ******** → 1
11001000 00010111 00011*** ******** → 2
otherwise → 3
```
For destination 11001000 00010111 00010110 10100001 → **Interface 0** (matches /20)
For destination 11001000 00010111 00011000 10101010 → **Interface 1** (matches /19)

**Q2. IPv4 Fragmentation**: 4000 byte datagram, MTU = 1500 bytes
- Data per fragment = 1500 - 20 = 1480 bytes
- Fragments needed = 3 (4000/1480 = 2.7)
- Fragment 1: len=1500, ID=x, MF=1, offset=0
- Fragment 2: len=1500, ID=x, MF=1, offset=185
- Fragment 3: len=1060, ID=x, MF=0, offset=370

**Q3. Fragmentation Numerical Example**: MTU=200 bytes, IP packet=520 bytes, header=20 bytes
- Max data per fragment = 180 bytes (must be multiple of 8 → 176 bytes = 22×8)
- Fragments: 176, 176, 148 bytes data
- Offsets: 0, 22, 44

**Q4. Subnet Address Calculation**: IP=172.21.35.17, Class B
- Default mask: 255.255.0.0
- Network address = 172.21.0.0

**Q5. Address Range in Blocks**:
- 123.56.77.32/29: 8 total, 6 usable (33-38), broadcast=39
- 180.34.64.64/30: 4 total, 2 usable (65-66), broadcast=67
- 200.17.21.128/27: 32 total, 30 usable (129-158), broadcast=159

**Q6. Subnet Design**: Network 175.200.0.0, need 4 subnets
- Min host bits = 2 (2²=4 subnets)
- Subnet mask: 255.255.192.0 (/26)

**Q7. Dijkstra's Algorithm**: Compute shortest paths from u
```
Step 0: N'={u}, D(v)=2, D(x)=1, D(w)=5, D(y)=∞, D(z)=∞
Step 1: Add x (D=1), update D(w)=4, D(y)=2
Step 2: Add y (D=2), update D(w)=3, D(z)=4
Step 3: Add v (D=2), no updates
Step 4: Add w (D=3), update D(z)=4
Step 5: Add z (D=4), done
```

**Q8. Bellman-Ford**: Given neighbors x,v,w with Dx(z)=3, Dv(z)=5, Dw(z)=3
Du(z) = min{cu,x+Dx(z), cu,v+Dv(z), cu,w+Dw(z)} = min{1+3, 2+5, 5+3} = 4 (via x)

**Q9. Distance Vector Iterations**: t=0,1,2,3,4 convergence
- t=0: only direct neighbors
- t=1: info propagates 1 hop
- t=2: info propagates 2 hops
- t=3: info propagates 3 hops
- t=4: convergence

**Q10. NAT Translation**: Host 10.0.0.2:4000 → Web 93.184.216.34:443, NAT 138.76.29.7:5002
- ① Leaves host: S=10.0.0.2:4000, D=93.184.216.34:443
- ② Leaves NAT: S=138.76.29.7:5002, D=93.184.216.34:443
- ③ Reply to NAT: S=93.184.216.34:443, D=138.76.29.7:5002
- ④ Reply to host: S=93.184.216.34:443, D=10.0.0.2:4000

**Q11. SDN/OpenFlow**: Match IP Dst=51.6.0.8 → Action: forward port 6
- Flow table: Match (header fields) → Action (forward/drop/modify/controller) → Stats

**Q12. Datacenter Oversubscription**: 40 servers × 25 Gbps = 1000 Gbps, 4 uplinks × 100 Gbps = 400 Gbps
- Oversubscription = 1000/400 = 2.5:1

**Q13. ECMP**: Hash 5-tuple (src/dst IP, port, protocol) → pick spine
- Per-flow hashing avoids packet reordering
- Spine failure: re-hash onto remaining paths

**Q14. IPv6 Address Compression**: 
- 2001:0db8:0000:0000:0000:ff00:0042:8329 → 2001:db8::ff00:42:8329
- ::1 = loopback, :: = unspecified

**Q15. IPv6 Transition**: Tunneling = IPv6 payload in IPv4 datagram
- Dual stack = run both IPv4 and IPv6

---

### Review Questions

1. **Forwarding vs Routing?**
   - Forwarding: Local action moving packet from input to output link
   - Routing: Network-wide path determination

2. **Data plane vs Control plane?**
   - Data plane: Per-router forwarding (fast, hardware)
   - Control plane: Network-wide routing logic (slow, software)

3. **Longest prefix matching?**
   - When multiple prefixes match, choose the longest (most specific)

4. **What is SDN?**
   - Separation of control and data planes; centralized controller manages switches via OpenFlow

5. **Link State vs Distance Vector?**
   - LS: Global topology, Dijkstra, fast convergence, more resources
   - DV: Neighbor info only, Bellman-Ford, slow convergence, count-to-infinity

6. **IPv4 fragmentation fields?**
   - Identification (same for all fragments), Flags (MF, DF), Fragment Offset (in 8-byte units)

7. **Why avoid fragmentation?**
   - One lost fragment loses all; TCP avoids with MSS; DF bit; IPv6 routers don't fragment

8. **CIDR vs Classful?**
   - CIDR: Arbitrary prefix length, efficient allocation
   - Classful: Fixed /8, /16, /24 boundaries, wasteful

9. **NAT operation?**
   - Replace private (IP, port) with public (IP, new port) for outgoing; reverse for incoming

10. **IPv6 improvements?**
    - 128-bit addresses, fixed 40-byte header, no checksum, no router fragmentation, flow label, extension headers

11. **ICMP uses?**
    - Error reporting (unreachable, TTL expired), ping, traceroute

12. **DHCP DORA?**
    - Discover (broadcast) → Offer (broadcast) → Request (broadcast) → ACK (broadcast)

13. **Leaf-Spine vs 3-Tier?**
    - Leaf-spine: Every rack equal distance, all links used, scale by adding leaves/spines
    - 3-Tier: Funnel traffic to core, spanning tree blocks links, scale up = bigger boxes

14. **ECMP in datacenters?**
    - Hash flow (5-tuple) → pick spine; per-flow hashing avoids reordering; fast failover

15. **DCTCP/BBR in DCs?**
    - DCTCP: ECN marking fraction → proportional window cut
    - BBR: Model-based (BW × RTT_min), paces at BDP, ignores loss

---

## Multiple Choice Questions (from Slides)

**Q1. Network-layer functions:**
- Forwarding: move packets from input to output link
- Routing: determine route from source to destination

**Q2. Forwarding vs Routing analogy:**
- Forwarding: process of getting through single interchange
- Routing: process of planning trip from source to destination

**Q3. Network service model - Internet best effort provides:**
- No bandwidth guarantees, no loss guarantees, no order guarantees, no timing guarantees

**Q4. Router architecture - which component operates in millisecond timeframe?**
- Routing processor (control plane)

**Q5. Longest prefix matching - if prefixes don't divide nicely?**
- Use longest matching prefix

**Q6. Switching fabric types:**
- Memory (2 bus crossings), Bus (contention), Interconnection network (parallelism)

**Q6. HOL blocking occurs at:**
- Input port queues

**Q7. Output port queuing - buffering required when:**
- Datagrams arrive from fabric faster than link transmission rate

**Q8. Buffer sizing (RFC 3439):**
- Average buffering = RTT × link capacity C
- Recent: RTT × C / √N

**Q9. IPv4 header - which field is 16-bit identifier?**
- Used for fragmentation/reassembly

**Q10. IPv4 fragmentation - fragment offset units:**
- 8-byte units

**Q11. Why fragmentation avoided?**
- One lost fragment loses all; TCP sizes segments; DF bit; IPv6 no router fragmentation

**Q12. CIDR address format:**
- a.b.c.d/x where x = bits in subnet portion

**Q13. Classful addressing problem:**
- Class A too large, Class C too small, Class B wasteful

**Q14. Route aggregation example:**
- 200.23.16.0/20 covers 8 /23 organizations

**Q15. NAT advantages:**
- Single IP from ISP, change local addresses without notifying outside, change ISP, security

**Q16. Bellman-Ford equation:**
- Dx(y) = minᵥ { c(x,v) + Dᵥ(y) }

**Q17. Distance vector algorithm:**
- Send DV to neighbors; update using B-F; notify neighbors if changed

**Q18. Count-to-infinity problem:**
- Bad news travels slow; y thinks path via z, z thinks path via y

**Q19. Link State vs DV - advertisement:**
- DV: periodic (30-90s) broadcast; LS: triggered (on change) multicast

**Q20. SDN - OpenFlow port:**
- 6653 (TCP)

**Q21. OpenFlow message classes:**
- Controller-to-switch, Switch-to-controller, Symmetric

**Q22. Datacenter traffic types:**
- North-South: user ↔ datacenter; East-West: server ↔ server

**Q23. 3-tier limitation:**
- Bottlenecks for east-west traffic; spanning tree blocks links

**Q24. Leaf-spine - every leaf connects to:**
- Every spine

**Q25. Oversubscription ratio:**
- Server-facing bandwidth / uplink bandwidth

**Q26. ECMP hashing:**
- 5-tuple hash → pick path; per-flow avoids reordering

**Q27. IPv6 header - what's missing?**
- No checksum, no fragmentation, no options in base header

**Q28. IPv6 compression - double colon used:**
- Only once per address

**Q29. IPv6 address types:**
- Unicast, Multicast, Anycast; No broadcast (use multicast)

**Q30. DHCP DORA:**
- Discover, Offer, Request, ACK

**Q31. ICMP ping:**
- Type 8 (echo request), Type 0 (echo reply)

**Q32. Traceroute uses:**
- ICMP Type 11 (TTL expired)

---

## Textbook End-of-Chapter Problems (Chapters 4-5)

**P1.** Explain the difference between forwarding and routing with an analogy.
**P2.** Describe the input port functions in a router.
**P3.** Explain longest prefix matching with an example.
**P4.** Compare memory, bus, and crossbar switching fabrics.
**P5.** Describe IPv4 datagram format and the purpose of each field.
**P6.** Walk through IPv4 fragmentation for a 4000-byte datagram with MTU=1500.
**P7.** Calculate subnet address, broadcast address, and usable range for 123.56.77.32/29.
**P8.** Explain NAT operation with a translation table example.
**P9.** Trace Dijkstra's algorithm for a given network topology.
**P10.** Trace Bellman-Ford distance vector algorithm iterations.
**P11.** Explain count-to-infinity problem and why "good news travels fast, bad news travels slow."
**P12.** Describe SDN architecture with control/data plane separation.
**P13.** Explain OpenFlow flow table abstraction (match + action).
**P14.** Compare 3-tier vs leaf-spine datacenter architectures.
**P15.** Explain ECMP and why per-flow hashing is used.
**P16.** Describe IPv6 header format and differences from IPv4.
**P17.** Compress/decompress IPv6 addresses using zero compression rules.
**P18.** Explain DHCP DORA process and what information is returned.
**P19.** List common ICMP message types and their uses.
**P20.** What are the protocol innovations for datacenters at each layer?