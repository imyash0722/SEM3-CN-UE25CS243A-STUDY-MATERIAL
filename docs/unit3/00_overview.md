# Computer Networks (UE25CS243A) — Unit 3

## Network Layer (Data Plane & Control Plane)

**Course**: UE25CS243A | **Semester**: III (Aug-Dec 2026) | **Credits**: 4
**Textbook**: Kurose & Ross, *Computer Networking: A Top-Down Approach*, 9th Edition (2026)
**Chapters**: 4–5 | **Hours**: 14 | **Evaluation**: ISA-2 (40 marks → 15%)

---

## 📚 Unit Overview

| Topic | Chapter | Key Concepts |
|-------|---------|--------------|
| Network Layer Services | 4.1 | Forwarding vs routing, data plane vs control plane, service models (best effort, QoS) |
| Router Internals | 4.2 | Input ports (lookup, queueing), switching fabric (memory/bus/crossbar), output ports (scheduling, buffer sizing) |
| IPv4 Datagram | 4.3 | 20-byte header, fragmentation (ID, flags, offset), TTL, protocol field, checksum |
| IPv4 Addressing | 4.4 | CIDR (a.b.c.d/x), subnets, hierarchical aggregation, NAT (private: 10/8, 172.16/12, 192.168/16) |
| Routing Algorithms | 5.1 | Link State (Dijkstra) vs Distance Vector (Bellman-Ford), convergence, scalability |
| SDN | 5.2 | Control/data separation, OpenFlow, flow tables, P4 programmable data plane |
| Datacenter Networks | 5.3 | Leaf-spine, ECMP, oversubscription, DCTCP/BBR, SDN control |
| IPv6 | 4/5 | 128-bit, 40-byte fixed header, no fragmentation, extension headers, flow label |
| ICMP | 4/5 | Error reporting, ping (echo), traceroute (TTL expired) |
| DHCP | 4/5 | DORA (Discover, Offer, Request, ACK), lease, options |

---

## 📖 Quick Navigation

- [Complete Unit 3 Notes](unit3_complete.md)

---

## ✅ Study Checklist (ISA-2)

### Network Layer Fundamentals
- [ ] Forwarding vs Routing: local action vs network-wide path determination
- [ ] Data plane (per-router, nanosecond) vs Control plane (network-wide, millisecond)
- [ ] Service models: best effort (Internet), CBR/ABR (ATM), Intserv/Diffserv (QoS)
- [ ] Longest prefix matching: choose entry with longest matching prefix

### Router Architecture
- [ ] Input port: physical → link layer → lookup (forwarding table) → switch fabric
- [ ] Switching fabrics: memory (2 bus crossings), bus (contention), crossbar/multistage (parallelism)
- [ ] HOL blocking at input queues; output queueing when fabric > line rate
- [ ] Buffer sizing: RFC 3439 = RTT × C; recent = RTT × C / √N

### IPv4
- [ ] Header fields: ver, HLEN, ToS (DiffServ+ECN), length, ID, flags (DF, MF), offset, TTL, protocol, checksum, src/dst IP
- [ ] Fragmentation: ID same for all fragments, MF flag, offset in 8-byte units, reassembly only at destination
- [ ] Why avoid fragmentation: one lost loses all, TCP uses MSS, DF bit, IPv6 routers don't fragment

### IPv4 Addressing & NAT
- [ ] CIDR: a.b.c.d/x (x = subnet bits), hierarchical aggregation
- [ ] Subnetting: subnet mask, network/host portions, broadcast address
- [ ] Private addresses: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
- [ ] NAT: outgoing → replace (src IP, port) with (NAT IP, new port), maintain translation table

### Routing Algorithms
- [ ] Dijkstra (Link State): global topology, iterative, after k iterations know k shortest paths
- [ ] Bellman-Ford (Distance Vector): Dx(y) = minᵥ {c(x,v) + Dᵥ(y)}, iterative, asynchronous
- [ ] Good news travels fast (decrease), bad news slow (count-to-infinity)
- [ ] DV vs LS: DV sends table to neighbors, LS floods link state; DV slow convergence, LS fast

### SDN
- [ ] Control/data separation, centralized controller, OpenFlow southbound API
- [ ] Flow table: match (header fields) → action (forward, drop, modify, controller)
- [ ] P4: programmable data plane, protocol-independent, parser/ingress/egress/deparser

### Datacenter Networks
- [ ] Leaf-spine: every leaf to every spine, ECMP hashing per flow
- [ ] Oversubscription: server-facing / uplink bandwidth (typical 3:1)
- [ ] Scaling: pods + super-spines (leaf-spine of leaf-spines)
- [ ] Protocol innovations: RoCE (RDMA), DCTCP (ECN fraction), hop-by-hop backpressure, SDN, locality-aware placement

### IPv6, ICMP, DHCP
- [ ] IPv6: 128-bit, 40-byte fixed header, no checksum, no fragmentation, flow label (20b), extension headers
- [ ] Address types: unicast, multicast, anycast (no broadcast)
- [ ] Transition: tunneling (IPv6 in IPv4), dual stack, NAT64
- [ ] ICMP: Type 0/8 (echo), Type 3 (unreachable), Type 11 (TTL expired for traceroute)
- [ ] DHCP: DORA (Discover/Offer/Request/ACK), lease, options (gateway, DNS, mask)

---

## 🧠 Key Formulas (Memorize)

| Formula | Equation |
|---------|----------|
| IPv4 Header Checksum | 1's complement sum of 16-bit header words |
| Longest Prefix Match | Choose entry with longest matching prefix |
| Subnet Address | IP AND Subnet Mask |
| Broadcast Address | Subnet Address OR (NOT Subnet Mask) |
| Hosts per Subnet | `2^(32 - prefix_length) - 2` |
| Dijkstra Update | `D(v) = min(D(v), D(w) + c(w,v))` |
| Bellman-Ford | `Dx(y) = minᵥ { c(x,v) + Dᵥ(y) }` |

---

## ❓ Quick Self-Test

1. **Forwarding vs Routing?**
2. **Data plane vs Control plane?**
3. **Longest prefix matching?**
4. **What is SDN?**
5. **Link State vs Distance Vector?**
6. **IPv4 fragmentation fields?**
7. **Why avoid fragmentation?**
8. **CIDR vs Classful?**
9. **NAT operation?**
10. **IPv6 improvements?**
11. **ICMP uses?**
12. **DHCP DORA?**

---

## 🎯 Exam-Relevant MCQ Patterns

- Numerical: Dijkstra step-by-step for given topology
- Numerical: Bellman-Ford distance vector updates
- Numerical: Subnetting (network/broadcast/host range for given CIDR)
- Conceptual: Longest prefix match for given forwarding table and destination
- Conceptual: SDN architecture components and message types
- Conceptual: Datacenter leaf-spine vs 3-tier
- Conceptual: IPv6 header differences from IPv4

---

*Unit 3 covers Chapters 4–5. ISA-2 evaluates Units 3 & 4 (40 marks → 15%).*