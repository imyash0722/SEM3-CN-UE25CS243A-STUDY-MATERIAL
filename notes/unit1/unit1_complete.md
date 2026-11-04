# Unit 1: Complete Study Guide — Computer Networks & Application Layer

# Computer Networks (UE25CS243A) — Unit 1

## Internet & Application Layer

**Course**: UE25CS243A | **Semester**: III (Aug-Dec 2026) | **Credits**: 4
**Textbook**: Kurose & Ross, *Computer Networking: A Top-Down Approach*, 9th Edition (2026)
**Chapters**: 1–2 | **Hours**: 14 | **Evaluation**: ISA-1 (40 marks → 15%)

---

## 📚 Unit Overview

| Topic | Chapter | Key Concepts |
|-------|---------|--------------|
| Internet Architecture | Ch 1 | Nuts-and-bolts vs services view, protocol layers, encapsulation |
| Network Edge & Core | Ch 1 | Access networks (DSL, Cable, FTTH, 5G), packet vs circuit switching, ISP hierarchy |
| Delay, Loss, Throughput | Ch 1 | 4 delay components, queuing theory (M/M/1), traffic intensity, bottleneck link |
| Protocol Layers | Ch 1 | 5-layer Internet model, OSI 7-layer, encapsulation/decapsulation |
| Application Architectures | Ch 2 | Client-server vs P2P, sockets, transport services (TCP vs UDP) |
| HTTP/HTTPS | Ch 2 | Non-persistent/persistent/pipelined, HTTP/2, HTTP/3 over QUIC, TLS 1.3 |
| DNS | Ch 2 | Hierarchical distributed DB, recursive/iterative queries, caching, record types |
| Email | Ch 2 | SMTP, POP3/IMAP, MIME |
| CDNs & Streaming | Ch 2 | DASH, CDN operation, Netflix/YouTube case studies |
| Socket Programming | Ch 2 | UDP (sendto/recvfrom), TCP (connect/accept), Python examples |

---

## 📖 Quick Navigation

- [Chapter 1: Computer Networks & Internet](01_chapter1_network_fundamentals.md)
- [Chapter 2: Application Layer](02_chapter2_application_layer.md)
- [Complete Unit 1 Notes](unit1_complete.md)

---

## ✅ Study Checklist (ISA-1)

### Chapter 1: Network Fundamentals
- [ ] Four delay components + formulas (`d_trans = L/R`, `d_prop = d/s`, `d_queue = (L/R)×ρ/(1-ρ)`)
- [ ] Packet switching vs circuit switching (statistical multiplexing, store-and-forward)
- [ ] Traffic intensity ρ = La/R, stability condition (ρ ≤ 1)
- [ ] End-to-end delay for N links
- [ ] Bottleneck throughput = min(R₁, R₂, ..., Rₙ)
- [ ] Protocol layering: 5-layer Internet model vs OSI 7-layer
- [ ] Encapsulation: message → segment → datagram → frame → bits
- [ ] Network structure: Tier-1/2/3 ISPs, IXPs, CDNs, peering vs transit

### Chapter 2: Application Layer
- [ ] Client-server vs P2P architectures (self-scalability)
- [ ] Socket API: UDP (sendto/recvfrom) vs TCP (connect/accept, welcoming socket)
- [ ] Transport services: TCP (reliable, ordered, flow/congestion control) vs UDP (unreliable)
- [ ] HTTP: Non-persistent (2 RTT/object) vs Persistent (2 RTT + K×trans) vs Pipelined (2 RTT)
- [ ] HTTP/2: Binary framing, multiplexing, HPACK, server push
- [ ] HTTP/3 over QUIC: 0-RTT, connection migration, no HOL blocking
- [ ] Cookies: Set-Cookie/Cookie headers, session state, third-party tracking
- [ ] DNS: Hierarchical DB, root→TLD→authoritative, recursive vs iterative, TTL, record types (A, AAAA, CNAME, MX, NS, TXT)
- [ ] Email: SMTP (push, port 25/587), POP3/IMAP (pull), MIME
- [ ] CDNs: Edge caching, GeoDNS/anycast, DASH adaptive streaming
- [ ] Socket programming: UDP vs TCP client/server patterns in Python

---

## 🧠 Key Formulas (Memorize)

| Formula | Equation |
|---------|----------|
| Transmission Delay | `d_trans = L / R` |
| Propagation Delay | `d_prop = d / s` |
| Total Nodal Delay | `d_nodal = d_proc + d_queue + d_trans + d_prop` |
| End-to-End (N links) | `N × (d_trans + d_prop)` |
| Traffic Intensity | `ρ = (L × a) / R` |
| Avg Queuing Delay (M/M/1) | `d_queue = (L/R) × (ρ / (1-ρ))` |
| Store-and-Forward (P pkts) | `d = (N + P - 1) × L / R` |
| Bottleneck Throughput | `min(R₁, R₂, ..., R_N)` |
| Non-persistent HTTP (K obj) | `K × (2×RTT + L/R)` |
| Persistent HTTP | `2×RTT + K×L/R` |

---

## ❓ Quick Self-Test

1. **Difference between packet switching and circuit switching?**
2. **What are the four delay components in a router?**
3. **When does packet loss occur?**
4. **What determines end-to-end throughput?**
5. **Client-server vs P2P?**
6. **TCP vs UDP services?**
7. **Non-persistent vs persistent HTTP?**
8. **How do cookies work?**
9. **What is DNS and how does it work?**
10. **UDP vs TCP socket programming differences?**

---

## 🎯 Exam-Relevant MCQ Patterns

- Numerical: Calculate end-to-end delay given link rates, distances, packet size
- Numerical: Traffic intensity and queuing delay for given arrival rate
- Conceptual: Identify delay component from scenario (propagation vs transmission)
- Conceptual: HTTP connection type from timing description
- Conceptual: DNS query type (recursive vs iterative) from description
- Code: Identify socket type (UDP/TCP) from Python snippet

---

*Unit 1 covers Chapters 1–2. ISA-1 evaluates Units 1 & 2 (40 marks → 15%).*

---

# Unit 1: Computer Networks and the Internet (Chapter 1)

## 1.1 What Is the Internet?

### A Nuts-and-Bolts Description
The Internet is a **global network of networks** - a complex infrastructure consisting of:
- **End systems (hosts)**: Computers, smartphones, servers, IoT devices (19 billion devices in 2025, 29 billion by 2030)
- **Communication links**: Fiber optics, copper wire, coaxial cable, radio spectrum, satellite links
- **Packet switches**: Routers and link-layer switches that forward packets
- **Protocols**: TCP, IP, HTTP, DNS, etc. that control communication

**Key concept**: The Internet provides a **service model** to applications - a set of operations (send/receive) and expected behavior (reliability, timing, etc.)

### A Services Description
The Internet provides two key services to applications:
1. **Connectionless service (UDP)**: Unreliable, no handshake, minimal overhead
2. **Connection-oriented service (TCP)**: Reliable, in-order byte stream with flow/congestion control

Applications access these services via **sockets** - the API between application and transport layer. The socket interface is the "door" through which applications send/receive messages.

### What Is a Protocol?
A **protocol** defines the format, order, and actions taken on transmission/receipt of messages among communicating entities.
- **Syntax**: Message format, data representation
- **Semantics**: Meaning of fields, actions to take
- **Timing**: When to send, how fast, timeouts

**Example**: HTTP defines how a client requests a web page and how a server responds.

**Human analogy**: "Hi" → "Hi" → "What's the time?" → "2:00" - specific messages sent, specific actions taken on receipt.

---

## 1.2 The Network Edge

### 1.2.1 Access Networks
Access networks connect end systems to the first router (edge router). Types:

| Access Network | Technology | Typical Speed | Characteristics |
|----------------|------------|---------------|-----------------|
| **DSL** | Digital Subscriber Line | ~24 Mbps downstream (up to 1 Gbps latest standard) | Uses existing telephone lines; dedicated per household; asymmetric (downstream > upstream); distance limited to ~5-10 miles from CO |
| **Cable** | HFC (Hybrid Fiber-Coax) | ~1-2 Gbps downstream (DOCSIS 3.0: 1.2 Gbps) | Shared broadcast medium; uses DOCSIS; asymmetric; collision possible on upstream |
| **FTTH** | Fiber to the Home | ~1-10 Gbps | Dedicated fiber; highest speeds; PON (passive optical network) common |
| **5G/Fixed Wireless** | Cellular | ~100 Mbps - 1 Gbps | Mobile/wireless; shared spectrum; beam-forming |
| **Enterprise (Ethernet/WiFi)** | 802.3/802.11 | ~1-100 Gbps | Wired/wireless LAN in organizations |
| **LEO Satellites** | Low Earth Orbit | ~100 Mbps | Rural/remote; ~10ms latency (vs 280ms GEO) |

**Key distinction**: 
- **Dedicated access** (DSL, FTTH): Bandwidth not shared
- **Shared access** (Cable, WiFi, 5G): Bandwidth shared among users

**DSL detail**: Uses telephone line with frequency-division multiplexing: high-speed downstream (50 kHz-1 MHz), medium-speed upstream (4-50 kHz), telephone (0-4 kHz). DSLAM at central office.

**Cable detail**: HFC = fiber to neighborhood junctions, coax to homes. CMTS at head end. Shared broadcast medium - all packets travel to all homes.

**FTTH detail**: PON architecture - OLT at CO, splitter combines <100 homes on shared fiber, ONT at home.

### 1.2.2 Physical Media
| Medium | Type | Characteristics |
|--------|------|-----------------|
| **Twisted Pair (Cat 5e/6/6a/7)** | Copper | 100m max; 1-10 Gbps; susceptible to interference; dominant for LANs |
| **Coaxial Cable** | Copper | Longer distances; used in cable TV/HFC; shared medium; concentric conductors |
| **Fiber Optics (SMF/MMF)** | Glass | Km distances; 10-100+ Gbps; immune to EMI; low attenuation; preferred for long-haul |
| **Radio Spectrum** | Wireless | WiFi, 4G/5G, satellite; shared medium; variable propagation |
| **Terrestrial Radio** | Wireless | Short (1-2m), local (10-100s m), wide-area (10s km) |
| **Satellite Radio** | Wireless | GEO: 36,000km, 280ms RTT; LEO: much lower latency |

---

## 1.3 The Network Core

### 1.3.1 Packet Switching
The Internet uses **packet switching** (not circuit switching):
- Messages broken into **packets** (typically 1-1500 bytes)
- Each packet routed independently through network
- **Store-and-forward**: Each switch receives entire packet before forwarding to next link
- **Statistical multiplexing**: Links shared on demand; no reservation

**Store-and-forward delay**: For N links of rate R, single packet delay = N × L/R
For P packets back-to-back: delay = (N + P - 1) × L/R

**Example**: 3 packets, 2 links (1 router). At t=0 send pkt1. At t=L/R router begins forwarding pkt1, source sends pkt2. At t=2L/R dest receives pkt1, router receives pkt2. At t=3L/R dest receives pkt2, router receives pkt3. At t=4L/R all 3 received.

**Advantages over Circuit Switching**:
- Efficient for bursty data traffic (statistical multiplexing)
- No connection setup delay
- Better resource utilization
- Robust (packets can take different paths)

**Statistical Multiplexing Example**: 1 Gbps link, 1 Mbps/user, 10% active. Circuit: 1000 users max. Packet: ~5000+ users (statistically, low blocking).

### 1.3.2 Circuit Switching (for comparison)
- Dedicated end-to-end path reserved for duration of connection
- Constant bandwidth guaranteed (FDM or TDM)
- Used in traditional telephone networks
- Inefficient for bursty traffic (resources idle during silence)
- **FDM**: Frequency bands (e.g., 4 kHz per call)
- **TDM**: Time slots in frames (e.g., 8000 frames/sec × 8 bits = 64 kbps per circuit)

### 1.3.3 A Network of Networks
The Internet = **Interconnected ISPs**:

**Network Structure Evolution**:
1. **Structure 1**: Single global transit ISP (customer-provider)
2. **Structure 2**: Multiple global transit ISPs (must interconnect)
3. **Structure 3**: Regional ISPs added (multi-tier hierarchy)
4. **Structure 4**: PoPs, multi-homing, peering, IXPs
5. **Structure 5**: Content provider networks (Google, Netflix, etc.)

**Tiered ISPs**:
1. **Tier-1 ISPs**: Global reach, peer with each other settlement-free (AT&T, NTT, Tata, Level 3)
2. **Tier-2/Regional ISPs**: Regional, buy transit from Tier-1
3. **Tier-3/Access ISPs**: Local, connect end users

**Peering vs Transit**:
- **Peering**: Mutual agreement, no payment (typically Tier-1 to Tier-1, or same-level ISPs)
- **Transit**: Customer pays provider for global connectivity

**IXPs**: Internet Exchange Points - physical locations where ISPs peer (NIXI: 77 nodes in India, >1.5 Tbps peak)

**Content Providers**: Google, Netflix, Akamai, Cloudflare - deploy private networks, peer at IXPs, bypass tier-1 when possible

---

## 1.4 Delay, Loss, and Throughput in Packet-Switched Networks

### 1.4.1 Overview of Delay in Packet-Switched Networks
Total nodal delay at each router:
```
d_nodal = d_proc + d_queue + d_trans + d_prop
```

| Delay Component | Formula | Description |
|-----------------|---------|-------------|
| **Processing Delay (d_proc)** | ~microseconds | Header check, routing table lookup, bit-error check |
| **Queuing Delay (d_queue)** | Variable | Time waiting in output buffer; depends on traffic intensity |
| **Transmission Delay (d_trans)** | L / R | Time to push packet bits onto link |
| **Propagation Delay (d_prop)** | d / s | Time for bits to travel across link (speed of light ~2×10⁸ m/s in fiber) |

**Transmission Delay**: `d_trans = L / R`
- L = packet length (bits)
- R = link bandwidth (bps)

**Propagation Delay**: `d_prop = d / s`
- d = link length (meters)
- s = propagation speed (m/s)

**Transmission vs Propagation**: 
- Transmission: function of packet length & link rate, NOT distance
- Propagation: function of distance, NOT packet length or rate

### 1.4.2 Caravan Analogy (Tollbooth)
- **Cars = bits**, **Caravan = packet**, **Tollbooth = router**
- **Transmission delay** = time to push entire caravan through tollbooth (10 cars × 12 sec = 120 sec)
- **Propagation delay** = time for car to travel between tollbooths (100 km / 100 km/hr = 1 hr)
- **Total** = transmission + propagation = 62 minutes

**Key insight**: If transmission delay > propagation delay, first cars arrive at next tollbooth before last cars leave first tollbooth. Same in networks - first bits arrive at next router while remaining bits still being transmitted.

### 1.4.3 Numerical Examples (Which Delay Wins?)
**Scenario A**: 5 MB image, 1 Gbps fiber, 12,000 km away
- d_prop = 12,000,000 / (2×10⁸) = 60 ms
- d_trans = (5×10⁶×8) / 10⁹ = 40 ms
- **Propagation dominates**

**Scenario B**: 5 MB image, 1 Mbps dial-up, next door
- d_prop ≈ negligible
- d_trans = (5×10⁶×8) / 10⁶ = 40 seconds
- **Transmission dominates**

### 1.4.4 Queuing Delay and Packet Loss
**Traffic Intensity**: `ρ = (L × a) / R = λL / R`
- a = average packet arrival rate (packets/sec)
- λ = a (arrival rate)
- ρ = fraction of time link is busy

| Traffic Intensity | Behavior |
|-------------------|----------|
| ρ < 1 | Stable, finite average queue |
| ρ → 1 | Queue grows, delay increases dramatically |
| ρ > 1 | Unstable, queue → ∞, packets dropped |

**Average Queuing Delay (M/M/1 queue)**:
```
d_queue = (L/R) × (ρ / (1-ρ))
```

**Congestion Multiplier**: `ρ/(1-ρ)`
- ρ=0.5 → 1× (delay = 1 transmission time)
- ρ=0.8 → 4×
- ρ=0.9 → 9×
- ρ=0.99 → 99×

**Packet Loss**: Occurs when buffer is full (finite capacity). Lost packets may be retransmitted (TCP) or lost forever (UDP).

**Numerical Example**: R=10 Mbps, L=1000 bits → d_trans=100 μs. At a=1000 pkt/s, I=0.1 → d_queue≈11.1 μs. Raise to a=9000 (I=0.9) → d_queue=900 μs (9× arrivals → 81× delay).

### 1.4.5 End-to-End Delay
For N links (no queuing/processing):
```
d_end-end = N × (d_trans + d_prop)
```

General case:
```
d_end-end = Σ(d_proc_i + d_queue_i + d_trans_i + d_prop_i)
```

**Traceroute**: Measures RTT to each router by sending packets with TTL=1,2,3... Router with TTL=0 sends ICMP Time Exceeded. Three probes per hop.

### 1.4.6 Throughput in Computer Networks
**Instantaneous Throughput**: Rate at which receiver gets bits
**Average Throughput**: `F / T` (file size / transfer time)

**Bottleneck Link**: The link with minimum rate along path
```
Throughput = min(R₁, R₂, ..., R_N)  (no cross traffic)
```

**M flows sharing bottleneck R**:
```
Throughput_per_flow = R / M
```

**Interactive Exercise Example**: 
- 4 servers, 4 clients, 4 three-hop paths sharing middle link R=300 Mbps
- RS=50 Mbps (server links), RC=90 Mbps (client links)
- Per-connection throughput = min(50, 90, 300/4) = 50 Mbps
- Bottleneck = Rs (50 Mbps)
- Server utilization = 50/50 = 1.0
- Client utilization = 50/90 = 0.56
- Shared link utilization = 50/(300/4) = 0.67

---

## 1.5 Protocol Layers and Their Service Models

### 1.5.1 Layered Architecture
**Five-Layer Internet Model**:
| Layer | Name | Key Protocols | Responsibility |
|-------|------|---------------|----------------|
| 5 | Application | HTTP, DNS, SMTP, FTP | Network applications |
| 4 | Transport | TCP, UDP | Process-to-process delivery |
| 3 | Network | IP, ICMP, routing protocols | Host-to-host delivery, routing |
| 2 | Link | Ethernet, WiFi, PPP | Node-to-node delivery |
| 1 | Physical | Cables, radio waves | Bit transmission |

**OSI 7-Layer Model** (for reference):
7. Application, 6. Presentation, 5. Session, 4. Transport, 3. Network, 2. Data Link, 1. Physical
- Internet stack "missing" presentation & session - implemented in application if needed

**Why Layering?**:
- Explicit structure for complex systems
- Modularization eases maintenance/updating
- Change in layer implementation transparent to rest of system

### 1.5.2 Encapsulation
Each layer adds its own **header** (and sometimes trailer):
```
Application Message (M)
    → Transport Header (Ht) + M = Segment (TCP) / Datagram (UDP)
        → IP Header (Hn) + Segment = Datagram
            → Link Header (Hl) + Datagram + Link Trailer = Frame
                → Physical layer transmits bits
```

**Matryoshka Dolls Analogy**: Nested encapsulation like stacking dolls.

**At each router**: Decapsulate to link layer, process IP header, re-encapsulate in new frame.
- Link-layer switch: layers 1-2 only
- Router: layers 1-3
- Host: all 5 layers

---

## 1.6 Networks Under Attack
Types of attacks:
1. **Malware**: Viruses, worms, botnets, ransomware (self-replicating, spreads exponentially)
2. **DoS/DDoS**: Overwhelm target with traffic (vulnerability attack, bandwidth flooding, connection flooding)
3. **Sniffing/Eavesdropping**: Passive interception (wireless, cable, Ethernet broadcast)
4. **Spoofing**: Fake source IP/email (IP spoofing)
5. **Man-in-the-Middle**: Intercept and modify
6. **DNS Attacks**: Cache poisoning, hijacking

**Defense**: Firewalls, IDS/IPS, encryption (TLS/IPsec), authentication, access control

---

## 1.7 History of Computer Networking

| Era | Key Developments |
|-----|------------------|
| **1961-1972** | Packet switching theory (Kleinrock 1961, Baran 1964, Davies); ARPANET (1969, 4 nodes); NCP protocol; first email (Tomlinson 1972) |
| **1972-1980** | TCP/IP (Cerf & Kahn 1974); Ethernet (Metcalfe 1976); ALOHAnet; separation of TCP/IP/UDP |
| **1980-1990** | TCP/IP standardized (1983); DNS (1984); NSFNET backbone (56kbps→1.5Mbps); congestion control (Jacobson 1988) |
| **1990s** | Web (Berners-Lee 1989-91); Mosaic/Netscape; Commercial ISPs; Dot-com boom; 4 killer apps: email, Web, IM, P2P (Napster) |
| **2000s-Present** | Broadband, WiFi, Mobile (3G/4G/5G), Cloud, CDNs, SDN, IoT, QUIC/HTTP/3, generative AI |

**Key Milestones**:
- 1969: First ARPANET packet (UCLA→SRI, "Lo" before crash)
- 1983: TCP/IP flag day (NCP→TCP/IP)
- 1991: NSFNET allows commercial use
- 2011: Wireless devices > wired devices

---

## Key Formulas (Chapter 1)

| Formula | Equation |
|---------|----------|
| Transmission Delay | `d_trans = L / R` |
| Propagation Delay | `d_prop = d / s` |
| Total Nodal Delay | `d_nodal = d_proc + d_queue + d_trans + d_prop` |
| End-to-End (N links, no queue/proc) | `d_end-end = N × (d_trans + d_prop)` |
| Traffic Intensity | `ρ = (L × a) / R` |
| Avg Queuing Delay (M/M/1) | `d_queue = (L/R) × (ρ / (1-ρ))` |
| Store-and-Forward (1 packet, N links) | `d = N × L / R` |
| Store-and-Forward (P packets, N links) | `d = (N + P - 1) × L / R` |
| Bottleneck Throughput | `min(R₁, R₂, ..., R_N)` |
| M flows sharing bottleneck | `R / M` |
| Queuing Delay (general) | `I·L / (R(1-I))` for I < 1 |

---

## Complete Questions, Examples, and MCQs from Slides and Textbook

### Numerical Problems (Exam Practice)

**Q1. One-hop transmission delay**: Given L=8000 bits, R=1 Mbps, calculate d_trans and max packets/sec.
- **Answer**: d_trans = 8 ms, max packets/sec = R/L = 125

**Q2. Queuing delay**: R=1,900,000 bps, L=4700 bits
- a) a=35: I=0.0865 → d_queue=0.23 ms
- b) a=77: I=0.19 → d_queue=0.58 ms
- c) 613 packets arrive, infinite buffer: fill rate = 613 - R/L = 209 pkts/sec
- d) Buffer=627: packets dropped = 613 - (404 + 209) = 0

**Q3. End-to-end delay (3 links)**: L=12000 bits, links: 100Mbps/3km, 1Mbps/5000km, 10Mbps/1km
- Link 1: d_trans=0.12ms, d_prop=0.01ms, total=0.13ms
- Link 2: d_trans=12ms, d_prop=16.67ms, total=28.67ms
- Link 3: d_trans=1.2ms, d_prop=0.003ms, total=1.203ms
- Total = 30ms

**Q4. Throughput bottleneck**: 10 pairs, RS=50, RC=60, R=300 shared
- Per pair = min(50, 60, 300/10) = 30 Mbps
- Bottleneck = R/10
- Server util = 30/50 = 0.6, Client util = 30/60 = 0.5, Shared util = 30/30 = 1.0

**Q5. Store-and-forward timing**: N=3 links, L=12000 bits, R=100 Mbps. How long for 1 packet? For 3 packets back-to-back?
- 1 packet: 3 × 12000/100000000 = 0.36 ms
- 3 packets: (3+3-1) × 12000/100000000 = 0.6 ms

### Review Questions

1. **Difference between packet switching and circuit switching?**
   - Packet: statistical multiplexing, store-and-forward, no reservation, bursty-friendly
   - Circuit: dedicated path, guaranteed bandwidth, connection setup required, FDM/TDM

2. **What are the four delay components?**
   - Processing, Queuing, Transmission, Propagation

3. **When does packet loss occur?**
   - When router buffer is full (queue overflow)

4. **What determines end-to-end throughput?**
   - The bottleneck link (minimum rate along path)

5. **What is the difference between peering and transit?**
   - Peering: mutual, no payment; Transit: customer pays provider

6. **What is encapsulation?**
   - Each layer adds header/trailer to payload from layer above

7. **What is traffic intensity and when does queuing delay blow up?**
   - ρ = La/R; blows up as ρ→1 (multiplier ρ/(1-ρ))

8. **Explain the caravan analogy for transmission vs propagation delay.**
   - Cars=bits, caravan=packet, tollbooth=router. Transmission=pushing caravan through tollbooth. Propagation=driving between tollbooths.

9. **How does traceroute work?**
   - Sends packets with TTL=1,2,3... Router with TTL=0 sends ICMP Time Exceeded. Measures RTT.

10. **What are the 5 layers of the Internet stack?**
    - Physical, Link, Network, Transport, Application

---

## Multiple Choice Questions (from Slides)

**Q1. Shared or private? For each link, decide whether other nodes compete for the same channel.**
- Your laptop's cable to a switch port → **Private (one at each end)**
- The Wi-Fi in this classroom → **Shared (one radio channel)**
- Cable-TV internet, homes sending upstream → **Shared (one cable)**
- Your phone to a cell tower → **Shared (the tower schedules)**

**Q2. An ideal Multiple access protocol desiderata:**
1. When one node wants to transmit, it can send at rate R
2. When M nodes want to transmit, each can send at average rate R/M
3. Fully decentralized: no special node to coordinate, no synchronization of clocks/slots
4. Simple

**Q3. Which statement about Ethernet CSMA/CD is TRUE?**
- a) Collisions detected within long time → False (short time)
- b) Colliding transmissions aborted, reducing channel wastage → **True**
- c) Collision detection easy with wireless → False (easy in wired, difficult in wireless)
- d) After n collisions, NIC chooses K from {0,1,2,..., 2m} → False ({0,1,2,..., 2m-1})

**Q4. Is collision detection still used?**
- Modern switched Ethernet: No (full-duplex, separate channels)
- Wi-Fi: Still shared, collisions happen

---

## Textbook End-of-Chapter Problems (Chapter 1)

**P1.** Compare packet switching and circuit switching for bursty traffic.
**P2.** Calculate end-to-end delay for a 3-hop path with given link rates and distances.
**P3.** Explain queuing delay formula and behavior as ρ→1.
**P4.** Describe the 5-layer Internet model and how it differs from OSI 7-layer.
**P5.** What is the difference between FDM and TDM in circuit switching?
**P6.** Explain statistical multiplexing with a numerical example.
**P7.** Describe the network of networks structure with Tier-1, Tier-2, Tier-3 ISPs.
**P8.** How does traceroute use ICMP to measure RTT?
**P9.** What are the four types of network attacks discussed?
**P10.** Trace the history of Internet from ARPANET to present.

---



---

# Unit 1: Application Layer (Chapter 2)

## 2.1 Principles of Network Applications

### 2.1.1 Network Application Architectures
Two main paradigms:

| Architecture | Description | Examples |
|--------------|-------------|----------|
| **Client-Server** | Always-on server (fixed IP) serves clients; clients don't communicate directly; often data centers for scaling | Web, Email, DNS, Video Streaming |
| **Peer-to-Peer (P2P)** | No always-on server; peers act as both clients and servers; self-scaling (new peers bring capacity + demand) | BitTorrent, Bitcoin, Skype (original) |

**Hybrid**: Many modern apps use both (e.g., P2P for content, centralized for discovery/auth).

**Key Insight**: Application architecture ≠ Network architecture. Network architecture (5-layer stack) is fixed; application architecture is chosen by developer.

### 2.1.2 Processes Communicating
- **Process**: Program running within a host (not the program itself, but its execution instance)
- **Client process**: Initiates communication
- **Server process**: Waits to be contacted
- **Inter-process communication**: Same host (OS-defined); Different hosts (exchange messages over network)

### 2.1.3 Sockets
- **Socket**: Interface between application process and transport-layer protocol
- **Analogy**: Process = house, Socket = door
- **Sending process** shoves message out its door (socket)
- **Transport infrastructure** on other side delivers to receiving process's door
- **Application developer controls**: Application-layer side of socket
- **OS controls**: Transport-layer side of socket
- **Developer choices**: (1) Transport protocol (TCP/UDP), (2) Few parameters (buffer sizes, MSS)

### 2.1.4 Addressing Processes
To receive messages, process needs identifier:
- **Host identifier**: 32-bit IP address
- **Process identifier**: **Port number** (16-bit)
- **Example**: Web server: IP + port 80; Mail server: IP + port 25

### 2.1.5 Transport Services Available to Applications
Four dimensions:

| Service | Description |
|---------|-------------|
| **Reliable Data Transfer** | Guaranteed delivery without errors, in order (TCP) vs loss-tolerant (UDP) |
| **Throughput** | Guaranteed minimum rate (not provided by Internet) vs elastic (use whatever) |
| **Timing** | Guaranteed max delay (not provided) vs best-effort |
| **Security** | Encryption, integrity, authentication (TLS enhances TCP) |

**Services NOT provided by Internet transport protocols**: Throughput guarantees, Timing guarantees

### 2.1.6 Transport Services Provided by the Internet

| Feature | TCP | UDP |
|---------|-----|-----|
| **Connection** | Connection-oriented (3-way handshake) | Connectionless |
| **Reliability** | Reliable, in-order byte stream | Unreliable, may arrive out of order |
| **Flow Control** | Yes (receiver buffer) | No |
| **Congestion Control** | Yes (throttles sender) | No |
| **Security** | Via TLS (application layer) | Via DTLS |
| **Header Overhead** | 20+ bytes | 8 bytes |

**Application Protocol Mapping**:
- TCP: HTTP, SMTP, FTP, SSH, IMAP
- UDP: DNS, RTP, DHCP, SIP, QUIC
- Either: Video conferencing (UDP preferred, TCP fallback for firewalls)

### 2.1.7 Application-Layer Protocols
Define:
- Message types (request/response)
- Message syntax (fields, delineation)
- Field semantics (meaning)
- Rules for when/how to send/respond

**Open protocols** (RFCs): HTTP, SMTP, DNS - interoperability
**Proprietary protocols**: Zoom, Skype (original)

---

## 2.2 The Web and HTTP

### 2.2.1 Overview of HTTP
- **HTTP**: HyperText Transfer Protocol (RFC 1945, 7230, 7540, 9114)
- **Client**: Browser (requests, receives, displays objects)
- **Server**: Web server (sends objects in response)
- **Objects**: HTML, JPEG, JavaScript, CSS, video - each addressable by URL
- **Web page**: Base HTML + referenced objects (e.g., HTML + 5 images = 6 objects)
- **URL format**: `http://hostname/path` (hostname + path name)
- **Stateless**: Server maintains no client state between requests

### 2.2.2 Non-Persistent vs Persistent Connections

| Connection Type | Description | RTTs for K objects |
|-----------------|-------------|-------------------|
| **Non-persistent (HTTP/1.0)** | New TCP connection per object | K × 2 RTTs |
| **Persistent (HTTP/1.1)** | Single TCP connection for multiple objects | 2 RTT + K×trans |
| **Pipelined Persistent** | Send requests back-to-back without waiting | 2 RTT + K×trans |

**HTTP/1.0**: Default non-persistent (can use `Connection: keep-alive`)
**HTTP/1.1**: Default persistent, supports pipelining (rarely used due to HOL blocking)

**Numerical Example**: 1 HTML + 6 images, RTT=80ms, transmission negligible
- Non-persistent: 7 × 2 × 80 = 1120 ms
- Persistent (no pipelining): 1 (TCP) + 7 (req/resp) = 8 RTT = 640 ms
- Persistent (pipelining): 1 (TCP) + 1 (HTML) + 1 (all images) = 3 RTT = 240 ms

### 2.2.3 HTTP Message Format

**Request Message**:
```
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/5.0
Accept-language: fr

[empty line]
[entity body - empty for GET, form data for POST]
```

**Components**:
- **Request line**: Method (GET, POST, HEAD, PUT, DELETE), URL, HTTP version
- **Header lines**: Host, Connection, User-agent, Accept-language, etc.
- **Entity body**: For POST (form data), PUT (file upload)

**Response Message**:
```
HTTP/1.1 200 OK
Connection: close
Date: Mon, 21 Oct 2024 18:58:21 GMT
Server: Apache/2.2.3
Last-Modified: Sun, 20 Oct 2024 13:20:46 GMT
Content-Length: 6821
Content-Type: text/html

<html>...</html>
```

**Components**:
- **Status line**: Version, status code, phrase
- **Header lines**: Date, Server, Last-Modified, Content-Length, Content-Type
- **Entity body**: Requested object

**Common Methods**: GET (retrieve), POST (submit form), HEAD (headers only), PUT (upload), DELETE (remove)

**Common Status Codes**:
- 200 OK, 301 Moved Permanently, 304 Not Modified
- 400 Bad Request, 404 Not Found
- 505 HTTP Version Not Supported

### 2.2.4 User-Server Interaction: Cookies
**Problem**: HTTP is stateless; servers need to identify users across requests
**Solution**: **Cookies** (RFC 6265)

**Four Components**:
1. **Set-cookie header** in HTTP response
2. **Cookie header** in subsequent HTTP requests
3. **Cookie file** on user's host (managed by browser)
4. **Back-end database** at Web site

**How it works**:
1. User visits site first time → Server creates unique ID, stores in database
2. Server responds with `Set-cookie: 1678`
3. Browser stores `hostname, 1678` in cookie file
4. Subsequent requests include `Cookie: 1678`
5. Server tracks user activity, enables shopping cart, recommendations

**Privacy**: Third-party cookies (ad networks) track across sites; restricted by modern browsers

### 2.2.5 Browser Caching
**Goal**: Reduce latency, bandwidth, server load
**Mechanism**:
- Server sends `Cache-Control: max-age=3600` or `Expires`
- Browser caches response
- **Conditional GET**: If stale, send `If-Modified-Since: <date>`
- Server responds **304 Not Modified** (no object) if unchanged
- **304 saves bandwidth and response time**

**Cache-Control directives**: `no-store`, `max-age`, `must-revalidate`, etc.

### 2.2.6 HTTP/2 (RFC 7540)
**Goals**: Reduce latency, eliminate HOL blocking, header compression
**Key Features**:
1. **Binary framing** (not text) - efficient parsing
2. **Multiplexing** - multiple streams over single TCP connection
3. **Header compression (HPACK)** - reduces overhead
4. **Server push** - send resources proactively
5. **Stream prioritization** - critical resources first

**HOL Blocking Problem in HTTP/1.1**: Single TCP connection → large object blocks small ones behind it
**HTTP/2 Solution**: Frame interleaving - break messages into frames, interleave on same connection

**Example**: Video (1000 frames) + 8 small objects (2 frames each)
- With interleaving: Small objects sent after 18 frames
- Without: Small objects wait for 1016 frames

**Limitation**: HOL blocking still at TCP level (lost packet blocks all streams)

### 2.2.7 HTTP/3 and QUIC (RFC 9114, RFC 9000)
**QUIC**: Quick UDP Internet Connections
- Runs over **UDP** (not TCP)
- Implements reliability, congestion control, TLS 1.3 **in user space**
- **0-RTT resumption** for repeat connections
- **Connection migration** - survives IP change (mobile handoff)
- **Per-stream flow control** - no HOL blocking across streams

**HTTP/3** = HTTP semantics over QUIC

**Handshake Comparison**:
- TCP + TLS 1.2: 2 RTT
- TCP + TLS 1.3: 1 RTT
- QUIC + TLS 1.3: 1 RTT
- QUIC 0-RTT: 0 RTT (resumption)

---

## 2.3 Electronic Mail in the Internet

### 2.3.1 SMTP (Simple Mail Transfer Protocol)
- **Port 25** (server-to-server), **Port 587** (client submission with TLS)
- **Push protocol**: Sender pushes to receiver
- **Text-based** commands: HELO, MAIL FROM, RCPT TO, DATA, QUIT
- **Reliable**: Uses TCP
- **7-bit ASCII** only (requires MIME for binary/attachments)

**Flow**: 
```
Client → MTA → ... → MTA → Recipient's Mail Server
```

### 2.3.2 Mail Message Formats
**RFC 5322** (message format):
```
From: sender@example.com
To: recipient@example.com
Subject: Hello
Date: Mon, 03 Nov 2026 12:00:00 GMT
Message-ID: <unique@id>

Body text here...
```

**MIME** (Multipurpose Internet Mail Extensions) - RFC 2045:
- `Content-Type`: text/plain, text/html, multipart/mixed, image/jpeg, etc.
- `Content-Transfer-Encoding`: base64, quoted-printable, 7bit
- Enables attachments, non-ASCII, multipart messages

### 2.3.3 Mail Access Protocols
| Protocol | Port | Description |
|----------|------|-------------|
| **POP3** | 110 (995 TLS) | Download and delete; simple, offline access |
| **IMAP** | 143 (993 TLS) | Remote folder management; sync across devices; server-side search |
| **HTTP** | 80/443 | Webmail (Gmail, Outlook.com) - uses web API |

**SMTP** = sending mail; **POP3/IMAP** = reading mail

---

## 2.4 DNS — The Internet's Directory Service

### 2.4.1 Services Provided by DNS
1. **Hostname to IP translation** (primary)
2. **Host aliasing** (CNAME records)
3. **Mail server aliasing** (MX records)
4. **Load distribution** (multiple A records for same name)
5. **Service discovery** (SRV records)

### 2.4.2 Overview of How DNS Works
**Hierarchical, distributed database**:
```
Root (.) → TLD (.com, .org, .edu) → Authoritative (example.com)
```

**DNS Servers**:
1. **Root servers** (13 logical, hundreds physical): Know TLD servers
2. **TLD servers**: Know authoritative servers for domains
3. **Authoritative servers**: Know actual records for domain
4. **Local/Recursive resolvers**: ISP/company DNS; perform recursive queries

**Query Types**:
- **Recursive**: Resolver does all work, returns final answer
- **Iterative**: Resolver asks root → TLD → authoritative step by step

**Caching**: All responses cached (TTL typically 2 days = 172,800 sec)

**Messages for 3-level lookup**: 8 messages (4 queries + 4 replies)

### 2.4.3 DNS Records and Messages

**Resource Record Format**: `(Name, Value, Type, TTL)`

| Type | Name | Value | Purpose |
|------|------|-------|---------|
| **A** | hostname | IPv4 address | Name → IPv4 |
| **AAAA** | hostname | IPv6 address | Name → IPv6 |
| **CNAME** | alias | canonical name | Alias → real name |
| **MX** | domain | mail server hostname | Mail routing |
| **NS** | domain | authoritative NS | Delegation |
| **TXT** | domain | arbitrary text | SPF, DKIM, verification |
| **SRV** | service | host:port | Service discovery |

**DNS Message Format**:
```
Header (12 bytes): ID, flags, QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT
Question Section: QNAME, QTYPE, QCLASS
Answer Section: RRs
Authority Section: RRs
Additional Section: RRs
```

**Flags**: QR (0=query, 1=response), Opcode, AA (authoritative), TC (truncated), RD (recursion desired), RA (recursion available), RCODE

### 2.4.4 DNS Security
- **DNSSEC**: Cryptographic signatures on records (RRSIG, DNSKEY, DS)
- **DoH/DoT**: DNS over HTTPS/TLS for privacy
- **Attacks**: Cache poisoning, DDoS on root/TLD, hijacking

---

## 2.5 Video Streaming and Content Distribution Networks

### 2.5.1 Internet Video
**Characteristics**: High bandwidth, delay-tolerant (buffering), loss-tolerant
**Types**:
- **Stored video**: YouTube, Netflix (pre-recorded)
- **Live streaming**: Twitch, sports (real-time encoding)
- **Interactive video**: Zoom, FaceTime (low latency critical)

### 2.5.2 HTTP Streaming and DASH
**Problem**: Traditional streaming (RTSP/RTP) doesn't traverse firewalls well
**Solution**: **DASH** (Dynamic Adaptive Streaming over HTTP)
- Video encoded at multiple bitrates/qualities
- **MPD** (Media Presentation Description): XML manifest listing segments
- Client adapts quality based on measured bandwidth
- Segments fetched via standard HTTP GET

**Quality adaptation algorithms**: Buffer-based, throughput-based, hybrid

### 2.5.3 Content Distribution Networks (CDNs)
**Problem**: Single server far from users → high latency, low throughput
**CDN Solution**: Deploy server clusters (PoPs) globally

**CDN Operations**:
1. **Request routing**: DNS redirects to nearest PoP (GeoDNS, anycast)
2. **Content placement**: Popular content cached at edge
3. **Content delivery**: Serve from cache or fetch from origin

**Types**:
- **Private CDNs**: Netflix Open Connect, Google Global Cache
- **Third-party CDNs**: Akamai, Cloudflare, Fastly, CloudFront

**Benefits**: Lower latency, higher throughput, reduced origin load, DDoS absorption

**Netflix Case Study**: 
- Open Connect Appliances deployed at ISPs
- Pre-positions content based on viewing predictions
- ~15% of global Internet traffic

---

## 2.6 Socket Programming

### 2.6.1 Socket Programming with UDP
**UDP Socket API** (Python):
```python
# Server
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', port))
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    serverSocket.sendto(modifiedMessage, clientAddress)

# Client
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
```

**Key points**:
- `sendto()`/`recvfrom()` include destination address
- No connection setup
- Unreliable, unordered

### 2.6.2 Socket Programming with TCP
**TCP Socket API** (Python):
```python
# Server
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', port))
serverSocket.listen(1)
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024)
    connectionSocket.send(modifiedMessage)
    connectionSocket.close()

# Client
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send(message)
modifiedMessage = clientSocket.recv(1024)
clientSocket.close()
```

**Key points**:
- `accept()` creates **new connection socket** per client
- Welcoming socket (listens) vs connection socket (data transfer)
- Reliable, ordered byte stream
- `send()`/`recv()` don't need address (connection-oriented)

### 2.6.3 Socket Programming with QUIC
- Uses libraries like `aioquic` (Python)
- Similar to TCP but with streams, 0-RTT, connection migration
- Application handles TLS certificates

---

## Key Formulas (Chapter 2)

| Scenario | Total Time |
|----------|------------|
| Non-persistent (K objects) | `K × (2×RTT + L/R)` |
| Non-persistent (P parallel) | `ceil(K/P) × (2×RTT + L/R)` |
| Persistent (no pipelining) | `2×RTT + K×L/R` |
| Persistent + Pipelining | `2×RTT + K×L/R` (requests back-to-back) |
| HTTP/2 / HTTP/3 | `RTT_handshake + RTT_req/resp + L/R` |

**DNS**: 3-level lookup = 8 messages (4 queries + 4 replies)
**TTL**: Typically 2 days = 172,800 seconds

---

## Complete Questions, Examples, and MCQs from Slides and Textbook

### Numerical Problems (Exam Practice)

**Q1. HTTP Performance Calculation**: 
A web page consists of a base HTML (100 KB) + 5 embedded images (200 KB each). RTT = 80 ms. Transmission rates: server link = 100 Mbps, client link = 50 Mbps. Calculate total time for:
- a) Non-persistent HTTP
- b) Persistent HTTP (no pipelining)
- c) Persistent HTTP (pipelining)

**Answer**: 
- a) 6 objects × (2 × 80 + 300KB/50Mbps) = 6 × (160 + 48) = 1248 ms
- b) 2×80 + 6×(300KB/50Mbps) = 160 + 288 = 448 ms
- c) 80 + 300KB/50Mbps + 80 + 5×300KB/50Mbps ≈ 240 ms

**Q2. DNS Query Calculation**:
For a 3-level DNS lookup (root → TLD → authoritative), how many messages are exchanged?
- **Answer**: 8 messages (4 queries + 4 replies)

**Q3. DNS Caching**: TTL = 2 days. How many seconds?
- **Answer**: 172,800 seconds

### Review Questions

1. **Client-server vs P2P?**
   - Client-server: dedicated always-on server
   - P2P: peers act as both client/server, self-scaling

2. **What is a socket?**
   - API between application and transport layer; identified by (IP, port)

3. **TCP vs UDP services?**
   - TCP: reliable, ordered, flow/congestion control, connection-oriented
   - UDP: unreliable, unordered, no flow/congestion control, connectionless

4. **Non-persistent vs persistent HTTP?**
   - Non-persistent: new TCP per object (2 RTT each)
   - Persistent: single TCP for multiple objects

5. **How do cookies work?**
   - Server sets cookie via Set-Cookie header
   - Browser sends cookie in future requests to same domain

6. **What is DNS and how does it work?**
   - Hierarchical distributed database mapping names to IPs
   - Recursive/iterative queries; caching with TTL

7. **What is DASH?**
   - HTTP-based adaptive streaming; client selects quality based on bandwidth

8. **What is a CDN?**
   - Geographically distributed servers caching content near users

9. **UDP vs TCP socket programming?**
   - UDP: sendto/recvfrom with address; no connection
   - TCP: connect/accept; send/recv without address; welcoming + connection sockets

10. **HTTP/2 vs HTTP/3?**
    - HTTP/2: TCP, multiplexing, but HOL blocking at TCP level
    - HTTP/3: QUIC over UDP, 0-RTT, connection migration, per-stream control

---

## Multiple Choice Questions (from Slides)

**Q1. Application architecture vs Network architecture:**
- Application architecture: chosen by developer (client-server, P2P)
- Network architecture: fixed (5-layer stack)

**Q2. A process sends messages into, and receives messages from, the network through a software interface called:**
- a) port
- b) **socket**
- c) pipe
- d) channel

**Q3. The socket is the interface between:**
- a) Application layer and network layer
- b) Transport layer and network layer
- c) **Application layer and transport layer**
- d) Physical layer and link layer

**Q4. To identify the receiving process, two pieces of information need to be specified:**
- (1) the address of the host (IP)
- (2) an identifier that specifies the receiving process (port number)

**Q5. Which of the following is NOT a service provided by Internet transport protocols?**
- a) Reliable data transfer
- b) **Throughput guarantees**
- c) Timing guarantees
- d) Security (via TLS)

**Q6. TCP services include:**
- a) Connection-oriented service (handshaking)
- b) Reliable data transfer service
- c) Congestion control (for Internet welfare)
- d) **All of the above**

**Q7. UDP provides:**
- a) Connection-oriented service
- b) Reliable data transfer
- c) **Connectionless, unreliable data transfer**
- d) Congestion control

**Q7. HTTP is stateless. How does server maintain user state?**
- a) Session IDs in URLs
- b) **Cookies** (Set-Cookie / Cookie headers)
- c) Hidden form fields
- d) IP address tracking

**Q8. HTTP/1.1 default connection type:**
- a) Non-persistent
- b) **Persistent**
- c) Pipelined
- d) Parallel

**Q9. HTTP/2 multiplexing solves which problem?**
- a) **Head-of-line blocking**
- b) Slow start
- c) Three-way handshake
- d) DNS lookup

**Q10. HTTP/3 runs over:**
- a) TCP
- b) **UDP (QUIC)**
- c) SCTP
- d) IP directly

**Q11. SMTP is a:**
- a) Pull protocol
- b) **Push protocol**
- c) Peer-to-peer protocol
- d) Connectionless protocol

**Q12. Which port does SMTP use for server-to-server?**
- a) 587
- b) **25**
- c) 110
- d) 143

**Q13. DNS query types:**
- Recursive: Resolver does all work
- Iterative: Resolver asks root → TLD → authoritative step by step

**Q14. For 3-level DNS lookup, total messages = ?**
- a) 4
- b) 6
- c) **8**
- d) 12

**Q15. CDN benefits:**
- Lower latency, higher throughput, reduced origin load, DDoS absorption

**Q16. Socket programming - UDP vs TCP:**
- UDP: `sendto()`/`recvfrom()` with address; no connection
- TCP: `connect()`/`accept()`; `send()`/`recv()` without address

---

## Textbook End-of-Chapter Problems (Chapter 2)

**P1.** Compare client-server and P2P architectures for a video streaming application.
**P2.** Write a simple UDP client-server in Python that echoes messages.
**P3.** Calculate total HTTP response time for a page with K objects under non-persistent, persistent, and pipelined connections.
**P4.** Explain how cookies work with a diagram showing request/response headers.
**P5.** Describe the DNS resolution process for www.example.com with a diagram.
**P6.** What are the differences between POP3, IMAP, and HTTP for email access?
**P7.** Explain DASH adaptive streaming and how it differs from traditional RTSP/RTP streaming.
**P8.** Describe CDN operation: request routing, content placement, content delivery.
**P9.** Write a TCP client-server in Python for a simple file transfer application.
**P10.** Compare HTTP/1.1, HTTP/2, and HTTP/3 in terms of handshake, multiplexing, and HOL blocking.

---

## Key Formulas (Units 1 & 2)

| Formula | Equation |
|---------|----------|
| Transmission Delay | `d_trans = L / R` |
| Propagation Delay | `d_prop = d / s` |
| Total Nodal Delay | `d_nodal = d_proc + d_queue + d_trans + d_prop` |
| End-to-End (N links, no queue/proc) | `d_end-end = N × (d_trans + d_prop)` |
| Traffic Intensity | `ρ = (L × a) / R` |
| Avg Queuing Delay (M/M/1) | `d_queue = (L/R) × (ρ / (1-ρ))` |
| Store-and-Forward (1 packet, N links) | `d = N × L / R` |
| Store-and-Forward (P packets, N links) | `d = (N + P - 1) × L / R` |
| Bottleneck Throughput | `min(R₁, R₂, ..., R_N)` |
| M flows sharing bottleneck | `R / M` |

### HTTP Performance
| Scenario | Total Time |
|----------|------------|
| Non-persistent (K objects) | `K × (2×RTT + L/R)` |
| Non-persistent (P parallel) | `ceil(K/P) × (2×RTT + L/R)` |
| Persistent (no pipelining) | `2×RTT + K×L/R` |
| Persistent + Pipelining | `2×RTT + K×L/R` |
| HTTP/2 / HTTP/3 | `RTT_handshake + RTT_req/resp + L/R` |

**DNS**: 3-level lookup = 8 messages (4 queries + 4 replies)
**TTL**: Typically 2 days = 172,800 seconds

---

## Review Questions

1. **Difference between packet switching and circuit switching?**
   - Packet: statistical multiplexing, store-and-forward, no reservation
   - Circuit: dedicated path, guaranteed bandwidth, connection setup required

2. **What are the four delay components?**
   - Processing, Queuing, Transmission, Propagation

3. **When does packet loss occur?**
   - When router buffer is full (queue overflow)

4. **What determines end-to-end throughput?**
   - The bottleneck link (minimum rate along path)

5. **What is the difference between peering and transit?**
   - Peering: mutual, no payment; Transit: customer pays provider

6. **What is encapsulation?**
   - Each layer adds header/trailer to payload from layer above

7. **Client-server vs P2P?**
   - Client-server: dedicated always-on server
   - P2P: peers act as both client/server, self-scaling

8. **What is a socket?**
   - API between application and transport layer; identified by (IP, port)

9. **TCP vs UDP services?**
   - TCP: reliable, ordered, flow/congestion control, connection-oriented
   - UDP: unreliable, unordered, no flow/congestion control, connectionless

10. **Non-persistent vs persistent HTTP?**
    - Non-persistent: new TCP per object (2 RTT each)
    - Persistent: single TCP for multiple objects

11. **How do cookies work?**
    - Server sets cookie via Set-Cookie header
    - Browser sends cookie in future requests to same domain

12. **What is DNS and how does it work?**
    - Hierarchical distributed database mapping names to IPs
    - Recursive/iterative queries; caching with TTL

13. **What is DASH?**
    - HTTP-based adaptive streaming; client selects quality based on bandwidth

14. **What is a CDN?**
    - Geographically distributed servers caching content near users

15. **UDP vs TCP socket programming?**
    - UDP: sendto/recvfrom with address; no connection
    - TCP: connect/accept; send/recv without address; welcoming + connection sockets

---

# Extra Problems (from Course Materials)

## Delay Problems

### Q1: Transmission Delay
**Problem**: Packet length = 4000 bits, link rate = 10 MBps. What is the transmission delay?
- L = 4000 bits
- R = 10 MBps = 10 × 8 × 10⁶ bps = 80 Mbps
- **Answer**: Transmission Delay = L/R = 4000 / (10 × 8 × 10⁶) = 0.00005s = **50 microseconds**

### Q2: Dedicated Link vs Courier
**Problem**: Send 10 TB from Bengaluru to Chennai. Dedicated link: 100 Mbps. Courier: 1 day delivery.
- 10 TB = 10 × 10¹² × 8 bits = 8×10¹³ bits
- Link time: 8×10¹³ / (100 × 10⁶) = 800,000 seconds ≈ **9.26 days**
- Courier: **1 day**
- **Answer**: Courier is faster

### Q3: Optical Fiber Distance
**Problem**: Optical fiber at 70% speed of light, propagation time = 10 μs. What distance?
- Speed = 0.7 × 3×10⁸ = 2.1×10⁸ m/s
- Distance = Speed × Time = 2.1×10⁸ × 10×10⁻⁶ = **2100 m = 2.1 km**

### Q4: Transmission vs Propagation Delay Ratio
**Problem**: Propagation delay = 1000 × transmission delay. Total delay = 3 μs, distance = 2 km.
- Total = d_trans + d_prop = d_trans + 1000×d_trans = 1001×d_trans = 3 μs
- **Answer**: d_trans ≈ **3 ns**

### Q5: Processing Delay Calculation
**Problem**: One-hop d_trans = 0.003 ms, d_queue = 1 μs, distance = 3 km, total nodal delay = 0.04 ms. Find d_proc.
- d_nodal = d_proc + d_queue + d_trans + d_prop
- d_prop = 3000 / (3×10⁸) = 0.01 ms
- 0.04 = d_proc + 0.001 + 0.003 + 0.01
- **Answer**: d_proc = **0.026 ms**

---

## Throughput Problems

### Q6: Actual Throughput with Efficiency
**Problem**: Link bandwidth = 15 Mbps each direction, efficiency = 80%.
- Ideal = min(15, 15) = 15 Mbps
- **Answer**: Actual = 0.8 × 15 = **12 Mbps**

### Q7: Circuit Switching Throughput
**Problem**: 10 Mbps link, 7 users, circuit switching.
- **Answer**: Per user = 10/7 ≈ **1.43 Mbps**

### Q8: Transmission Delay
**Problem**: 20 Mbps link, 1000-bit packet. What is transmission delay?
- **Answer**: 1000 / (20×10⁶) = **50 μs**

### Q9: Propagation & Transmission Delay Formulas
**Problem**: Hosts A, B separated by m meters, link rate R bps, packet size L bits, prop speed s m/s.
- d_prop = m/s
- d_trans = L/R
- End-to-end = d_trans + d_prop
- At t = d_trans: last bit just leaving A
- If d_prop > d_trans: first bit in link; if d_prop < d_trans: first bit arrived at B
- For d_prop = d_trans: m = s × (L/R)
- Example: s=2.5×10⁸, L=1500 bytes, R=10 Mbps → m = **300 km**

### Q10: Bandwidth-Delay Product
**Problem**: 20,000 km, R=5 Mbps, s=2.5×10⁸ m/s.
- d_prop = 2×10⁷ / 2.5×10⁸ = 0.08 s
- R×d_prop = (5×10⁶)×0.08 = **400,000 bits**
- File = 800,000 bits > BDP → max bits in link = **400,000 bits**
- Bit width = s/R = 2.5×10⁸/5×10⁶ = **50 meters** (half football field)
- For R=1 Gbps: BDP = 80,000,000 bits, bit width = **0.25 meters**

### Q11: ISP Delay Promise
**Problem**: 10 Mbps, 10,000 km, 100 KB/s data, promised < 5 ms delay.
- d_prop = 10⁷/2.5×10⁸ = 40 ms
- d_trans = (100×1000×8)/10⁷ = 80 ms
- Total = **120 ms** > 5 ms
- **Answer**: **Cannot deliver on promise**

### Q12: Transmission Speed for Packet Timing
**Problem**: 5000 km, 2 packets of 4 MB, queue delay = 10 ms, s=2.5×10⁸. Find R so 2nd packet finishes when 1st arrives.
- d_prop = 20 ms
- 1st packet arrival = 10 + d_trans + 20 = 30 + d_trans
- 2nd packet finish = 10 + 2×d_trans
- Set equal: 10 + 2d_trans = 30 + d_trans → d_trans = 20 ms
- R = L/d_trans = (4×10⁶×8)/0.02 = **1.6 Gbps**

### Q13: 100 TB Transfer - Network vs Driving
**Problem**: 100 TB, 350 km, 1 Gbps, s=2×10⁸, drive time = 7 hrs one way.
- d_trans = 8×10¹³/10⁹ = 8×10⁴ sec = **222 hours (9.25 days)**
- d_prop = 3.5×10⁵/2×10⁸ = 1.75 ms (negligible)
- Drive round trip = 14 hours
- **Answer**: **Driving is faster**; d_trans is dominant (99.99% of total)

### Q14: Lossy vs Lossless Channel
**Problem**: 100 packets × 16 MB. Path 1: lossless 10 Gbps. Path 2: 50% loss, 20 Gbps. Queue = 10 ms/packet.
- Lossless: d_trans = 128/10000 = 12.8 ms → total = 22.8 ms/packet → 100 × 22.8 = **2.28 sec**
- Lossy (50% loss): 2 transmissions/packet → 200 transmissions × (10+6.4) = **3.28 sec**
- **Answer**: **Use lossless 10 Gbps channel**
