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
- Initial: `cwnd = 1 MSS` (up to 10 MSS per RFC 3390)
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

### 3.7.2 Recent End-End TCP Congestion Control Algorithms

#### CUBIC (Default in Linux since 2.6.19)
- **Function**: `cwnd = C × (t - K)³ + W_max`
- `t` = time since last congestion event
- `K` = cubic root of `(W_max × (1 - β) / C)`
- `β = 0.7` (multiplicative decrease factor)
- Less RTT-dependent; more aggressive after loss

#### TCP Vegas
- **Delay-based**: Measures `Expected = cwnd/RTT_min`, `Actual = cwnd/RTT_curr`
- If `Actual < Expected - α`: increase cwnd
- If `Actual > Expected + β`: decrease cwnd
- Prevents congestion before loss occurs

#### BBR (Bottleneck Bandwidth and Round-trip propagation time) - Google
- **Model-based**: Estimates `BW` (bottleneck bandwidth) and `RTT_min`
- **BDP = BW × RTT_min**
- **Pacing rate = BDP × gain** (gain cycles: 1.25, 0.75, 1, 1...)
- **cwnd = BDP + headroom**
- Does not react to loss; reacts to bandwidth/delay measurements

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

### 3.7.4 Fairness
**Fair Share**: `R / K` for K flows sharing bottleneck rate R
**AIMD Convergence**: Additive Increase (1 MSS/RTT), Multiplicative Decrease (÷2) → converges to fairness

---

## 3.8 Evolution of Transport-Layer Functionality
- **TCP**: Monolithic in kernel; hard to evolve
- **QUIC**: User-space (UDP); rapid evolution; includes TLS 1.3
- **HTTP/3 over QUIC**: Stream-level multiplexing; 0-RTT; connection migration

---

## 3.9 Summary

### Key Concepts
1. **Transport services**: Process-to-process delivery via ports
2. **Multiplexing/Demultiplexing**: UDP (2-tuple), TCP (4-tuple)
3. **UDP**: Minimal, 8-byte header, checksum
4. **RDT principles**: ACK/NAK, sequence numbers, timers, pipelining
5. **GBN vs SR**: GBN = cumulative ACK, retransmit all; SR = selective ACK, retransmit one
6. **TCP**: Reliable byte stream, flow control (rwnd), congestion control (cwnd)
7. **RTT estimation**: EWMA for EstimatedRTT and DevRTT; Timeout = EstRTT + 4×DevRTT
8. **TCP Congestion Control**: Slow Start → CA → Fast Recovery; AIMD
9. **Modern variants**: CUBIC, Vegas, BBR
10. **ECN**: Explicit congestion marking

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