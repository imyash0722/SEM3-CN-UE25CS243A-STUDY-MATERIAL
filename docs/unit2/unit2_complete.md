# Unit 2: Complete Study Guide — Transport Layer

# Computer Networks (UE25CS243A) — Unit 2

## Transport Layer

**Course**: UE25CS243A | **Semester**: III (Aug-Dec 2026) | **Credits**: 4
**Textbook**: Kurose & Ross, *Computer Networking: A Top-Down Approach*, 9th Edition (2026)
**Chapter**: 3 | **Hours**: 14 | **Evaluation**: ISA-1 (40 marks → 15%)

---

## 📚 Unit Overview

| Topic | Section | Key Concepts |
|-------|---------|--------------|
| Transport Services | 3.1 | Process-to-process delivery, multiplexing/demultiplexing, TCP vs UDP |
| Multiplexing | 3.2 | UDP (2-tuple), TCP (4-tuple), port numbers, well-known ports |
| UDP | 3.3 | 8-byte header, checksum (1's complement + pseudo-header) |
| Reliable Data Transfer | 3.4 | RDT 1.0→3.0, stop-and-wait, pipelining, GBN vs SR |
| Go-Back-N | 3.4.3 | Cumulative ACK, window N ≤ 2ᵏ⁻¹, retransmit all on timeout |
| Selective Repeat | 3.4.4 | Per-packet timers, N ≤ 2ᵏ⁻¹, buffer out-of-order |
| TCP Connection | 3.5.1 | Full-duplex, point-to-point, 3-way handshake, 4-way teardown |
| TCP Segment | 3.5.2 | Sequence/ACK numbers (byte-oriented), flags, window, options (MSS) |
| RTT Estimation | 3.5.3 | EWMA (α=0.125), DevRTT (β=0.25), Timeout = EstRTT + 4×DevRTT, Karn's Algorithm |
| Reliable Transfer | 3.5.4 | Sender events, fast retransmit (3 dup ACKs), fast recovery |
| Flow Control | 3.5.5 | rwnd = RcvBuffer - (LastByteRcvd - LastByteRead), sender constraint |
| Connection Mgmt | 3.5.6 | SYN/SYN+ACK/ACK, FIN/ACK, TIME_WAIT (2×MSL ≈ 2 min) |
| Congestion Control | 3.6-3.7 | Slow Start → CA → Fast Recovery, AIMD, Tahoe/Reno/CUBIC/Vegas/BBR |
| ECN | 3.7.3 | IP ECN bits (ECT0/ECT1/CE), TCP CWR/ECE response |
| QUIC/HTTP/3 | 3.8 | 1-RTT/0-RTT, connection migration, stream independence |

---

## 📖 Quick Navigation

- [Chapter 3: Transport Layer](03_chapter3_transport_layer.md)
- [Complete Unit 2 Notes](unit2_complete.md)

---

## ✅ Study Checklist (ISA-1)

### Transport Services & UDP
- [ ] Process-to-process delivery via ports (multiplexing/demultiplexing)
- [ ] UDP: 2-tuple demux; TCP: 4-tuple demux
- [ ] UDP header: src/dst port (16b), length (16b), checksum (16b) = 8 bytes
- [ ] UDP checksum: 1's complement sum of 16-bit words + pseudo-header

### Reliable Data Transfer (RDT)
- [ ] RDT evolution: 1.0 (reliable) → 2.0 (bit errors, ACK/NAK) → 2.1 (corrupt ACK) → 2.2 (NAK-free) → 3.0 (loss + errors, timers)
- [ ] Stop-and-wait utilization: U = (L/R) / (RTT + L/R)
- [ ] Pipelining: sender allows multiple in-flight packets
- [ ] GBN: cumulative ACK, window bound N ≤ 2ᵏ⁻¹, retransmit ALL on timeout
- [ ] SR: selective ACK, per-packet timers, N ≤ 2ᵏ⁻¹, buffer out-of-order

### TCP
- [ ] Segment structure: seq# (byte of first data), ACK# (next expected byte), flags (SYN, ACK, FIN, RST, PSH, URG, ECE, CWR), window (rwnd)
- [ ] MSS = MTU - 40 (typically 1460 bytes)
- [ ] RTT estimation: EstRTT = 0.875×EstRTT + 0.125×SampleRTT, DevRTT = 0.75×DevRTT + 0.25×|SampleRTT-EstRTT|
- [ ] Timeout = EstRTT + 4×DevRTT, exponential backoff on timeout
- [ ] Karn's Algorithm: don't measure SampleRTT for retransmitted segments
- [ ] Sender: data from app → create segment, start timer if first; timeout → retransmit oldest, restart; ACK(y>SendBase) → SendBase=y, restart if unACKed remain
- [ ] Fast retransmit: 3 dup ACKs → retransmit missing immediately, enter fast recovery
- [ ] Fast recovery: ssthresh=cwnd/2, cwnd=ssthresh+3MSS, per dup ACK cwnd+=1MSS, on new ACK cwnd=ssthresh
- [ ] Flow control: rwnd = RcvBuffer - (LastByteRcvd - LastByteRead), sender limits unACKed to min(cwnd, rwnd)
- [ ] 3-way handshake: SYN(x) → SYN+ACK(y, x+1) → ACK(x+1, y+1)
- [ ] 4-way teardown: FIN(u) → ACK(u+1) → FIN(v) → ACK(v+1), TIME_WAIT = 2×MSL

### Congestion Control
- [ ] Slow Start: cwnd=1 MSS (10 MSS per RFC 3390), per ACK cwnd+=1 MSS (doubles/RTT), exit when cwnd≥ssthresh
- [ ] Congestion Avoidance: per RTT cwnd+=1 MSS (linear), per ACK cwnd+=MSS×(MSS/cwnd)
- [ ] Timeout: ssthresh=cwnd/2, cwnd=1 MSS, enter Slow Start
- [ ] 3 Dup ACKs: ssthresh=cwnd/2, cwnd=ssthresh+3 MSS, Fast Recovery
- [ ] AIMD: Additive Increase (1 MSS/RTT), Multiplicative Decrease (÷2)
- [ ] Macroscopic throughput: 0.75×W/RTT (W = cwnd at loss)
- [ ] Loss rate model: Throughput ≈ 1.22×MSS/(RTT×√L)
- [ ] CUBIC: cwnd = C×(t-K)³ + W_max, less RTT-dependent
- [ ] Vegas: delay-based, Expected = cwnd/RTT_min, Actual = cwnd/RTT_curr
- [ ] BBR: model-based, BDP = BW×RTT_min, pacing = BDP×gain, ignores loss
- [ ] ECN: IP ECN bits (ECT0/ECT1/CE), TCP response: cwnd/=2, ssthresh=cwnd, set CWR

### QUIC/HTTP/3
- [ ] TCP+TLS 1.3 = 2 RTT; QUIC+TLS 1.3 = 1 RTT; QUIC 0-RTT resume
- [ ] Connection ID survives IP change (migration)
- [ ] Stream independence: lost packet blocks only that stream

---

## 🧠 Key Formulas (Memorize)

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
| Macroscopic Throughput | `0.75 × W / RTT` |
| Loss Rate (Padhye) | `1.22 × MSS / (RTT × √L)` |
| TIME_WAIT | `2 × MSL ≈ 2 minutes` |

---

## ❓ Quick Self-Test

1. **Difference between GBN and SR?**
2. **Why is SR window size ≤ 2ᵏ⁻¹?**
3. **TCP sequence number = ?**
4. **TCP ACK number = ?**
5. **How does TCP flow control work?**
6. **Slow Start vs Congestion Avoidance?**
7. **Fast Retransmit trigger?**
8. **Timeout vs 3 Dup ACKs reaction?**
9. **What is BBR?**
10. **What is ECN?**

---

## 🎯 Exam-Relevant MCQ Patterns

- Numerical: Calculate EstimatedRTT, DevRTT, TimeoutInterval from SampleRTT sequence
- Numerical: GBN/SR transmission count for given loss pattern (e.g., "every 5th packet lost, N=10")
- Numerical: Macroscopic throughput from loss rate
- Conceptual: TCP state machine transitions (handshake, teardown)
- Conceptual: Identify congestion control phase from cwnd behavior
- Conceptual: QUIC advantage over TCP+TLS

---

*Unit 2 covers Chapter 3. ISA-1 evaluates Units 1 & 2 (40 marks → 15%).*

---

# Unit 2: Transport Layer (Chapter 3)

## 3.1 Introduction and Transport-Layer Services

### 3.1.1 Relationship Between Transport and Network Layers
- **Network Layer (IP)**: Host-to-host delivery (IP addresses)
- **Transport Layer (TCP/UDP)**: Process-to-process delivery (port numbers)

**Analogy**: 
- Houses = Hosts
- Kids = Processes
- Letters = Application messages
- Ann/Bill (parents) = Transport layer (sorting letters to kids)
- Postal service = Network layer (delivering between houses)

**Key point**: Transport layer enhances network layer service:
- IP = best-effort, unreliable
- TCP = reliable, ordered, flow/congestion control on top of IP
- UDP = minimal enhancement (just multiplexing + checksum)

### 3.1.2 Overview of Transport Layer in the Internet
Two protocols:
- **TCP**: Reliable, connection-oriented, byte stream
- **UDP**: Unreliable, connectionless, datagram

| Feature | TCP | UDP |
|---------|-----|-----|
| Reliability | ✓ | ✗ |
| Ordering | ✓ | ✗ |
| Connection setup | 3-way handshake | None |
| Flow control | ✓ | ✗ |
| Congestion control | ✓ | ✗ |
| Header size | 20-60 bytes | 8 bytes |
| Use cases | Web, email, file transfer | DNS, streaming, gaming, QUIC |

---

## 3.2 Multiplexing and Demultiplexing

### Core Concept
- **Multiplexing** (sender): Gather data from multiple sockets, add transport headers, pass to network layer
- **Demultiplexing** (receiver): Use header fields to deliver segment to correct socket

### UDP Demultiplexing
- **2-tuple**: (Destination IP, Destination Port)
- All datagrams with same dest IP+port → same socket
- Different sources can send to same socket

### TCP Demultiplexing
- **4-tuple**: (Source IP, Source Port, Destination IP, Destination Port)
- Each connection = unique 4-tuple = unique socket
- Server can handle millions of connections on same port (e.g., port 80)

**Why the difference?**
- UDP: stateless, each datagram independent
- TCP: stateful (sequence numbers, buffers, timers); needs 4-tuple to identify connection state

---

## 3.3 Connectionless Transport: UDP

### 3.3.1 UDP Segment Structure
```
 0      7 8     15 16    23 24    31
+--------+--------+--------+--------+
|     Source Port      | Destination Port |
+--------+--------+--------+--------+
|     Length           |    Checksum     |
+--------+--------+--------+--------+
|          Data (application message)         |
+---------------------------------------------+
```
**Fields**:
- **Source Port** (16 bits): Optional, for replies
- **Destination Port** (16 bits): Required for demultiplexing
- **Length** (16 bits): Total segment length (header + data) in bytes
- **Checksum** (16 bits): Error detection (Internet checksum)
- **Header size**: Exactly 8 bytes

### 3.3.2 UDP Checksum (Internet Checksum)
**Goal**: Detect bit errors in header + data

**Sender Algorithm**:
1. Treat header + data as sequence of 16-bit words
2. Add pseudo-header (source IP, dest IP, zero, protocol=17, UDP length)
3. Sum all 16-bit words using **1's complement arithmetic**
4. Add any carry-around (wrap-around) to LSB
5. Take 1's complement (flip all bits) → checksum
6. Insert checksum in segment

**Receiver Algorithm**:
1. Sum all 16-bit words (including checksum) using 1's complement
2. Add carry-around
3. If result = all 1's (0xFFFF) → no error detected
4. Else → error detected

**Why 1's complement?** 
- Endian-independent (carry wraps same way)
- Easy verification: sum + checksum = all 1s

**Pseudo-header**: Protects against misdelivery (wrong IP/port)

---

## 3.4 Principles of Reliable Data Transfer

### 3.4.1 Building a Reliable Data Transfer Protocol
**Problem**: Underlying channel can lose, corrupt, duplicate, reorder packets
**Goal**: Provide reliable, in-order delivery to application

**Approach**: ACK/NAK + Retransmission + Sequence Numbers

#### rdt 1.0: Reliable channel
- No errors, no loss
- Simple: send, receive, deliver

#### rdt 2.0: Channel with bit errors
- Add **checksum** for error detection
- **ACK** (positive acknowledgment) / **NAK** (negative acknowledgment)
- **Retransmission** on NAK or corrupted ACK/NAK
- **Sequence numbers** (0/1) to detect duplicates

#### rdt 2.1: Sender handles corrupted ACK/NAK
- Add sequence number to ACK/NAK
- Sender retransmits if ACK/NAK corrupted

#### rdt 2.2: NAK-free (only ACKs)
- Receiver sends ACK for last correctly received packet
- Sender retransmits on timeout if no ACK
- Duplicate ACKs trigger retransmission

#### rdt 3.0: Channel with loss AND errors
- **Timer** for each packet
- Timeout → retransmit
- **Problem**: How to set timeout? (covered in 3.5.3)

### 3.4.2 Pipelined Reliable Data Transfer Protocols
**Stop-and-Wait**: Send one packet, wait for ACK → low utilization
**Utilization**: `U = (L/R) / (RTT + L/R)`

**Pipelining**: Send multiple packets before waiting for ACKs
- Increases utilization
- Requires: larger sequence number space, buffering at sender/receiver

**Two main approaches**:
1. **Go-Back-N (GBN)**
2. **Selective Repeat (SR)**

### 3.4.3 Go-Back-N (GBN)
**Sender Window**: Size N, sequence numbers `[base, base+N-1]`
- `base` = oldest unACKed packet
- `nextseqnum` = next packet to send

**Sender Behavior**:
- On data from app: if window not full, send packet, start timer if first in window
- On ACK: cumulative ACK (ACK n = all up to n received); slide window
- On timeout: **retransmit ALL packets from base to nextseqnum-1**

**Receiver Behavior**:
- Only accepts in-order packets
- Sends ACK for highest in-order packet received
- Discards out-of-order packets (sends duplicate ACK)

**Window Size Constraint**: `N ≤ 2ᵏ - 1` (k = sequence number bits)
- Prevents ambiguity between old and new packets

**Utilization**: `U = N × (L/R) / (RTT + L/R)` (if N < N_optimal)

**Example (N=10, every 5th packet lost)**:
- Round 1: Send 1-10, lose 5,10 → ACK 4, timeout → 18 total transmissions

### 3.4.4 Selective Repeat (SR)
**Sender Window**: Size N, per-packet timers
- Only retransmits **specific timed-out packet**

**Receiver Window**: Size N, buffers out-of-order packets
- Accepts packets in `[rcv_base, rcv_base+N-1]`
- Sends individual ACK for each packet
- Delivers in-order to application when possible

**Window Size Constraint**: `N ≤ 2ᵏ⁻¹` (Proof: 2N ≤ 2ᵏ → N ≤ 2ᵏ⁻¹)
- Prevents overlap between sender and receiver windows

**Utilization**: Same as GBN but fewer retransmissions

**Example (same conditions)**: 12 total transmissions (only retransmit lost packets)

---

## 3.5 Connection-Oriented Transport: TCP

### 3.5.1 The TCP Connection
- **Full-duplex**: Both sides send/receive simultaneously
- **Point-to-point**: One sender, one receiver (no multicast)
- **Connection state**: Buffers, sequence numbers, timers, congestion control vars
- **3-way handshake** to establish; **4-way teardown** to close

### 3.5.2 TCP Segment Structure
```
 0                   15 16                  31
+----------------------+----------------------+
|     Source Port      |   Destination Port   |
+----------------------+----------------------+
|        Sequence Number (32 bits)            |
+----------------------+----------------------+
|       Acknowledgment Number (32 bits)       |
+----------------------+----------------------+
|  HdrLen  | Reserved |Flags|   Window Size    |
+----------------------+----------------------+
|      Checksum        |   Urgent Pointer     |
+----------------------+----------------------+
|         Options (variable)                  |
+----------------------+----------------------+
|               Data                          |
+---------------------------------------------+
```

**Key Fields**:
- **Sequence Number**: Byte number of FIRST data byte in segment
- **Acknowledgment Number**: Next expected byte (cumulative ACK)
- **Flags**: SYN, ACK, FIN, RST, PSH, URG, ECE, CWR
- **Window Size**: Flow control (rwnd) - 16 bits (scaled by window scale option)
- **Options**: MSS, Window Scale, SACK, Timestamps

**MSS** (Maximum Segment Size): `MSS = MTU - 40` (typically 1460 bytes)

### 3.5.3 Round-Trip Time Estimation and Timeout (RFC 6298)

**SampleRTT**: Measured RTT for a segment (sent → ACK received)
**EstimatedRTT** (smoothed):
```
EstimatedRTT = (1 - α) × EstimatedRTT + α × SampleRTT
α = 0.125 (1/8)
EstimatedRTT = 0.875 × EstimatedRTT + 0.125 × SampleRTT
```

**DevRTT** (variation):
```
DevRTT = (1 - β) × DevRTT + β × |SampleRTT - EstimatedRTT|
β = 0.25 (1/4)
DevRTT = 0.75 × DevRTT + 0.25 × |SampleRTT - EstimatedRTT|
```

**TimeoutInterval**:
```
TimeoutInterval = EstimatedRTT + 4 × DevRTT
```

**On Timeout**: `TimeoutInterval = 2 × TimeoutInterval` (exponential backoff)

**Initial Values**: 
- `EstimatedRTT = 1 second`
- `DevRTT = 5 ms` (or first SampleRTT/2)
- `TimeoutInterval = 1 second`

**Karn's Algorithm**: Don't use retransmitted segments for SampleRTT (ambiguous which transmission ACK corresponds to)

### 3.5.4 Reliable Data Transfer

**Sender Events**:
1. **Data from application**: Create segment with seq#, start timer if not running, send
2. **Timeout**: Retransmit oldest unACKed segment, restart timer
3. **ACK received** (y > SendBase): 
   - `SendBase = y` (cumulative ACK)
   - If unACKed segments remain, restart timer; else stop timer

**Fast Retransmit** (3 Duplicate ACKs):
- Receiver sends duplicate ACK when out-of-order segment arrives
- Sender receives 3 dup ACKs → **retransmit missing segment immediately** (before timeout)
- Enter **Fast Recovery**

**Fast Recovery**:
```
ssthresh = cwnd / 2
cwnd = ssthresh + 3 MSS
For each additional dup ACK: cwnd += 1 MSS
On new ACK (covers missing data): cwnd = ssthresh; exit to Congestion Avoidance
```

### 3.5.5 Flow Control

**Problem**: Sender may overwhelm receiver buffer
**Solution**: **Receiver Advertised Window (rwnd)**

```
rwnd = RcvBuffer - (LastByteRcvd - LastByteRead)
```

**Sender Constraint**:
```
LastByteSent - LastByteAcked ≤ min(cwnd, rwnd)
```

**Zero Window**: If rwnd = 0, sender stops sending
- **Zero Window Probe**: Sender sends 1-byte segment periodically to check if window opened
- Prevents deadlock if window update lost

### 3.5.6 TCP Connection Management

#### 3-Way Handshake (Connection Establishment)
```
Client                    Server
  |--- SYN (seq=x) ---->|
  |<-- SYN+ACK (seq=y, ack=x+1) --|
  |--- ACK (seq=x+1, ack=y+1) -->|
```
- Client ISN = x, Server ISN = y (randomized for security)
- SYN consumes 1 sequence number
- Connection established after 3rd packet

#### 4-Way Teardown (Connection Termination)
```
Client                    Server
  |--- FIN (seq=u) ---->|
  |<-- ACK (ack=u+1) ---|
  |<-- FIN (seq=v) ---->|
  |--- ACK (ack=v+1) --->|
```
- Each FIN consumes 1 sequence number
- **TIME_WAIT**: Client waits `2 × MSL` (~2 minutes) after sending final ACK
  - MSL (Maximum Segment Lifetime) ≈ 60 seconds
  - Ensures final ACK received; handles delayed duplicates

**Simultaneous Open/Close**: Both sides send SYN/FIN at same time - handled by state machine

---

## 3.6 Principles of Congestion Control

### 3.6.1 The Causes and Costs of Congestion
**Causes**:
- Multiple senders transmitting too fast for network capacity
- Queue buildup at routers → delay, loss
- Retransmissions of lost packets add more load

**Costs**:
- Large queuing delays
- Packet loss (buffer overflow)
- Wasted work (retransmitting lost packets)
- Wasted bandwidth (packets dropped after traversing part of path)

### 3.6.2 Approaches to Congestion Control
| Approach | Description |
|----------|-------------|
| **End-to-End** | Network provides no explicit feedback; sender infers congestion from loss/delay (TCP) |
| **Network-Assisted** | Routers provide explicit feedback (ECN, source quench) |

---

## 3.7 TCP Congestion Control

### 3.7.1 Classic End-End TCP Congestion Control (Reno)

**State Variables**:
- `cwnd` = congestion window (sender-side limit, in bytes or MSS)
- `ssthresh` = slow start threshold
- `EffectiveWindow = min(cwnd, rwnd)`

#### Slow Start (SS)
- Initial: `cwnd = 1 MSS` (up to 10 MSS per RFC 3390/RFC 6928)
- **Per ACK received**: `cwnd += 1 MSS` (doubles per RTT)
- Exponential growth
- **Exit condition**: `cwnd ≥ ssthresh` → enter Congestion Avoidance

#### Congestion Avoidance (CA)
- **Per RTT**: `cwnd += 1 MSS` (linear growth)
- **Per ACK**: `cwnd += MSS × (MSS / cwnd)` ≈ 1 MSS per RTT
- Additive Increase

#### Loss Reactions
| Event | Action |
|-------|--------|
| **Timeout** | `ssthresh = cwnd/2; cwnd = 1 MSS; enter Slow Start` |
| **3 Dup ACKs** | `ssthresh = cwnd/2; cwnd = ssthresh + 3 MSS; enter Fast Recovery` |

#### Fast Recovery (after 3 dup ACKs)
```
cwnd = ssthresh + 3 MSS
For each additional dup ACK: cwnd += 1 MSS
On new ACK (ack > previous): cwnd = ssthresh; exit to CA
```

**Sawtooth Pattern**: cwnd increases linearly, drops multiplicatively on loss

### 3.7.2 TCP Variants: Tahoe, Reno, CUBIC

| Feature | Tahoe (1988) | Reno (1990) | CUBIC (2008) |
|---------|--------------|-------------|--------------|
| Growth before loss | Slow start, then +1 MSS/RTT | Slow start, then +1 MSS/RTT | Slow start, then cubic in time since last loss |
| On timeout | cwnd = 1 MSS, slow start | cwnd = 1 MSS, slow start | cwnd = 1 MSS, slow start |
| On 3 dup ACKs | cwnd = 1 MSS, slow start | cwnd = ssthresh + 3 (fast recovery), then ssthresh | cwnd × 0.7 during fast recovery |
| Fast recovery | No | Yes | Yes |
| Reference | First congestion control that worked | Textbook model | Default in Linux/Windows/macOS (RFC 9438) |

**CUBIC Details**:
- Function: `cwnd = C × (t - K)³ + W_max`
- `t` = time since last congestion event
- `K` = cubic root of `(W_max × (1 - β) / C)`
- `β = 0.7` (multiplicative decrease factor)
- Less RTT-dependent; more aggressive after loss
- Under Reno: 20ms flow grows 10× faster than 200ms flow
- Under CUBIC: both follow same time-based curve

### 3.7.3 Network-Assisted Explicit Congestion Notification (ECN)

**IP Header ECN bits** (2 bits in ToS field):
| Codepoint | Meaning |
|-----------|---------|
| 00 | Not ECN-Capable Transport (Not-ECT) |
| 01 | ECN-Capable Transport (ECT1) |
| 10 | ECN-Capable Transport (ECT0) |
| 11 | Congestion Experienced (CE) |

**Router Action**: When queue exceeds threshold, mark packet CE (instead of dropping)
**Sender Reaction to CE**:
```
cwnd = cwnd / 2
ssthresh = cwnd
Set CWR (Congestion Window Reduced) flag in TCP header
```
**Receiver**: Echoes CE back via ECE flag in TCP ACK

**History**: Specified in 1999, took two decades for real deployment. Cost: feedback still costs full RTT, network modification required.

### 3.7.4 Fairness
**Fair Share**: `R / K` for K flows sharing bottleneck rate R
**AIMD Convergence**: Additive Increase (1 MSS/RTT), Multiplicative Decrease (÷2) → converges to fairness

---

## 3.8 Evolution of Transport-Layer Functionality
- **TCP**: Monolithic in kernel; hard to evolve
- **QUIC**: User-space (UDP); rapid evolution; includes TLS 1.3
- **HTTP/3 over QUIC**: Stream-level multiplexing; 0-RTT; connection migration

---

## Key Formulas (Chapter 3)

| Formula | Equation |
|---------|----------|
| UDP Checksum | 1's complement sum of 16-bit words + pseudo-header |
| Stop-and-Wait Utilization | `U = (L/R) / (RTT + L/R)` |
| Pipelined Utilization | `U = N × (L/R) / (RTT + L/R)` |
| Optimal Window | `N_optimal = 1 + (RTT × R) / L` |
| BDP | `BDP = R × RTT` |
| GBN Window Bound | `N ≤ 2ᵏ - 1` |
| SR Window Bound | `N ≤ 2ᵏ⁻¹` |
| EstimatedRTT | `0.875 × EstRTT + 0.125 × SampleRTT` |
| DevRTT | `0.75 × DevRTT + 0.25 × \|SampleRTT - EstRTT\|` |
| TimeoutInterval | `EstimatedRTT + 4 × DevRTT` |
| rwnd | `RcvBuffer - (LastByteRcvd - LastByteRead)` |
| Sender Constraint | `LastByteSent - LastByteAcked ≤ min(cwnd, rwnd)` |
| MSS | `MSS = MTU - 40` (typically 1460) |
| Slow Start | `cwnd += 1 MSS` per ACK |
| Congestion Avoidance | `cwnd += 1 MSS` per RTT |
| Timeout Reaction | `ssthresh = cwnd/2; cwnd = 1 MSS` |
| 3 Dup ACKs | `ssthresh = cwnd/2; cwnd = ssthresh + 3 MSS` |
| Avg cwnd (steady) | `cwnd_avg = 0.75 × W` (W = cwnd at loss) |
| Macroscopic Throughput | `Throughput = 0.75 × W / RTT` |
| Loss Rate Model (Padhye) | `Throughput ≈ 1.22 × MSS / (RTT × √L)` |
| Mathis Bound | `Throughput ≤ MSS / (RTT × √L)` |
| TIME_WAIT | `2 × MSL ≈ 2 minutes` |

---

## Complete Questions, Examples, and MCQs from Slides and Textbook

### Numerical Problems (Exam Practice)

**Q1. Stop-and-Wait Utilization**: L=1000 bits, R=1 Mbps, RTT=20ms
- U = (1000/1e6) / (0.02 + 1000/1e6) = 0.001 / 0.021 = 0.0476 = 4.76%

**Q2. GBN Transmissions (from slides)**: N=10, every 5th packet lost
- Round 1: Send 1-10, lose 5,10 → ACK 4, timeout → 18 total transmissions

**Q3. SR Transmissions (from slides)**: N=10, every 5th packet lost
- Round 1: 10 tx, Round 2: 2 tx = **12 total** (only retransmit lost packets)

**Q4. RTT Estimation**: SampleRTT sequence: 100ms, 120ms, 110ms, 90ms, 130ms
- Start: EstRTT=1000ms, DevRTT=5ms
- After 1st: EstRTT=0.875×1000+0.125×100=887.5, DevRTT=0.75×5+0.25×|100-1000|=230
- Continue...

**Q5. TCP Throughput (Padhye)**: MSS=1460, RTT=100ms, L=0.001 (0.1% loss)
- Throughput ≈ 1.22 × 1460 / (0.1 × √0.001) = 1781 / 0.00316 = 563 Kbps

**Q6. Window Size Bounds**: k=4 bits sequence numbers
- GBN max N = 2⁴ - 1 = 15
- SR max N = 2³ = 8

**Q7. Congestion Window Evolution**: Initial cwnd=1 MSS, ssthresh=8 MSS
- Round 1: 1, 2: 2, 3: 4, 4: 8 → hit ssthresh, enter CA
- Round 5: 9, 6: 10, 7: 11, 8: 12
- Loss at round 8 via 3 dup ACKs: ssthresh=6, cwnd=9 (Reno) or cwnd=1 (Tahoe)

### Review Questions

1. **Difference between GBN and SR?**
   - GBN: cumulative ACK, retransmit all from base on timeout
   - SR: individual ACK, per-packet timer, retransmit only timed-out packet

2. **Why is SR window size ≤ 2ᵏ⁻¹?**
   - Prevents overlap between sender and receiver windows (2N ≤ 2ᵏ)

3. **TCP sequence number = ?**
   - Byte number of FIRST data byte in segment

4. **TCP ACK number = ?**
   - Next expected byte (cumulative)

5. **How does TCP flow control work?**
   - Receiver advertises rwnd = buffer - unread data
   - Sender limits unACKed data to min(cwnd, rwnd)

6. **Slow Start vs Congestion Avoidance?**
   - SS: exponential growth (per ACK: cwnd += 1 MSS)
   - CA: linear growth (per RTT: cwnd += 1 MSS)

7. **Fast Retransmit trigger?**
   - 3 duplicate ACKs

8. **Timeout vs 3 Dup ACKs reaction?**
   - Timeout: cwnd = 1 MSS, Slow Start
   - 3 Dup ACKs: cwnd = ssthresh + 3 MSS, Fast Recovery

9. **What is BBR?**
   - Model-based congestion control using BW and RTT_min estimates

10. **What is ECN?**
    - Router marks packets CE instead of dropping; sender reacts by halving cwnd

---

## Multiple Choice Questions (from Slides)

**Q1. Congestion vs Flow Control:**
- Congestion: too many senders, sending too fast for network
- Flow control: one sender too fast for one receiver

**Q2. Causes/Costs of Congestion - Scenario 1 (Infinite buffers):**
- As λin approaches R/2: throughput λout approaches R/2, delay → ∞

**Q3. Causes/Costs of Congestion - Scenario 2 (Finite buffers, retransmissions):**
- Idealization 1 (perfect knowledge): throughput = λin, capped at R/2
- Idealization 2 (resends only if known lost): throughput < R/2 (wasted retransmissions)
- Realistic (unneeded duplicates): further decreases throughput

**Q4. Scenario 3 (Multi-hop, 4 senders):**
- As λin' increases, all arriving blue pkts at upper queue are dropped → blue throughput → 0
- Another cost: when packet dropped, upstream capacity/buffering wasted

**Q5. Congestion Control Approaches:**
- End-end: no explicit feedback, inferred from loss/delay (TCP)
- Network-assisted: routers provide explicit feedback (ECN, ATM, DECbit)

**Q5. ECN Steps:**
1. Router congested → sets CE bit in IP ToS field (2 bits), packet still delivered
2. Receiver sees CE → sets ECE flag in TCP ACK
3. Sender sees ECE → halves cwnd, sets CWR flag
4. All three must support ECN

**Q6. TCP Sender Behavior:**
- Roughly: send cwnd bytes, wait RTT for ACKs, then send more
- TCP rate ~ cwnd bytes/sec / RTT
- LastByteSent - LastByteAcked < cwnd (also min(cwnd, rwnd))

**Q7. TCP Congestion Control Guiding Principles:**
- Lost segment → congestion → decrease rate
- Acknowledged segment → network delivering → increase rate
- Bandwidth probing

**Q8. AIMD:**
- Additive Increase: +1 MSS per RTT
- Multiplicative Decrease: cut rate in half at each loss event
- Optimizes congested flow rates network-wide, desirable stability

**Q9. Slow Start:**
- Initially cwnd = 1 MSS (practice: 10 MSS per RFC 6928)
- Double cwnd every RTT (increment for every ACK)
- Initial rate slow, ramps up exponentially fast

**Q10. Loss Detection/Reaction:**
- Timeout: cwnd = 1 MSS, grows exponentially to threshold, then linearly
- 3 dup ACKs (Reno): dup ACKs indicate network delivering some segments, cwnd cut in half, grows linearly
- Tahoe always sets cwnd = 1 (timeout or 3 dup ACKs)

**Q11. State Machine (from slides):**

| State | On New ACK | On Dup ACK | On DupACK=3 | On Timeout |
|-------|------------|------------|-------------|------------|
| Slow Start | cwnd+=MSS; dupACK=0; transmit | dupACK++ | ssthresh=cwnd/2; cwnd=ssthresh+3; retransmit → fast recovery | ssthresh=cwnd/2; cwnd=1; dupACK=0; retransmit → slow start |
| Congestion Avoidance | cwnd+=MSS×(MSS/cwnd); dupACK=0; transmit | dupACK++ | ssthresh=cwnd/2; cwnd=ssthresh+3; retransmit → fast recovery | ssthresh=cwnd/2; cwnd=1; dupACK=0; retransmit → slow start |
| Fast Recovery | cwnd=ssthresh; dupACK=0 → congestion avoidance | cwnd+=MSS; transmit | — | ssthresh=cwnd/2; cwnd=1; dupACK=0; retransmit → slow start |

**Q12. TCP Variants Comparison:**
- Tahoe: first working congestion control, 1986 collapse solved
- Reno: triple-dup-ACK loss is mild; don't restart from scratch
- CUBIC: +1 MSS/RTT too slow on long, fast paths; default in Linux/Windows/macOS

**Q13. CUBIC Curve:**
- Cube function: steep → flat → steep
- Flat point at W_max
- K = time to return to W_max (further drop → further K)
- Time-based, not ACK-based (RTT-fair)

---

## Textbook End-of-Chapter Problems (Chapter 3)

**P1.** Explain the difference between multiplexing and demultiplexing in transport layer.
**P2.** Calculate UDP checksum for given data (with pseudo-header).
**P3.** Trace rdt 3.0 protocol for a scenario with packet loss and corruption.
**P4.** Compare GBN and SR for N=4, k=3, with packet 2 lost.
**P5.** Draw TCP segment structure and explain each field.
**P6.** Given SampleRTT values, compute EstimatedRTT, DevRTT, TimeoutInterval.
**P7.** Explain TCP 3-way handshake and 4-way teardown with sequence numbers.
**P8.** Describe TCP flow control with rwnd calculation example.
**P9.** Trace TCP congestion control: slow start, congestion avoidance, fast recovery for given loss pattern.
**P10.** Compare Tahoe, Reno, and CUBIC congestion control algorithms.
**P11.** Explain ECN operation and why it took decades to deploy.
**P12.** Prove AIMD converges to fairness for two competing flows.
**P13.** Calculate throughput using Padhye formula for given MSS, RTT, loss rate.
**P14.** Describe QUIC advantages over TCP+TLS.
**P15.** What is the count-to-infinity problem in distance vector routing? How is it solved?

---

## Review Questions

1. **Difference between GBN and SR?**
   - GBN: cumulative ACK, retransmit all from base on timeout
   - SR: individual ACK, per-packet timer, retransmit only timed-out packet

2. **Why is SR window size ≤ 2ᵏ⁻¹?**
   - Prevents overlap between sender and receiver windows (2N ≤ 2ᵏ)

3. **TCP sequence number = ?**
   - Byte number of FIRST data byte in segment

4. **TCP ACK number = ?**
   - Next expected byte (cumulative)

5. **How does TCP flow control work?**
   - Receiver advertises rwnd = buffer - unread data
   - Sender limits unACKed data to min(cwnd, rwnd)

6. **Slow Start vs Congestion Avoidance?**
   - SS: exponential growth (per ACK: cwnd += 1 MSS)
   - CA: linear growth (per RTT: cwnd += 1 MSS)

7. **Fast Retransmit trigger?**
   - 3 duplicate ACKs

8. **Timeout vs 3 Dup ACKs reaction?**
   - Timeout: cwnd = 1 MSS, Slow Start
   - 3 Dup ACKs: cwnd = ssthresh + 3 MSS, Fast Recovery

9. **What is BBR?**
   - Model-based congestion control using BW and RTT_min estimates

10. **What is ECN?**
    - Router marks packets CE instead of dropping; sender reacts by halving cwnd
