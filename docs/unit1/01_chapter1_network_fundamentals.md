# Unit 1: Computer Networks and the Internet (Chapter 1)

## 1.1 What Is the Internet?

### A Nuts-and-Bolts Description
The Internet is a **global network of networks** - a complex infrastructure consisting of:
- **End systems (hosts)**: Computers, smartphones, servers, IoT devices
- **Communication links**: Fiber optics, copper wire, coaxial cable, radio spectrum, satellite links
- **Packet switches**: Routers and link-layer switches that forward packets
- **Protocols**: TCP, IP, HTTP, DNS, etc. that control communication

**Key concept**: The Internet provides a **service model** to applications - a set of operations (send/receive) and expected behavior (reliability, timing, etc.)

### A Services Description
The Internet provides two key services to applications:
1. **Connectionless service (UDP)**: Unreliable, no handshake, minimal overhead
2. **Connection-oriented service (TCP)**: Reliable, in-order byte stream with flow/congestion control

Applications access these services via **sockets** - the API between application and transport layer.

### What Is a Protocol?
A **protocol** defines the format, order, and actions taken on transmission/receipt of messages among communicating entities.
- **Syntax**: Message format, data representation
- **Semantics**: Meaning of fields, actions to take
- **Timing**: When to send, how fast, timeouts

**Example**: HTTP defines how a client requests a web page and how a server responds.

---

## 1.2 The Network Edge

### 1.2.1 Access Networks
Access networks connect end systems to the first router (edge router). Types:

| Access Network | Technology | Typical Speed | Characteristics |
|----------------|------------|---------------|-----------------|
| **DSL** | Digital Subscriber Line | ~24 Mbps downstream | Uses existing telephone lines; dedicated per household |
| **Cable** | HFC (Hybrid Fiber-Coax) | ~1-2 Gbps downstream | Shared broadcast medium; uses DOCSIS |
| **FTTH** | Fiber to the Home | ~1-10 Gbps | Dedicated fiber; highest speeds |
| **5G/Fixed Wireless** | Cellular | ~100 Mbps - 1 Gbps | Mobile/wireless; shared spectrum |
| **Enterprise (Ethernet/WiFi)** | 802.3/802.11 | ~1-100 Gbps | Wired/wireless LAN in organizations |

**Key distinction**: 
- **Dedicated access** (DSL, FTTH): Bandwidth not shared
- **Shared access** (Cable, WiFi, 5G): Bandwidth shared among users

### 1.2.2 Physical Media
| Medium | Type | Characteristics |
|--------|------|-----------------|
| **Twisted Pair (Cat 5e/6/6a/7)** | Copper | 100m max; 1-10 Gbps; susceptible to interference |
| **Coaxial Cable** | Copper | Longer distances; used in cable TV/HFC |
| **Fiber Optics (SMF/MMF)** | Glass | Km distances; 10-100+ Gbps; immune to EMI |
| **Radio Spectrum** | Wireless | WiFi, 4G/5G, satellite; shared medium; variable propagation |

---

## 1.3 The Network Core

### 1.3.1 Packet Switching
The Internet uses **packet switching** (not circuit switching):
- Messages broken into **packets** (typically 1-1500 bytes)
- Each packet routed independently through network
- **Store-and-forward**: Each switch receives entire packet before forwarding to next link
- **Statistical multiplexing**: Links shared on demand; no reservation

**Advantages over Circuit Switching**:
- Efficient for bursty data traffic
- No connection setup delay
- Better resource utilization
- Robust (packets can take different paths)

### 1.3.2 Circuit Switching (for comparison)
- Dedicated end-to-end path reserved for duration of connection
- Constant bandwidth guaranteed
- Used in traditional telephone networks
- Inefficient for bursty traffic (resources idle during silence)

### 1.3.3 A Network of Networks
The Internet = **Interconnected ISPs**:
1. **Tier-1 ISPs**: Global reach, peer with each other (no transit fees)
2. **Tier-2 ISPs**: Regional, buy transit from Tier-1
3. **Tier-3/Access ISPs**: Local, connect end users
4. **Content Providers (CDNs)**: Google, Netflix, Akamai - deploy servers close to users
5. **IXPs (Internet Exchange Points)**: Physical locations where ISPs peer

**Peering vs Transit**:
- **Peering**: Mutual agreement, no payment (typically Tier-1 to Tier-1)
- **Transit**: Customer pays provider for global connectivity

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

### 1.4.2 Queuing Delay and Packet Loss
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

**Packet Loss**: Occurs when buffer is full. Lost packets may be retransmitted (TCP) or lost forever (UDP).

### 1.4.3 End-to-End Delay
For N links (no queuing/processing):
```
d_end-end = N × (d_trans + d_prop)
```

General case:
```
d_end-end = Σ(d_proc_i + d_queue_i + d_trans_i + d_prop_i)
```

### 1.4.4 Throughput in Computer Networks
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

### 1.5.2 Encapsulation
Each layer adds its own **header** (and sometimes trailer):
```
Application Message
    → Transport Header + Message = Segment (TCP) / Datagram (UDP)
        → IP Header + Segment = Datagram
            → Link Header + Datagram + Link Trailer = Frame
                → Physical layer transmits bits
```

At receiver: **Decapsulation** - each layer strips its header and passes payload up.

---

## 1.6 Networks Under Attack
Types of attacks:
1. **Malware**: Viruses, worms, botnets, ransomware
2. **DoS/DDoS**: Overwhelm target with traffic
3. **Sniffing/Eavesdropping**: Passive interception
4. **Spoofing**: Fake source IP/email
5. **Man-in-the-Middle**: Intercept and modify
6. **DNS Attacks**: Cache poisoning, hijacking

**Defense**: Firewalls, IDS/IPS, encryption (TLS/IPsec), authentication, access control

---

## 1.7 History of Computer Networking

| Era | Key Developments |
|-----|------------------|
| **1961-1972** | Packet switching theory (Kleinrock, Baran, Davies); ARPANET (1969); NCP protocol |
| **1972-1980** | Email (Tomlinson); TCP/IP (Cerf & Kahn, 1974); Ethernet (Metcalfe, 1976) |
| **1980-1990** | TCP/IP standardized (1983); DNS (1984); NSFNET backbone; Routing protocols (RIP, OSPF, BGP) |
| **1990s** | Web (Berners-Lee, 1990); Mosaic browser; Commercial ISPs; Dot-com boom |
| **2000s-Present** | Broadband, WiFi, Mobile (3G/4G/5G), Cloud, CDNs, SDN, IoT, QUIC/HTTP/3 |

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