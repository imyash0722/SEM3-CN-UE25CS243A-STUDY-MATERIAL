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
[unit1/unit1_complete.md](unit1/unit1_complete.md)
- **Chapter 1**: Internet architecture, delay/loss/throughput, protocol layers
- **Chapter 2**: HTTP/HTTPS, DNS, Email, CDNs, Socket programming

### Unit 2: Transport Layer
[unit2/unit2_complete.md](unit2/unit2_complete.md)
- **Chapter 3**: UDP, Reliable data transfer (GBN/SR), TCP, Congestion control

### Unit 3: Network Layer
[unit3/unit3_complete.md](unit3/unit3_complete.md)
- **Chapter 4**: Router internals, IP, Fragmentation, Addressing, NAT, SDN
- **Chapter 5**: Routing algorithms (Link State, Distance Vector), IPv6, ICMP, DHCP

### Unit 4: Link Layer & LAN
[unit4/unit4_complete.md](unit4/unit4_complete.md)
- **Chapter 6**: Error detection, MAC protocols, Ethernet, Switches, VLANs, WiFi

---

## Key Formulae Reference (All Units)

### Unit 1: Delay, Throughput, HTTP
| Formula | Equation |
|---------|----------|
| Transmission Delay | `d_trans = L / R` |
| Propagation Delay | `d_prop = d / s` |
| Total Nodal Delay | `d_nodal = d_proc + d_queue + d_trans + d_prop` |
| End-to-End (N links) | `d_end-end = N × (d_trans + d_prop)` |
| Traffic Intensity | `ρ = (L × a) / R` |
| Avg Queuing Delay (M/M/1) | `d_queue = (L/R) × (ρ / (1-ρ))` |
| Store-and-Forward (P packets) | `d = (N + P - 1) × L / R` |
| Bottleneck Throughput | `min(R₁, R₂, ..., R_N)` |
| Non-persistent HTTP (K objects) | `K × (2×RTT + L/R)` |
| Persistent HTTP | `2×RTT + K×L/R` |

### Unit 2: Transport Layer
| Formula | Equation |
|---------|----------|
| Stop-and-Wait Utilization | `U = (L/R) / (RTT + L/R)` |
| Pipelined Utilization | `U = N × (L/R) / (RTT + L/R)` |
| Optimal Window | `N_optimal = 1 + (RTT × R) / L` |
| BDP | `BDP = R × RTT` |
| GBN Window Bound | `N ≤ 2ᵏ - 1` |
| SR Window Bound | `N ≤ 2ᵏ⁻¹` |
| EstimatedRTT | `0.875 × EstRTT + 0.125 × SampleRTT` |
| DevRTT | `0.75 × DevRTT + 0.25 × |SampleRTT - EstRTT|` |
| TimeoutInterval | `EstimatedRTT + 4 × DevRTT` |
| rwnd | `RcvBuffer - (LastByteRcvd - LastByteRead)` |
| Sender Constraint | `LastByteSent - LastByteAcked ≤ min(cwnd, rwnd)` |
| Slow Start | `cwnd += 1 MSS` per ACK |
| Congestion Avoidance | `cwnd += 1 MSS` per RTT |
| Timeout Reaction | `ssthresh = cwnd/2; cwnd = 1 MSS` |
| 3 Dup ACKs | `ssthresh = cwnd/2; cwnd = ssthresh + 3 MSS` |
| Macroscopic Throughput | `Throughput = 0.75 × W / RTT` |
| Loss Rate (Padhye) | `Throughput ≈ 1.22 × MSS / (RTT × √L)` |

### Unit 3: Network Layer
| Formula | Equation |
|---------|----------|
| IPv4 Header Checksum | 1's complement sum of 16-bit words |
| Longest Prefix Match | Choose entry with longest matching prefix |
| Subnet Address | IP AND Subnet Mask |
| Broadcast Address | Subnet Address OR (NOT Subnet Mask) |
| Hosts per Subnet | `2^(32 - prefix_length) - 2` |
| Dijkstra Update | `D(v) = min(D(v), D(w) + c(w,v))` |
| Bellman-Ford | `Dx(y) = minᵥ { c(x,v) + Dᵥ(y) }` |

### Unit 4: Link Layer
| Formula | Equation |
|---------|----------|
| CRC | Remainder of D × 2ʳ ÷ G (mod 2) |
| Ethernet Min Frame | 64 bytes = 512 bits |
| Ethernet Max Frame | 1518 bytes |
| Binary Exponential Backoff | Wait K × 512 bit times, K ∈ {0, ..., 2ⁿ⁻¹} |

---

## Important Concepts by Layer

### Application Layer (Layer 5)
- **Architectures**: Client-Server, P2P, Hybrid
- **HTTP**: Non-persistent (2 RTT/object), Persistent (2 RTT + K×trans), Pipelined (2 RTT), HTTP/2 (multiplexing), HTTP/3 over QUIC (0-RTT, no HOL blocking)
- **DNS**: Hierarchical distributed DB, recursive/iterative queries, caching (TTL), record types (A, AAAA, CNAME, MX, NS, TXT)
- **Email**: SMTP (push, port 25/587), POP3/IMAP (pull), MIME for attachments
- **CDNs**: Edge caching, GeoDNS/anycast routing, DASH adaptive streaming

### Transport Layer (Layer 4)
- **UDP**: 8-byte header, checksum (1's complement + pseudo-header), no reliability
- **RDT**: Stop-and-wait → Pipelining (GBN: cumulative ACK, retransmit all; SR: selective ACK, retransmit one)
- **TCP**: Reliable byte stream, 3-way handshake, flow control (rwnd), congestion control (cwnd)
- **RTT Estimation**: EWMA (α=0.125), DevRTT (β=0.25), Timeout = EstRTT + 4×DevRTT
- **Congestion Control**: Slow Start (exp) → CA (linear) → Fast Recovery; AIMD
- **Modern**: CUBIC (cubic function), Vegas (delay-based), BBR (model-based), ECN

### Network Layer (Layer 3)
- **Forwarding vs Routing**: Local vs global; Data plane vs Control plane
- **Router**: Input ports (lookup, queue), Switching fabric (memory/bus/crossbar), Output ports (queue, schedule)
- **IPv4**: 20-byte header, fragmentation (ID, flags, offset), TTL, protocol field
- **Addressing**: CIDR (a.b.c.d/x), subnets, hierarchical aggregation, NAT (private: 10/8, 172.16/12, 192.168/16)
- **Routing**: Link State (Dijkstra, OSPF/IS-IS) vs Distance Vector (Bellman-Ford, RIP)
- **SDN**: Control/data separation, OpenFlow, flow tables, P4 programmable data plane
- **Datacenters**: Leaf-spine, ECMP, oversubscription, DCTCP/BBR, SDN control
- **IPv6**: 128-bit, 40-byte fixed header, no fragmentation, extension headers, flow label
- **ICMP**: Error reporting, ping (echo), traceroute (TTL expired)
- **DHCP**: DORA (Discover, Offer, Request, ACK), lease, options

### Link Layer (Layer 2)
- **Error Detection**: Parity (1-bit), 2D parity (detect+correct), Checksum (1's complement), CRC (polynomial)
- **MAC Protocols**: CSMA/CD (Ethernet), CSMA/CA (WiFi), TDMA/FDMA/CDMA
- **Ethernet**: CSMA/CD (legacy), Switched full-duplex (modern), 64-1518 byte frames
- **Switches**: Self-learning (src MAC → port), flooding, forwarding table with TTL
- **VLANs**: 802.1Q tag (4 bytes, 12-bit VLAN ID), access/trunk ports, inter-VLAN routing
- **ARP**: Broadcast query → unicast reply, ARP table with TTL
- **WiFi (802.11)**: BSS/ESS, CSMA/CA, RTS/CTS (hidden terminal), association/authentication
- **Physical Layer**: NRZ, Manchester, 4B/5B, 8B/10B; twisted pair, coax, fiber, wireless

---

## Study Tips

### For Exams (ISA/ESA)
1. **Numerical problems**: Practice delay/throughput calculations, subnetting, Dijkstra, Bellman-Ford, CRC
2. **Protocol mechanisms**: Know exact header fields, state machines (TCP, ARP, DHCP)
3. **Comparisons**: Link State vs Distance Vector, GBN vs SR, TCP vs UDP, CSMA/CD vs CSMA/CA
4. **Diagrams**: Encapsulation, TCP state machine, 3-way handshake, 4-way teardown, DNS hierarchy

### Key RFCs to Know
- RFC 791: IPv4
- RFC 793: TCP
- RFC 768: UDP
- RFC 792: ICMP
- RFC 2131: DHCP
- RFC 826: ARP
- RFC 894: IP over Ethernet
- RFC 2460: IPv6
- RFC 3390: TCP initial window (10 MSS)
- RFC 6298: TCP RTO calculation
- RFC 7540: HTTP/2
- RFC 9000: QUIC

### Tools for Labs
- **Wireshark**: Packet capture/analysis (HTTP, DNS, TCP, UDP, ARP, ICMP)
- **Cisco Packet Tracer**: Network topology design, device configuration
- **Python Sockets**: TCP/UDP client-server programming
- **Mininet**: SDN/OpenFlow experimentation

---

## File Structure
```
notes/
├── MASTER_INDEX.md          (this file)
├── formulae_sheet.md        (all formulae consolidated)
├── unit1/
│   └── unit1_complete.md    (Ch 1-2: Internet + Application Layer)
├── unit2/
│   └── unit2_complete.md    (Ch 3: Transport Layer)
├── unit3/
│   └── unit3_complete.md    (Ch 4-5: Network Layer)
├── unit4/
│   └── unit4_complete.md    (Ch 6: Link Layer & LAN)
└── textbook/
    ├── kurose_ross_9th.txt  (full textbook text)
    └── kurose_ross_8th.txt  (8th edition)
```

---

## Quick Revision Checklist

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

*Generated from course materials, slides, textbook (Kurose & Ross 9th Ed), and syllabus for UE25CS243A*