# Unit 4: Link Layer and LAN (Chapter 6)

## Overview
This unit covers Chapter 6 of Kurose & Ross (9th Edition): The Link Layer and LANs

**Course Hours**: 14 hours

---

## 6.1 Introduction to Link Layer

### Terminology
- **Nodes**: Hosts, routers, switches, WiFi access points
- **Links**: Communication channels connecting adjacent nodes
  - Wired (copper, fiber)
  - Wireless (radio)
- **Frame**: Layer-2 packet, encapsulates datagram

### Link Layer Responsibility
Transfer datagram from one node to physically adjacent node over a link

### Link Layer Services
| Service | Description |
|---------|-------------|
| **Framing** | Encapsulate datagram into frame, add header/trailer |
| **Link Access** | Channel access if shared medium (MAC protocol) |
| **MAC Addressing** | 48-bit MAC addresses in frame headers identify source/destination |
| **Reliable Delivery** | Between adjacent nodes (rarely used on wired; wireless: high error rates) |
| **Error Detection** | Detect errors from signal attenuation, noise |
| **Error Correction** | Identify and correct bit errors without retransmission |
| **Flow Control** | Pacing between adjacent sending/receiving nodes |
| **Half/Full Duplex** | Half: one direction at a time; Full: simultaneous both directions |

### Where is Link Layer Implemented?
- In each host: Network Interface Card (NIC) or on-chip
- Implements link + physical layer
- Combination of hardware, software, firmware
- Attaches via host bus (PCI/PCIe)

---

## 6.2 Error Detection and Correction

### Error Detection Framework
- **EDC**: Error detection and correction bits (redundancy)
- **D**: Data protected by error checking
- Receiver computes EDC on received D', compares with received EDC'
- **Not 100% reliable**: Larger EDC field → better detection/correction

### Parity Checking
**Single bit parity** (even parity):
- Set parity bit so total number of 1's is even
- Detects single bit errors
- **Cannot detect**: Even number of bit flips

**Two-dimensional bit parity**:
- Row parity + column parity
- Detects AND corrects single bit errors
- Intersection of row/column parity error = error location

**Example (from slides)**: Send 1011 0110 with even-parity bit
- Data has 5 ones → parity bit = 1 → 6 ones total (even)
- Two bits flip → count changes by −2, 0, or +2 → still even → check passes
- **Answer**: No error detected (parity misses even number of flips)

### Internet Checksum (UDP/TCP)
**Sender**:
1. Treat segment (header + data + pseudo-header) as sequence of 16-bit integers
2. Compute 1's complement sum
3. Put checksum in checksum field

**Receiver**:
1. Compute 1's complement sum of received segment
2. If equals checksum field → no error detected
3. If not equal → error detected

### Cyclic Redundancy Check (CRC)
**More powerful error-detection coding**
- **D**: Data bits (binary number)
- **G**: Generator polynomial (r+1 bits)
- **R**: r CRC bits (remainder)

**Goal**: Compute R such that `<D,R>` exactly divisible by G (mod 2)
- Receiver knows G, divides `<D,R>` by G
- If non-zero remainder → error detected
- Can detect all burst errors < r+1 bits
- Widely used: Ethernet, 802.11 WiFi

**CRC Calculation**:
1. Append r zeros to data
2. Binary division by G
3. Remainder = CRC (r bits)
4. Transmit D followed by R

**Common Generators**:
- CRC-32 (Ethernet): x³² + x²⁶ + x²³ + x²² + x¹⁶ + x¹² + x¹¹ + x¹⁰ + x⁸ + x⁷ + x⁵ + x⁴ + x² + x + 1

**Numerical Example (from slides)**:
- D = 101110, d = 6, G = 1001, r = 3
- Append 3 zeros: 101110000
- Divide by 1001: remainder = 101
- Transmitted: 101110101

**Another Example**:
- Bit stream 1101011011, generator x⁴+x+1 = 10011
- Append 4 zeros, divide, remainder = CRC

---

## 6.3 Multiple Access Protocols

### Two Types of Links
1. **Point-to-point**: Ethernet switch to host, PPP, HDLC
2. **Broadcast (shared medium)**:
   - Old-fashioned Ethernet (coax)
   - Upstream HFC (cable)
   - 802.11 WiFi, 4G/5G, satellite

### Multiple Access Protocol
**Distributed algorithm** determining how nodes share channel
- Communication about channel sharing must use channel itself
- No out-of-band coordination channel

### Ideal MAC Protocol
Given: MAC channel of rate R bps
1. When one node wants to transmit → sends at rate R
2. When M nodes want to transmit → each at average rate R/M
3. Fully decentralized: no special coordinator, no clock sync
4. Simple

### MAC Protocol Taxonomy
1. **Channel Partitioning** (TDMA, FDMA, CDMA)
   - Divide channel into pieces (time slots, frequency, code)
   - Allocate piece to node for exclusive use

2. **Random Access** (ALOHA, Slotted ALOHA, CSMA, CSMA/CD, CSMA/CA)
   - Channel not divided, allow collisions
   - "Recover" from collisions

3. **Taking Turns** (Polling, Token Passing)
   - Nodes take turns; nodes with more data take longer turns

---

### CSMA (Carrier Sense Multiple Access)
**Simple CSMA**: Listen before transmit
- If channel sensed idle → transmit entire frame
- If channel sensed busy → defer transmission

**CSMA/CD**: CSMA with Collision Detection
- Collisions detected within short time
- Colliding transmissions aborted (reduces wastage)
- Easy in wired, difficult in wireless

### CSMA Collisions
- Propagation delay means two nodes may not hear each other's just-started transmission
- Collision: entire packet transmission time wasted
- Distance & propagation delay affect collision probability

### Ethernet CSMA/CD Algorithm
1. NIC receives datagram, creates frame
2. If channel idle → start transmission; if busy → wait until idle
3. If transmits entire frame without collision → done
4. If detects collision while sending → abort, send jam signal
5. **Binary Exponential Backoff**:
   - After n collisions, choose K randomly from {0, 1, ..., 2ⁿ⁻¹}
   - Wait K × 512 bit times, return to step 2
   - More collisions → longer backoff

### Is Collision Detection Still Used?
**Modern Ethernet (Switched, Full-Duplex)**:
- Switch gives each device dedicated cable/port
- Each direction has own channel → no collisions
- Collision detection switched OFF
- **Wi-Fi still shared**: Everyone uses one radio channel → collisions happen (CSMA/CA)

---

## 6.4 Switched LANs

### MAC Addresses
- **32-bit IP address**: Network-layer, used for L3 forwarding
- **48-bit MAC address**: Link-layer, used locally to get frame between physically-connected interfaces
- **Format**: 6 bytes, hexadecimal (e.g., 1A-2F-BB-76-09-AD)
- **Burned in NIC ROM** (usually unique); sometimes software-assigned (WiFi private addresses)

**Analogy**: MAC = Aadhar number; IP = Postal address
**Portability**: MAC flat address → can move interface between LANs; IP depends on subnet

### Private Wi-Fi Addresses
- Factory address = same everywhere → tracking risk
- Private address: invented per network (different at mall, airport, campus)
- Second hex digit: 2, 6, A, E = locally assigned
- Trade-off: Breaks sign-ins, fixed IP bookings, device allow-lists

---

### ARP (Address Resolution Protocol)
**Question**: How to determine MAC address knowing IP address?

**ARP Table**: Each IP node (host, router) on LAN has table:
- IP/MAC mappings: `<IP address; MAC address; TTL>`
- TTL: Time after which mapping forgotten (typically minutes)

### ARP Protocol in Action
**Example**: A wants to send to B, B's MAC not in A's ARP table
1. **ARP Query**: A broadcasts frame (dst MAC = FF-FF-FF-FF-FF-FF) containing "Who has B's IP? Tell A"
2. All nodes receive; only B (matching IP) replies
3. **ARP Reply**: B unicasts to A: "B's IP is at MAC"
4. A caches mapping in ARP table

**Key points**:
- All nodes receive broadcast; only target replies
- Both A and B update their ARP tables
- ARP trusts replies → ARP spoofing possible

**MCQ (from slides)**: A asks "who has B's IP?" in frame to FF-FF-FF-FF-FF-FF. Who receives/answers?
- a) Only B receives, B answers → False
- b) **All nodes receive; only B answers to A** → True
- c) All receive, all answer → False
- d) Only router receives → False

**MCQ (from slides)**: After A asked, B answered. Whose ARP table has new entry?
- a) Only A's → False
- b) **A's and B's (each other's)** → True
- c) Every node's → False
- d) Only switch's → False

---

### Routing to Another Subnet (IP + MAC Addressing Walkthrough)
**Scenario**: A (111.111.111.111) → B (222.222.222.222) via Router R

**Key Principle**: IP addresses stay same end-to-end; MAC addresses only get you to next hop

**Step-by-step**:
1. A compares subnet → B not on same LAN → send to default gateway R
2. A resolves R's MAC via ARP on left LAN
3. A creates IP datagram (src A, dst B), encapsulates in frame (src A, dst R)
4. R receives, strips frame, checks routing table → forward out right interface
5. R resolves B's MAC via ARP on right LAN
6. R re-encapsulates: new frame (src R-right, dst B), same IP datagram
7. B receives, extracts IP datagram, delivers to transport layer

**Frame-by-frame sequence (from slides)**:
| Step | Sender | Receiver | Message | Src MAC | Dst MAC |
|------|--------|----------|---------|---------|---------|
| 1 | A | - | Compare subnets (different) → send to R | - | - |
| 2 | A | All left LAN | ARP Request: "Who has R? Tell A" | A | FF-FF-FF-FF-FF-FF |
| 3 | R | A | ARP Reply: "R is at MAC_R" | MAC_R | A |
| 4 | A | R | Data frame (IP: A→B, MAC: A→R) | A | MAC_R |
| 5 | R | - | Strip frame, route to right interface | - | - |
| 6 | R | All right LAN | ARP Request: "Who has B? Tell R" | MAC_R | FF-FF-FF-FF-FF-FF |
| 7 | B | R | ARP Reply: "B is at MAC_B" | MAC_B | MAC_R |
| 8 | R | B | Data frame (IP: A→B, MAC: R→B) | MAC_R | MAC_B |

---

## 6.5 Ethernet

### Dominant Wired LAN Technology
- First widely used LAN tech
- Simpler, cheaper
- Speed race: 10 Mbps → 800 Gbps (1.6 Tbps coming)
- Single chip, multiple speeds

### Ethernet Topology
| Type | Description |
|------|-------------|
| **Bus** (legacy) | All nodes in same collision domain |
| **Switched** (modern) | Active L2 switch in center; each spoke separate collision domain; full duplex |

### Hub vs Switch
- **Hub**: Repeats every bit to every port → 1 collision domain
- **Switch**: Each port own collision domain; full duplex → no collisions

**MCQ (from slides)**: 8 PCs on hub, 8 on switch. How many collision domains?
- a) **Hub: 1; switch: 8** → True
- b) Hub: 8; switch: 1
- c) Hub: 1; switch: 1
- d) Hub: 8; switch: 8

### Ethernet Frame Structure
```
Preamble (8 bytes) | Dest MAC (6) | Src MAC (6) | Type (2) | Data (46-1500) | CRC (4)
```
- **Preamble**: 7 bytes 10101010 + 1 byte 10101011 (clock sync)
- **Addresses**: Dest first (early filtering)
- **Type**: Higher layer protocol (0x0800 = IP)
- **CRC**: Cyclic redundancy check
- **Min frame**: 64 bytes (512 bits = collision budget)
- **Max frame**: 1518 bytes (1500 MTU + 18 header/CRC)

**Smallest frame**: 6+6+2+46+4 = 64 bytes
**Largest frame**: 6+6+2+1500+4 = 1518 bytes

### Ethernet: Unreliable, Connectionless
- **Connectionless**: No handshaking between NICs
- **Unreliable**: No ACKs/NAKs; dropped frames recovered only by higher layer (TCP)
- **MAC Protocol**: Unslotted CSMA/CD with binary backoff (shared links)

**MCQ (from slides)**: Frame fails CRC at second router. Who notices, who resends?
- a) Second router asks first to resend → False
- b) **TCP at sender notices gap and resends** → True
- c) First router resends after timeout → False
- d) Nobody: file arrives with hole → False

---

## 6.6 Ethernet Switches

### Switch = Link-Layer Device
- Stores and forwards Ethernet frames
- Examines destination MAC, selectively forwards
- **Transparent**: Hosts unaware of switches
- **Plug-and-play, Self-learning**

### Self-Learning
- When frame received → "learn" sender location (incoming interface)
- Record (MAC, interface) in switch table with timestamp (TTL ~60s)

### Forwarding/Filtering
When frame received:
1. Record incoming link, sender MAC
2. Lookup destination MAC in table
3. If found:
   - If destination on same segment → drop
   - Else forward on indicated interface
4. If not found → **flood** (forward on all except arriving interface)
5. Broadcast frames (FF-FF-FF-FF-FF-FF) always flooded

### Interconnecting Switches
- Self-learning works across multiple switches
- Switch learns which host reachable via which switch port

**MCQ (from slides)**: C sends to I, I replies to C. Switch 2 learns C but not I. Why?
- a) **S4 knew C was toward S1, so I's reply skipped S2** → True
- b) S2's table was full
- c) S2 learns only from frames addressed to it
- d) I's reply was broadcast

**MCQ (from slides)**: Laptop sends ARP broadcast. Which devices receive it?
- a) Only devices on laptop's own switch
- b) Only router
- c) **Every device on every switch, up to router** → True
- d) Every device, including outside networks

---

## 6.7 VLANs (Virtual LANs)

### Problem: Large Broadcast Domain
- Traditional switched LAN = single broadcast domain
- As LAN grows: broadcast traffic (ARP, DHCP, unknown MAC) reaches everyone
- Scaling, security, privacy issues

### What is a VLAN?
Method of dividing single physical switched network into multiple logical LANs
- Devices in same VLAN communicate as if on same physical network
- Even if connected to different switches/locations

### VLAN Tag (802.1Q)
4-byte tag inserted after source MAC:
```
Tag marker (0x8100) | Priority (3) | Drop (1) | VLAN ID (12 bits)
```
- **Priority**: 0-7 (voice = 5)
- **VLAN ID**: 12 bits → 4,094 usable VLANs (0, 4095 reserved)
- Frame grows from 1518 to 1522 bytes

### Access vs Trunk Ports
| Port Type | Description |
|-----------|-------------|
| **Access** | One VLAN only; frames untagged to/from device |
| **Trunk** | Multiple VLANs; frames tagged |
| **Native VLAN** | One VLAN crosses trunk untagged; both ends must agree |

### VLAN-Aware Switch Forwarding
1. Note frame's VLAN (from port or tag)
2. Learn: Record (VLAN, src MAC) → port
3. Lookup (VLAN, dest MAC):
   - Known: send on that port
   - Unknown/broadcast: flood **only to ports in same VLAN + trunks carrying it**
4. Tag/untag on output: add tag on trunk, remove on access

**MCQ (from slides)**: PC on access port 5 (VLAN 20) sends broadcast. Ports 1-2 VLAN 10, 5-6 VLAN 20, 8 trunk (10,20). Where does broadcast go?
- a) Every port (broadcasts ignore VLANs)
- b) **Port 6 untagged, port 8 tagged 20** → True
- c) Only port 8 (trunk) tagged 20
- d) Only router

### Inter-VLAN Routing
- **Each VLAN = separate IP network**
- **Crossing VLANs = routing** (L3)
- Options: Router on trunk, or Layer-3 switch (switch + router in one)

---

## 6.8 A Day in the Life of a Web Request (Synthesis)

**Scenario**: Student on campus network requests www.google.com

### Protocol Stack Journey
1. **DHCP**: Get IP, gateway, DNS server
2. **ARP**: Get gateway MAC
3. **DNS**: Resolve www.google.com → IP
4. **TCP 3-way handshake**: Establish connection
5. **HTTP Request/Response**: Get web page
6. **Link Layer**: Ethernet frames, switch forwarding, VLANs

**Key insight**: Every layer involved; encapsulation/decapsulation at each hop

---

## 6.9 Physical Layer

### Purpose
Encode binary digits (frames) into signals to transmit/receive across physical media
- **Analog signal**: Continuous-valued (amplitudes, frequencies)
- **Digital signal**: Discrete-valued (0s & 1s)
- **Physical media**: Copper, optical fiber, wireless

### Physical Layer Elements
1. Physical media & connectors
2. Bit representation on media
3. Encoding of data & control info
4. Transmitter/receiver circuitry

### Physical Layer Devices
- Hub, Repeater, Modem, Cables, Network Adapters

### Encoding Schemes
| Encoding | Description |
|----------|-------------|
| **NRZ** | Low voltage = 0, high voltage = 1 |
| **Manchester** | Low→high transition = 1; high→low = 0 (self-clocking) |
| **4B/5B** | 4 data bits → 5 code bits (Ethernet 100 Mbps) |
| **8B/10B** | 8 data bits → 10 code bits (Gigabit Ethernet) |

### Transmission Media
| Media | Characteristics |
|-------|-----------------|
| **Twisted Pair (UTP/STP)** | Cat5e: 1 Gbps; Cat6: 10 Gbps; 100m max |
| **Coaxial Cable** | Two concentric conductors; cable TV/HFC |
| **Fiber Optic (SMF/MMF)** | Light pulses; 10s-100s Gbps; km distances; immune to EMI |
| **Wireless Radio** | Electromagnetic spectrum; broadcast, half-duplex |

---

## 6.10 Wireless LANs: IEEE 802.11

### Wireless Network Context
- More mobile subscribers than fixed (10:1)
- More mobile broadband devices than fixed (5:1)
- Two challenges: **Wireless** (comm over wireless link) + **Mobility** (changing attachment point)

### Elements of Wireless Network
- **Wireless hosts**: Laptop, smartphone, IoT (stationary or mobile)
- **Base station**: Connected to wired network; relays between wired and wireless hosts (cell tower, AP)
- **Wireless link**: Connects mobiles to base station; multiple access protocol coordinates access

### Wireless Network Taxonomy
| | Single Hop | Multiple Hops |
|---|------------|---------------|
| **Infrastructure** | Host → AP → Internet (WiFi, 4G/5G) | Mesh: relay through wireless nodes |
| **Ad Hoc** | No base station, no Internet (Bluetooth) | MANET, VANET |

---

### IEEE 802.11 (WiFi) Architecture
- **BSS** (Basic Service Set): Wireless hosts + Access Point (AP)
- **SSID**: Service Set ID (network name)
- **Channels**: 2.4 GHz (11 channels), 5 GHz, 6 GHz (WiFi 6E)
- **Association**: Scan channels → select AP → authenticate → DHCP

### 802.11 Standards Evolution
| Standard | Year | Max Rate | Frequency | Brand |
|----------|------|----------|-----------|-------|
| 802.11b | 1999 | 11 Mbps | 2.4 GHz | WiFi 1 |
| 802.11g | 2003 | 54 Mbps | 2.4 GHz | WiFi 3 |
| 802.11n | 2009 | 600 Mbps | 2.4/5 GHz | WiFi 4 |
| 802.11ac | 2013 | 3.47 Gbps | 5 GHz | WiFi 5 |
| 802.11ax | 2020 | 14 Gbps | 2.4/5/6 GHz | WiFi 6/6E |
| 802.11be | 2024 | 46 Gbps | 2.4/5/6/7 GHz | WiFi 7 |

All use **CSMA/CA** for multiple access

### CSMA/CA (Collision Avoidance)
**Why not CSMA/CD?**: Collision detection difficult in wireless (can't transmit and listen simultaneously on same frequency)

**CSMA/CA Mechanism**:
1. **Listen** (DIFS): If idle → wait random backoff, then transmit
2. **RTS/CTS** (optional): Reserve channel (hidden terminal problem)
3. **ACK**: Receiver sends ACK after successful frame
4. **No ACK** → assume collision/loss → backoff, retry

### 802.11 Frame Structure
- **Frame Control**: Type (data, control, management), subtype
- **Duration/ID**: NAV (Network Allocation Vector) for virtual carrier sense
- **Addresses**: Up to 4 addresses (src, dst, BSSID, transmitter/receiver)
- **Sequence Control**: Fragment number, sequence number
- **Frame Body**: Payload
- **FCS**: Frame Check Sequence (CRC-32)

### Hidden/Exposed Terminal Problems
- **Hidden Terminal**: A and C can't hear each other, both transmit to B → collision at B
  - **Solution**: RTS/CTS (Request to Send / Clear to Send)
- **Exposed Terminal**: B transmitting to A, C hears B → C defers unnecessarily
  - C could transmit to D without interfering

### Power Management
- **PSM (Power Save Mode)**: Client sleeps, wakes for beacon, tells AP it's awake
- **TIM (Traffic Indication Map)**: AP buffers frames for sleeping clients

---

## Key Formulas (Link Layer)

| Formula | Equation |
|---------|----------|
| Parity (even) | Parity bit = 1 if odd number of 1s in data |
| CRC | Remainder of D × 2ʳ ÷ G (mod 2) |
| Ethernet Min Frame | 64 bytes = 512 bits (collision budget) |
| Ethernet Max Frame | 1518 bytes (1500 MTU + 18 header) |
| Binary Exponential Backoff | Wait K × 512 bit times, K ∈ {0, ..., 2ⁿ⁻¹} |
| CSMA/CA Backoff | Wait random slots × slot_time after DIFS |
| NAV (Virtual Carrier) | Duration field in RTS/CTS/Data frames |

---

## Complete Questions, Examples, and MCQs from Slides and Textbook

### Numerical Problems (Exam Practice)

**Q1. Parity Check**: Send 1011 0110 with even parity. Two bits flip. What does receiver conclude?
- Data has 5 ones → parity = 1 (even total)
- Two flips change count by ±2 or 0 → still even
- **Answer**: No error detected

**Q2. Two-Dimensional Parity**: Given matrix with row/column parity, detect and correct single-bit error
- Row parity error on row 3, column parity error on column 2
- Error at (3,2): flip bit

**Q3. CRC Calculation**: D = 101110, G = 1001 (r=3)
- Append 3 zeros: 101110000
- Divide by 1001: remainder = 101
- Transmitted: 101110101

**Q4. CRC Numerical**: Bit stream 1101011011, generator x⁴+x+1 = 10011
- Append 4 zeros, divide by 10011
- Compute remainder → transmitted bit string

**Q5. Ethernet Frame Size**: Dest 6B, Src 6B, Type 2B, Data 46-1500B, CRC 4B
- Min frame = 6+6+2+46+4 = 64 bytes
- Max frame = 6+6+2+1500+4 = 1518 bytes
- Preamble (8B) not counted

**Q6. Binary Exponential Backoff**: After 3 collisions
- K ∈ {0, 1, ..., 2³⁻¹} = {0, 1, 2, 3, 4, 5, 6, 7}
- Wait K × 512 bit times

**Q7. VLAN Tag**: 4 bytes after source MAC
- TPID: 0x8100
- Priority: 3 bits (0-7)
- Drop eligible: 1 bit
- VLAN ID: 12 bits (4094 usable)

---

### Review Questions

1. **Link layer services?**
   - Framing, link access, reliable delivery, error detection/correction, flow control

2. **Where is link layer implemented?**
   - NIC or on-chip; hardware/software/firmware

3. **Parity vs CRC?**
   - Parity: single bit, detects odd flips only
   - CRC: polynomial division, detects all bursts < r+1 bits

4. **Internet checksum?**
   - 1's complement sum of 16-bit words; weak (misses compensating errors)

5. **CSMA/CD vs CSMA/CA?**
   - CD: detects collision, aborts (wired)
   - CA: avoids collision, uses ACK/RTS/CTS (wireless)

6. **Why no collision detection in modern Ethernet?**
   - Switched full-duplex = dedicated channels = no collisions

7. **MAC vs IP address?**
   - MAC: 48-bit, flat, local delivery, portable
   - IP: 32-bit, hierarchical, global routing, subnet-dependent

8. **ARP operation?**
   - Broadcast query "Who has IP X?" → unicast reply "X is at MAC Y"

9. **Switch self-learning?**
   - Learn src MAC → port on frame arrival; flood if dest unknown

10. **VLAN purpose?**
    - Divide broadcast domain; security, scalability, privacy

11. **Access vs trunk port?**
    - Access: 1 VLAN, untagged; Trunk: multiple VLANs, tagged

12. **Inter-VLAN routing?**
    - Requires router or L3 switch; each VLAN = separate IP subnet

13. **802.11 CSMA/CA?**
    - Listen (DIFS), random backoff, transmit, wait ACK, retry on failure

14. **Hidden terminal problem?**
    - A and C can't hear each other, both transmit to B
    - Solution: RTS/CTS reserves channel

15. **Physical layer encoding?**
    - NRZ, Manchester, 4B/5B, 8B/10B for clock recovery, DC balance

---

## Multiple Choice Questions (from Slides)

**Q1. Link layer services include:**
- a) Framing, link access, MAC addressing
- b) Reliable delivery, error detection, flow control
- c) Half/full duplex
- d) **All of the above**

**Q2. Error detection framework:**
- EDC not 100% reliable; larger EDC → better detection

**Q3. Single bit parity - can detect:**
- a) Single bit errors
- b) **Odd number of bit flips** → True
- c) Even number of bit flips → False (misses)

**Q4. Two-dimensional parity:**
- Detects AND corrects single-bit errors

**Q5. CRC - can detect all burst errors of length:**
- Less than r+1 bits

**Q6. Multiple access links - shared wire:**
- Old Ethernet, upstream HFC

**Q7. Shared radio:**
- 802.11 WiFi, 4G/5G, satellite

**Q8. Ideal MAC protocol desiderata:**
1. One node → rate R
2. M nodes → R/M each
3. Fully decentralized
4. Simple

**Q9. CSMA/CD - collision detection:**
- Easy in wired, difficult in wireless
- Colliding transmissions aborted (reduces wastage)

**Q10. CSMA collisions still occur because:**
- Propagation delay → two nodes may not hear each other's just-started transmission

**Q11. Ethernet CSMA/CD backoff:**
- After n collisions, K ∈ {0, ..., 2ⁿ⁻¹}, wait K×512 bit times

**Q12. Modern Ethernet - collision detection:**
- Switched OFF (full-duplex, no collisions)

**Q13. Wi-Fi - still shared, uses:**
- CSMA/CA

**Q14. MAC address - 48-bit, format:**
- Hexadecimal, 6 bytes (e.g., 1A-2F-BB-76-09-AD)

**Q15. Private Wi-Fi addresses - second hex digit:**
- 2, 6, A, E = locally assigned

**Q16. ARP table entries:**
- <IP address; MAC address; TTL>

**Q17. ARP query destination MAC:**
- FF-FF-FF-FF-FF-FF (broadcast)

**Q18. ARP - who receives broadcast, who answers?**
- All nodes receive; only target answers

**Q19. After ARP exchange - whose table updated?**
- Both A's and B's (each other's)

**Q20. ARP trusts replies → ARP spoofing possible**

**Q21. Routing to another subnet - key principle:**
- IP addresses stay same end-to-end; MAC addresses only get you to next hop

**Q22. Hub vs Switch collision domains:**
- Hub: 1 collision domain; Switch: 1 per port (8 ports = 8 domains)

**Q23. Ethernet frame - addresses order:**
- Destination first (early filtering)

**Q24. Smallest Ethernet frame (excluding preamble):**
- 64 bytes (512 bits)

**Q25. Largest Ethernet frame (excluding preamble):**
- 1518 bytes

**Q26. Ethernet unreliable, connectionless:**
- No ACKs; dropped frames recovered by TCP

**Q27. Frame fails CRC at router 2 - who resends?**
- TCP at sender (end-to-end)

**Q28. Switch self-learning:**
- Record (src MAC, incoming port) on frame arrival

**Q29. Switch forwarding:**
- Known dest → forward on port; Unknown → flood (except arriving)

**Q30. Switch interconnecting - self-learning works across switches**

**Q31. Broadcast domain - ARP broadcast goes to:**
- Every device on every switch, up to router

**Q32. VLAN - divides single physical network into:**
- Multiple logical LANs

**Q33. VLAN tag - 4 bytes, fields:**
- TPID (0x8100), Priority (3b), Drop (1b), VLAN ID (12b)

**Q34. Access port:**
- One VLAN, untagged frames

**Q35. Trunk port:**
- Multiple VLANs, tagged frames

**Q36. Native VLAN:**
- One VLAN crosses trunk untagged; both ends must agree

**Q37. VLAN-aware forwarding:**
- Lookup (VLAN, dest MAC); flood only within VLAN + trunks

**Q38. Inter-VLAN routing:**
- Router or L3 switch; each VLAN = separate IP network

**Q38. Web request life - protocol stack journey:**
- DHCP → ARP → DNS → TCP handshake → HTTP → Link layer

**Q39. Physical layer encoding:**
- NRZ, Manchester, 4B/5B, 8B/10B

**Q40. Wireless taxonomy:**
- Infrastructure single-hop: WiFi, 4G/5G
- Infrastructure multi-hop: Mesh
- Ad hoc single-hop: Bluetooth
- Ad hoc multi-hop: MANET, VANET

**Q41. 802.11 architecture:**
- BSS: hosts + AP; SSID: network name; Channels: 2.4/5/6 GHz

**Q42. 802.11 standards:**
- b/g/n/ac/ax/be (WiFi 1 through 7)

**Q43. CSMA/CA vs CSMA/CD:**
- CD impossible in wireless (can't transmit+listen same frequency)
- CA: DIFS → backoff → transmit → wait ACK

**Q44. Hidden terminal:**
- A and C can't hear, both send to B → collision
- Solution: RTS/CTS

**Q45. Exposed terminal:**
- C hears B, defers; but C could send to D

---

## Textbook End-of-Chapter Problems (Chapter 6)

**P1.** Explain the difference between error detection and error correction.
**P2.** Calculate single-bit parity for a given data word.
**P3.** Perform two-dimensional parity check and identify/correct single-bit error.
**P4.** Compute Internet checksum for a given UDP segment.
**P5.** Calculate CRC for given data and generator polynomial.
**P6.** Compare CSMA/CD and CSMA/CA with timing diagrams.
**P7.** Trace Ethernet CSMA/CD exponential backoff for n=3 collisions.
**P8.** Explain why modern switched Ethernet doesn't use collision detection.
**P9.** Describe ARP operation with a diagram showing request/reply.
**P10.** Walk through IP+MAC addressing when sending to another subnet.
**P11.** Calculate Ethernet frame sizes (min/max) and explain each field.
**P12.** Trace switch self-learning and forwarding for a multi-switch topology.
**P13.** Explain VLAN operation: tagging, access/trunk ports, inter-VLAN routing.
**P14.** Describe the protocol stack journey of a web request.
**P15.** Compare physical layer encoding schemes (NRZ, Manchester, 4B/5B, 8B/10B).
**P16.** Explain 802.11 CSMA/CA with RTS/CTS for hidden terminal problem.
**P17.** Compare infrastructure vs ad-hoc wireless network architectures.
**P18.** Describe 802.11 frame structure and the purpose of each field.