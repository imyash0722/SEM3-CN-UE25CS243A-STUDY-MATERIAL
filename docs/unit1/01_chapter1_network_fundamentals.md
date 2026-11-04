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