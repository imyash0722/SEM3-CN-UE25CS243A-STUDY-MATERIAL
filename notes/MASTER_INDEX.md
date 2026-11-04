# Computer Networks (UE25CS243A) - Complete Course Notes

## Course Information
- **Course Code**: UE25CS243A
- **Semester**: III (Aug-Dec 2026)
- **Credits**: 4 (L-T-P-S-C: 4-0-0-4-4)
- **Textbook**: Computer Networking: A Top-Down Approach, Kurose & Ross, 9th Edition (2026), Pearson
- **Reference**: TCP/IP Protocol Suite, Forouzan, 4th Edition, McGraw-Hill

---

## Unit Structure (56 Hours Total)

| Unit | Topic | Chapters | Hours | Evaluation |
|------|-------|----------|-------|------------|
| **Unit 1** | Computer Networks & Internet + Application Layer | Ch 1-2 | 14 | ISA-1 |
| **Unit 2** | Application Layer (cont.) + Transport Layer | Ch 2-3 | 14 | ISA-1 |
| **Unit 3** | Transport Layer (TCP) + Network Layer | Ch 3-5 | 14 | ISA-2 |
| **Unit 4** | Network Layer + Link Layer & LAN | Ch 4-6 | 14 | ISA-2 |

---

## Evaluation Policy
| Component | Weight | Description |
|-----------|--------|-------------|
| **ISA-1** | 40 marks → 15% | Unit 1 & 2 (Hybrid) |
| **ISA-2** | 40 marks → 15% | Unit 3 & 4 (Hybrid) |
| **Labs** | 10 marks → 10% | 6 individual + 1 group mini-project |
| **ESA** | 50 marks → 50% | End Semester Exam |
| **Total** | **100%** | |

### Lab Structure
- **Level 1 (Banana)**: 3 labs - Cisco Packet Tracer, UDP/DNS, Ethernet/ARP
- **Level 2 (Orange)**: 3 labs - HTTP Persistent/Non-persistent, TCP Congestion, Hardware
- **Level 3 (Jackfruit)**: Group of 3, 30+ projects, SDN + Socket Programming

---

## Quick Navigation

### Unit 1: Computer Networks & Internet + Application Layer
- [Overview & Syllabus](unit1/00_overview.md)
- [Chapter 1: Computer Networks & the Internet](unit1/01_chapter1_network_fundamentals.md)
- [Chapter 2: Application Layer](unit1/02_chapter2_application_layer.md)
- [Complete Unit 1 Notes](unit1/unit1_complete.md)

### Unit 2: Transport Layer
- [Overview](unit2/00_overview.md)
- [Chapter 3: Transport Layer](unit2/03_chapter3_transport_layer.md)
- [Complete Unit 2 Notes](unit2/unit2_complete.md)

### Unit 3: Network Layer
- [Overview](unit3/00_overview.md)
- [Complete Unit 3 Notes](unit3/unit3_complete.md)

### Unit 4: Link Layer & LAN
- [Overview](unit4/00_overview.md)
- [Complete Unit 4 Notes](unit4/unit4_complete.md)

### Reference
- [Complete Formulae Sheet](formulae_sheet.md) — All formulas for exams
- [Master Index & Study Checklist](MASTER_INDEX.md) — Full topic checklist

---

## 📚 Detailed Topic Index

### Unit 1 (ISA-1)

#### Chapter 1: Computer Networks and the Internet
- [ ] **1.1 What Is the Internet?**
  - Nuts-and-bolts vs services view
  - Protocol definition (syntax, semantics, timing)
  - Human protocol analogy
- [ ] **1.2 The Network Edge**
  - Access networks: DSL, Cable, FTTH, 5G, Enterprise
  - Physical media: Twisted pair, Coax, Fiber, Radio
  - Dedicated vs shared access
- [ ] **1.3 The Network Core**
  - Packet switching vs circuit switching
  - Store-and-forward, statistical multiplexing
  - Network of networks: Tier-1/2/3 ISPs, IXPs, CDNs
  - Peering vs transit
- [ ] **1.4 Delay, Loss, and Throughput**
  - Four delay components: processing, queuing, transmission, propagation
  - Caravan analogy (tollbooth)
  - Traffic intensity ρ = La/R, queuing delay formula
  - End-to-end delay, traceroute
  - Bottleneck throughput, M flows sharing
- [ ] **1.5 Protocol Layers**
  - 5-layer Internet model vs OSI 7-layer
  - Encapsulation/decapsulation (Matryoshka dolls)
- [ ] **1.6 Networks Under Attack**
  - Malware, DoS/DDoS, sniffing, spoofing, MitM, DNS attacks
- [ ] **1.7 History of Computer Networking**
  - 1961-1972: ARPANET, NCP
  - 1972-1980: TCP/IP, Ethernet
  - 1980-1990: NSFNET, DNS, congestion control
  - 1990s: Web, commercialization
  - 2000s-present: Broadband, mobile, cloud, SDN, IoT, QUIC

#### Chapter 2: Application Layer
- [ ] **2.1 Principles of Network Applications**
  - Client-server vs P2P architectures
  - Processes, sockets (API), addressing (IP + port)
  - Transport services: reliable, throughput, timing, security
  - TCP vs UDP services
  - Application-layer protocol definition
- [ ] **2.2 The Web and HTTP**
  - HTTP overview: stateless, URL format
  - Non-persistent vs persistent vs pipelined (RTT calculations)
  - HTTP message format (request/response)
  - Cookies (Set-Cookie, Cookie headers)
  - Browser caching (304 Not Modified)
  - HTTP/2: binary framing, multiplexing, HPACK, server push
  - HTTP/3 over QUIC: 0-RTT, connection migration, no HOL blocking
- [ ] **2.3 Electronic Mail**
  - SMTP (push, port 25/587, 7-bit ASCII)
  - Mail formats (RFC 5322, MIME)
  - POP3/IMAP/HTTP for mail access
- [ ] **2.4 DNS**
  - Hierarchical distributed DB: root → TLD → authoritative
  - Recursive vs iterative queries
  - Caching with TTL
  - Record types: A, AAAA, CNAME, MX, NS, TXT, SRV
  - DNSSEC, DoH/DoT
- [ ] **2.5 Video Streaming and CDNs**
  - Stored, live, interactive video
  - DASH (MPD, adaptive streaming)
  - CDN operation: request routing, content placement, delivery
  - Netflix/YouTube case studies
- [ ] **2.6 Socket Programming**
  - UDP: sendto/recvfrom (address included)
  - TCP: connect/accept (welcoming + connection sockets)
  - Python examples for both

---

### Unit 2 (ISA-1)

#### Chapter 3: Transport Layer
- [ ] **3.1 Introduction and Transport-Layer Services**
  - Transport vs network layer (process-to-process vs host-to-host)
  - TCP vs UDP feature comparison
- [ ] **3.2 Multiplexing and Demultiplexing**
  - UDP: 2-tuple (dst IP, dst port)
  - TCP: 4-tuple (src IP, src port, dst IP, dst port)
- [ ] **3.3 UDP**
  - 8-byte header structure
  - Checksum: 1's complement + pseudo-header
- [ ] **3.4 Principles of Reliable Data Transfer**
  - rdt 1.0 → 3.0 evolution
  - Stop-and-wait utilization
  - Pipelining: GBN vs SR
- [ ] **3.4.3 Go-Back-N (GBN)**
  - Sender/receiver window, cumulative ACK
  - Window bound: N ≤ 2ᵏ - 1
  - Retransmit ALL on timeout
  - Example: 18 transmissions (N=10, every 5th lost)
- [ ] **3.4.4 Selective Repeat (SR)**
  - Per-packet timers, individual ACKs
  - Window bound: N ≤ 2ᵏ⁻¹
  - Retransmit only timed-out packet
  - Example: 12 transmissions (same conditions)
- [ ] **3.5 TCP**
  - Segment structure: seq/ACK numbers, flags, window, options
  - MSS = MTU - 40
  - RTT estimation (EWMA α=0.125, DevRTT β=0.25)
  - Timeout = EstRTT + 4×DevRTT, Karn's Algorithm
  - Sender events, fast retransmit (3 dup ACKs), fast recovery
  - Flow control (rwnd)
  - 3-way handshake, 4-way teardown, TIME_WAIT
- [ ] **3.6-3.7 Congestion Control**
  - Causes/costs of congestion
  - End-end vs network-assisted
  - Slow Start, Congestion Avoidance, Fast Recovery
  - AIMD sawtooth
  - Tahoe, Reno, CUBIC comparison
  - ECN (CE/ECE/CWR bits)
  - Fairness (R/K)
- [ ] **3.8 Evolution**
  - TCP (kernel) vs QUIC (user-space)
  - HTTP/3 over QUIC

---

### Unit 3 (ISA-2)

#### Chapter 4: Network Layer - Data Plane
- [ ] **4.1 Overview**
  - Forwarding vs routing
  - Data plane vs control plane
  - Service models (best effort, CBR, ABR, Intserv, Diffserv)
- [ ] **4.2 Router Internals**
  - Routing processor (control plane, ms) vs switching fabric (data plane, ns)
  - Input ports: physical → link → lookup (match+action) → queue
  - Longest prefix matching (TCAM)
  - Switching fabrics: memory, bus, crossbar/Clos
  - HOL blocking at input queues
  - Output port queueing, buffer sizing (RTT×C, RTT×C/√N)
  - Buffer management: tail drop, priority, ECN/RED
- [ ] **4.3 IPv4**
  - Datagram format (20-byte header)
  - Fragmentation: ID, flags (MF, DF), offset (8-byte units)
  - Why avoid fragmentation
- [ ] **4.4 IPv4 Addressing**
  - CIDR (a.b.c.d/x), subnets
  - Hierarchical addressing, route aggregation
  - Classful vs classless
  - ICANN, RIRs, NAT for exhaustion
- [ ] **4.5 NAT**
  - Private address spaces (10/8, 172.16/12, 192.168/16)
  - Translation table, outgoing/incoming processing
  - NAT traversal (static port forwarding)

#### Chapter 5: Network Layer - Control Plane
- [ ] **5.1 Routing Algorithms**
  - Graph abstraction G=(N,E), c(x,y)
  - Global (Link State) vs Decentralized (Distance Vector)
  - Static vs Dynamic
- [ ] **5.2 Link-State (Dijkstra)**
  - Algorithm steps, initialization, loop
  - Example with 6 nodes
  - Forwarding table construction
- [ ] **5.3 Distance Vector (Bellman-Ford)**
  - BF equation: Dx(y) = minᵥ {c(x,v) + Dᵥ(y)}
  - Iterative algorithm, convergence
  - Count-to-infinity (bad news travels slow)
  - DV vs LS comparison table
- [ ] **5.4 SDN**
  - Control/data separation, centralized controller
  - OpenFlow: match+action, flow tables
  - P4 programmable data plane
- [ ] **5.5 Datacenter Networks**
  - North-South vs East-West traffic
  - 3-tier vs leaf-spine
  - Oversubscription, ECMP (per-flow hashing)
  - Protocol innovations: RoCE, DCTCP, hop-by-hop backpressure, SDN, locality-aware placement

#### IPv6, ICMP, DHCP
- [ ] **IPv6**: 128-bit, 40-byte fixed header, no checksum/fragmentation, flow label, extension headers, address types (unicast/multicast/anycast), transition (tunneling, dual stack)
- [ ] **ICMP**: Error reporting, ping (Type 8/0), traceroute (Type 11)
- [ ] **DHCP**: DORA (Discover/Offer/Request/ACK), lease, options (gateway, DNS, mask)

---

### Unit 4 (ISA-2)

#### Chapter 6: Link Layer and LANs
- [ ] **6.1 Introduction**
  - Nodes, links, frames
  - Services: framing, link access, MAC addressing, reliable delivery, error detection/correction, flow control, half/full duplex
  - Implementation: NIC/on-chip
- [ ] **6.2 Error Detection and Correction**
  - Single-bit parity (even), 2D parity (detect+correct)
  - Internet checksum (1's complement)
  - CRC (polynomial division, D×2ʳ mod G)
- [ ] **6.3 Multiple Access Protocols**
  - Channel partitioning (TDMA/FDMA/CDMA)
  - Random access (CSMA, CSMA/CD, CSMA/CA)
  - Taking turns (polling, token)
  - CSMA/CD: listen before transmit, binary exponential backoff
  - CSMA/CA: DIFS, backoff, ACK, RTS/CTS
  - Modern Ethernet: no collision detection
- [ ] **6.4 Switched LANs**
  - MAC addresses (48-bit, flat, portable) vs IP (32-bit, hierarchical)
  - Private WiFi addresses
  - ARP: broadcast query → unicast reply, ARP table with TTL
  - Routing to another subnet (IP end-to-end, MAC per-hop)
- [ ] **6.5 Ethernet**
  - Bus vs switched topology
  - Frame structure (preamble, addresses, type, data, CRC)
  - Min 64B, max 1518B
  - Unreliable, connectionless
- [ ] **6.6 Ethernet Switches**
  - Self-learning (src MAC → port), flooding, forwarding
  - Interconnecting switches
  - Switches vs routers (L2 vs L3)
  - Broadcast domain, VLANs
- [ ] **6.7 VLANs**
  - 802.1Q tag (4 bytes: TPID, priority, DEI, VLAN ID 12b)
  - Access vs trunk ports, native VLAN
  - VLAN-aware forwarding, inter-VLAN routing
- [ ] **6.8 A Day in the Life**
  - DHCP → ARP → DNS → TCP handshake → HTTP → Link layer
- [ ] **6.9 Physical Layer**
  - Encoding: NRZ, Manchester, 4B/5B, 8B/10B
  - Media: twisted pair, coax, fiber, wireless
- [ ] **6.10 Wireless LANs (802.11)**
  - BSS/ESS, channels, association
  - Standards evolution (b/g/n/ac/ax/be)
  - CSMA/CA, RTS/CTS, hidden/exposed terminal
  - Power management

---

## 🧮 Key Formulae by Chapter

### Chapter 1
- `d_trans = L / R`, `d_prop = d / s`, `d_nodal = d_proc + d_queue + d_trans + d_prop`
- `ρ = (L × a) / R`, `d_queue = (L/R) × (ρ / (1-ρ))`
- `d = N × L / R`, `d = (N + P - 1) × L / R`
- `Throughput = min(R₁, ..., R_N)`

### Chapter 2
- Non-persistent: `K × (2×RTT + L/R)`
- Persistent: `2×RTT + K×L/R`

### Chapter 3
- Stop-and-Wait: `U = (L/R) / (RTT + L/R)`
- GBN: `N ≤ 2ᵏ - 1`, SR: `N ≤ 2ᵏ⁻¹`
- `EstRTT = 0.875×EstRTT + 0.125×SampleRTT`
- `DevRTT = 0.75×DevRTT + 0.25×|SampleRTT-EstRTT|`
- `Timeout = EstRTT + 4×DevRTT`
- `rwnd = RcvBuffer - (LastByteRcvd - LastByteRead)`
- `cwnd += 1 MSS` per ACK (SS), `cwnd += 1 MSS` per RTT (CA)
- Timeout: `ssthresh=cwnd/2; cwnd=1 MSS`
- 3 Dup ACKs: `ssthresh=cwnd/2; cwnd=ssthresh+3 MSS`
- Throughput: `0.75×W/RTT`, `1.22×MSS/(RTT×√L)`

### Chapters 4-5
- Subnet: `IP AND Mask`, Broadcast: `Subnet OR (NOT Mask)`
- Hosts: `2^(32-prefix) - 2`
- Dijkstra: `D(v) = min(D(v), D(w) + c(w,v))`
- Bellman-Ford: `Dx(y) = minᵥ {c(x,v) + Dᵥ(y)}`

### Chapter 6
- CRC: Remainder of `D × 2ʳ ÷ G`
- Ethernet min: 64B, max: 1518B
- Backoff: `K × 512 bit times`, `K ∈ {0, ..., 2ⁿ⁻¹}`

---

## ✅ Complete Study Checklist (All Units)

### Unit 1 ✓
- [ ] 4 delay components + formulas
- [ ] Packet vs circuit switching
- [ ] Protocol layering (OSI vs TCP/IP)
- [ ] HTTP connection types + timing
- [ ] DNS hierarchy + query types
- [ ] Socket programming (UDP vs TCP)

### Unit 2 ✓
- [ ] UDP header + checksum
- [ ] RDT evolution (1.0 → 3.0)
- [ ] GBN vs SR (window bounds!)
- [ ] TCP segment structure
- [ ] RTT estimation + Karn's algorithm
- [ ] Flow control (rwnd)
- [ ] 3-way handshake + 4-way teardown
- [ ] Slow Start / CA / Fast Recovery
- [ ] CUBIC, Vegas, BBR, ECN

### Unit 3 ✓
- [ ] Router architecture (input/output/switching)
- [ ] Longest prefix matching
- [ ] IPv4 header + fragmentation
- [ ] CIDR, subnetting, NAT
- [ ] Dijkstra step-by-step
- [ ] Bellman-Ford + count-to-infinity
- [ ] SDN architecture + OpenFlow
- [ ] Datacenter: leaf-spine, ECMP
- [ ] IPv6 addressing + transition
- [ ] ICMP + DHCP DORA

### Unit 4 ✓
- [ ] Error detection: parity, checksum, CRC
- [ ] CSMA/CD vs CSMA/CA
- [ ] Ethernet frame + min/max size
- [ ] Switch self-learning + forwarding
- [ ] VLAN tag + access/trunk
- [ ] ARP operation
- [ ] 802.11 architecture + CSMA/CA
- [ ] Hidden/exposed terminal
- [ ] Physical layer encoding

---

## 🎯 Exam-Relevant MCQ Patterns

### Numerical
- Delay/throughput calculations (given link rates, distances, packet size)
- Traffic intensity and queuing delay
- Subnetting (network/broadcast/host range)
- Dijkstra/Bellman-Ford iterations
- CRC calculation
- RTT estimation (EstRTT, DevRTT, Timeout)

### Conceptual
- Identify delay component from scenario
- HTTP connection type from timing
- DNS query type from description
- TCP state machine transitions
- Congestion control phase from cwnd behavior
- Longest prefix match from forwarding table

### Code
- Identify socket type (UDP/TCP) from Python snippet
- ARP request/reply flow

---

## 🔧 Lab Components (10%)

| Level | Labs | Topics |
|-------|------|--------|
| **Banana (L1)** | 3 | Cisco Packet Tracer, UDP/DNS, Ethernet/ARP |
| **Orange (L2)** | 3 | HTTP Persistent/Non-persistent, TCP Congestion, Hardware |
| **Jackfruit (L3)** | Group of 3 | 30+ projects, SDN + Socket Programming |

---

## 🔑 Key RFCs to Know

| RFC | Protocol |
|-----|----------|
| 791 | IPv4 |
| 793 | TCP |
| 768 | UDP |
| 792 | ICMP |
| 2131 | DHCP |
| 826 | ARP |
| 894 | IP over Ethernet |
| 2460 | IPv6 |
| 3390 | TCP initial window (10 MSS) |
| 6298 | TCP RTO calculation |
| 7540 | HTTP/2 |
| 9000 | QUIC |

---

## 📁 File Structure
```
notes/
├── MASTER_INDEX.md          (this file)
├── formulae_sheet.md        (all formulae consolidated)
├── unit1/
│   ├── 00_overview.md
│   ├── 01_chapter1_network_fundamentals.md
│   ├── 02_chapter2_application_layer.md
│   └── unit1_complete.md
├── unit2/
│   ├── 00_overview.md
│   ├── 03_chapter3_transport_layer.md
│   └── unit2_complete.md
├── unit3/
│   ├── 00_overview.md
│   └── unit3_complete.md
├── unit4/
│   ├── 00_overview.md
│   └── unit4_complete.md
└── textbook/
    ├── kurose_ross_9th.txt  (full textbook text)
    └── kurose_ross_8th.txt  (8th edition)
```

---

*Generated from course materials, slides, textbook (Kurose & Ross 9th Ed), and syllabus for UE25CS243A*