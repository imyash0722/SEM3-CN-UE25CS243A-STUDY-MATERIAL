# Complete Formulae Sheet — Computer Networks (UE25CS243A)
## Units 1-4 (Chapters 1-6) — Kurose & Ross 9th Edition

---

# UNIT 1: Computer Networks & Internet + Application Layer (Chapters 1–2)

---

## Chapter 1: Network Fundamentals

### Delay Components
| Formula | Equation |
|---------|----------|
| **Transmission Delay** | `d_trans = L / R` |
| **Propagation Delay** | `d_prop = d / s` |
| **Processing Delay** | `d_proc` (typically µs) |
| **Queuing Delay** | `d_queue` (depends on traffic intensity) |
| **Total Nodal Delay** | `d_nodal = d_proc + d_queue + d_trans + d_prop` |
| **End-to-End (N links, no queue/proc)** | `d_end-end = N × (d_trans + d_prop)` |
| **General End-to-End** | `Σ(d_proc_i + d_queue_i + d_trans_i + d_prop_i)` |

### Queuing Theory
| Formula | Equation |
|---------|----------|
| **Traffic Intensity** | `ρ = (L × a) / R = λL / R` |
| **Stability** | `ρ ≤ 1` (if ρ > 1 → infinite queue) |
| **Avg Queuing Delay (M/M/1)** | `d_queue = (L/R) × (ρ / (1-ρ))` |

### Throughput
| Formula | Equation |
|---------|----------|
| **Instantaneous** | `Throughput_inst = receiver bit rate` |
| **Average (file transfer)** | `Throughput_avg = F / T` |
| **Bottleneck (no cross traffic)** | `Throughput = min(R₁, R₂, ..., R_N)` |
| **M flows sharing bottleneck R** | `Throughput_per_flow = R / M` |

### Store-and-Forward
| Formula | Equation |
|---------|----------|
| **Single packet, N links** | `d = N × L / R` |
| **P packets back-to-back, N links** | `d = (N + P - 1) × L / R` |

---

## Chapter 2: Application Layer

### HTTP Performance
| Scenario | Total Time |
|----------|------------|
| **Non-persistent (K objects)** | `K × (2×RTT + L/R)` |
| **Non-persistent (P parallel)** | `ceil(K/P) × (2×RTT + L/R)` |
| **Persistent (no pipelining)** | `2×RTT + K×L/R` |
| **Persistent + Pipelining** | `2×RTT + K×L/R` (requests back-to-back) |
| **HTTP/2 / HTTP/3** | `RTT_handshake + RTT_req/resp + L/R` |

### DNS
- Messages for 3-level lookup: **8 messages** (4 queries + 4 replies)
- TTL: typically **2 days = 172,800 seconds**

---

# UNIT 2: Transport Layer (Chapter 3)

---

## 3.1 UDP Checksum (Internet Checksum)

**Sender (1's complement):**
```
1. Sum all 16-bit words (header + data + pseudo-header)
2. Add wrap-around carry to LSB
3. Checksum = ~Sum (flip all bits)
```

**Receiver:**
```
Total = Sum(all 16-bit words) + Checksum
If Total == 0xFFFF → No error
Else → Error detected
```

**Pseudo-header:** `SrcIP(32) | DstIP(32) | Zero(8) | Protocol(8) | Length(16)`

---

## 3.2 RDT Performance

### Stop-and-Wait
```
U = (L/R) / (RTT + L/R)
Throughput = L / (RTT + L/R)
```

### Pipelined (Window N)
```
U = min(1, N × (L/R) / (RTT + L/R))
N_optimal = 1 + (RTT × R) / L
BDP = R × RTT
Packets_in_flight = (R × RTT) / L
```

---

## 3.3 Go-Back-N (GBN)

| Constraint | Formula |
|------------|---------|
| **Window Bound** | `N ≤ 2ᵏ - 1` (k = seq num bits) |
| **Sender Window** | `base` = oldest unACKed, `nextseqnum` = next to send |
| **On Timeout** | Retransmit ALL packets `[base, nextseqnum-1]` |
| **Utilization** | `U = N × (L/R) / (RTT + L/R)` (if N < N_optimal) |

**18-Transmission Problem (N=10, every 5th lost):**
- Round 1: 10 tx, Round 2: 6 tx, Round 3: 2 tx = **18 total**

---

## 3.4 Selective Repeat (SR)

| Constraint | Formula |
|------------|---------|
| **Window Bound** | `N ≤ 2ᵏ⁻¹` (Proof: 2N ≤ 2ᵏ → N ≤ 2ᵏ⁻¹) |
| **Sender Window** | `[base, base+N-1]`, per-packet timers |
| **On Timeout(n)** | Retransmit **only packet n** |
| **Receiver** | Buffers out-of-order in `[rcv_base, rcv_base+N-1]` |
| **Utilization** | Same as GBN but fewer retransmissions |

**12-Transmission Problem (same conditions):**
- Round 1: 10 tx, Round 2: 2 tx = **12 total**

---

## 3.5 TCP Fundamentals

| Concept | Formula |
|---------|---------|
| **Sequence Number** | Byte number of FIRST data byte in segment |
| **Acknowledgment Number** | Next expected byte (cumulative) |
| **MSS** | `MSS = MTU - 40` (typical: 1500 - 40 = 1460 bytes) |

---

## 3.6 RTT Estimation & Timeout (RFC 6298)

| Variable | Formula |
|----------|---------|
| **EstimatedRTT (α=0.125)** | `EstRTT = 0.875 × EstRTT + 0.125 × SampleRTT` |
| **DevRTT (β=0.25)** | `DevRTT = 0.75 × DevRTT + 0.25 × \|SampleRTT - EstRTT\|` |
| **TimeoutInterval** | `Timeout = EstRTT + 4 × DevRTT` |
| **On Timeout** | `Timeout = 2 × Timeout` (exponential backoff) |
| **Initial Values** | `EstRTT = 1s`, `DevRTT = 5ms`, `Timeout = 1s` |

---

## 3.7 TCP Reliable Transfer

### Sender Events
| Event | Action |
|-------|--------|
| Data from app | Create segment, start timer if not running, send |
| Timeout | Retransmit oldest unACKed, restart timer |
| ACK (y > SendBase) | `SendBase = y`; restart timer if unACKed remain |

### Fast Retransmit (3 Dup ACKs)
```
Retransmit missing segment immediately
ssthresh = cwnd/2
cwnd = ssthresh + 3 MSS
Enter Fast Recovery
```

---

## 3.8 TCP Flow Control

| Formula | Equation |
|---------|----------|
| **rwnd** | `rwnd = RcvBuffer - (LastByteRcvd - LastByteRead)` |
| **Sender Constraint** | `LastByteSent - LastByteAcked ≤ min(cwnd, rwnd)` |
| **Zero Window Probe** | Sender sends 1-byte probe periodically |

---

## 3.9 TCP Connection Management

| Phase | Packets |
|-------|---------|
| **3-Way Handshake** | SYN(x) → SYN+ACK(y, x+1) → ACK(x+1, y+1) |
| **4-Way Teardown** | FIN(x) → ACK(x+1) → FIN(y) → ACK(y+1) |
| **TIME_WAIT** | `2 × MSL ≈ 2 minutes` (MSL ≈ 60s) |

---

## 3.10 TCP Congestion Control

### State Variables
- `cwnd` = congestion window (sender limit)
- `ssthresh` = slow start threshold
- `EffectiveWindow = min(cwnd, rwnd)`

### Slow Start
```
cwnd = 1 MSS (up to 10 MSS per RFC 3390)
Per ACK: cwnd += 1 MSS  (doubles per RTT)
Exit: cwnd ≥ ssthresh → Congestion Avoidance
```

### Congestion Avoidance
```
Per RTT: cwnd += 1 MSS (linear)
Per ACK: cwnd += MSS × (MSS / cwnd)
```

### Loss Reactions

| Event | Action |
|-------|--------|
| **Timeout** | `ssthresh = cwnd/2; cwnd = 1 MSS; Slow Start` |
| **3 Dup ACKs** | `ssthresh = cwnd/2; cwnd = ssthresh + 3 MSS; Fast Recovery` |

### Fast Recovery
```
On each dup ACK: cwnd += 1 MSS
On new ACK: cwnd = ssthresh; exit to Congestion Avoidance
```

---

## 3.10.1 Macroscopic TCP Throughput

| Model | Formula |
|-------|---------|
| **Avg cwnd (steady state)** | `cwnd_avg = 0.75 × W` (W = cwnd at loss) |
| **Avg Throughput** | `Throughput = 0.75 × W / RTT` |
| **Loss Rate (Padhye)** | `Throughput ≈ 1.22 × MSS / (RTT × √L)` |
| **Mathis Bound** | `Throughput ≤ MSS / (RTT × √L)` |

---

## 3.10.2 Fairness

| Concept | Formula |
|---------|---------|
| **Fair Share (K flows, bottleneck R)** | `R / K` |
| **AIMD Convergence** | Additive Increase (1 MSS/RTT), Multiplicative Decrease (÷2) |

---

## 3.11 Modern TCP Variants

| Variant | Key Formula |
|---------|-------------|
| **CUBIC** | `cwnd = C × (t - K)³ + W_max` |
| **Vegas** | `Expected = cwnd/RTT_min; Actual = cwnd/RTT_curr` |
| **BBR** | `BDP = BW × RTT_min; Pacing = BDP × gain` |

---

## 3.12 ECN (Explicit Congestion Notification)

| ECN Bits (IP) | Meaning |
|---------------|---------|
| `10` (ECT0) | ECN-Capable |
| `01` (ECT1) | ECN-Capable |
| `11` (CE) | Congestion Experienced |

**TCP Response to CE:**
```
cwnd = cwnd/2; ssthresh = cwnd; Set CWR bit
```

---

## 3.13 QUIC / HTTP/3

| Metric | Value |
|--------|-------|
| **TCP+TLS 1.3 Handshake** | 2 RTT |
| **QUIC+TLS 1.3** | 1 RTT |
| **QUIC 0-RTT Resume** | 0 RTT |
| **Connection Migration** | Connection ID survives IP change |
| **Stream Independence** | Lost packet blocks only that stream |

---

# UNIT 3: Network Layer (Chapters 4–5)

---

## IPv4

| Formula | Equation |
|---------|----------|
| **Header Checksum** | 1's complement sum of 16-bit header words |
| **Longest Prefix Match** | Choose entry with longest matching prefix |
| **Subnet Address** | `IP AND Subnet Mask` |
| **Broadcast Address** | `Subnet Address OR (NOT Subnet Mask)` |
| **Hosts per Subnet** | `2^(32 - prefix_length) - 2` |

---

## Routing Algorithms

### Dijkstra (Link State)
```
D(v) = min( D(v), D(w) + c(w,v) )
```

### Bellman-Ford (Distance Vector)
```
Dx(y) = minᵥ { c(x,v) + Dᵥ(y) }
```

---

## IPv6

- Address: 128-bit (eight 16-bit hextets, colon-separated)
- Compression: `::` replaces one contiguous all-zero block
- No checksum, no fragmentation, no options in base header
- Flow label: 20 bits for "flow" identification

---

## ICMP

| Type | Code | Description |
|------|------|-------------|
| 0 | 0 | Echo reply (ping) |
| 3 | 0 | Dest network unreachable |
| 3 | 1 | Dest host unreachable |
| 3 | 3 | Dest port unreachable |
| 8 | 0 | Echo request (ping) |
| 11 | 0 | TTL expired (traceroute) |

---

## DHCP (DORA)

| Step | Message | Src | Dst |
|------|---------|-----|-----|
| 1 | Discover | 0.0.0.0:68 | 255.255.255.255:67 |
| 2 | Offer | Server:67 | 255.255.255.255:68 |
| 3 | Request | 0.0.0.0:68 | 255.255.255.255:67 |
| 4 | ACK | Server:67 | 255.255.255.255:68 |

---

# UNIT 4: Link Layer & LAN (Chapter 6)

---

## Error Detection

### Parity
| Type | Capability |
|------|------------|
| Single bit | Detect single bit error |
| Two-dimensional | Detect AND correct single bit error |

### Internet Checksum
- 1's complement sum of 16-bit words
- Weak: misses compensating errors across words

### CRC (Cyclic Redundancy Check)
| Parameter | Description |
|-----------|-------------|
| **D** | Data bits (binary number) |
| **G** | Generator polynomial (r+1 bits) |
| **R** | r CRC bits (remainder) |
| **Transmitted** | `<D,R>` exactly divisible by G (mod 2) |
| **Detection** | All burst errors < r+1 bits |

---

## Multiple Access

### Binary Exponential Backoff (Ethernet CSMA/CD)
```
After n collisions: choose K ∈ {0, 1, ..., 2ⁿ⁻¹}
Wait K × 512 bit times
```

### CSMA/CA (802.11)
```
DIFS → random backoff slots → transmit → wait ACK → retry on failure
```

---

## Ethernet

| Parameter | Value |
|-----------|-------|
| **Min Frame** | 64 bytes = 512 bits (collision budget) |
| **Max Frame** | 1518 bytes (1500 MTU + 18 header/CRC) |
| **Preamble** | 8 bytes (7×10101010 + 10101011) |
| **Addresses** | 6 bytes src + 6 bytes dst |
| **Type** | 2 bytes (0x0800 = IP) |
| **CRC** | 4 bytes (CRC-32) |

---

## Switches

| Parameter | Value |
|-----------|-------|
| **Learning** | On frame arrival: record (src MAC, incoming port) |
| **Aging** | TTL ~60 seconds |
| **Forwarding** | Lookup dest MAC: known → forward; unknown → flood |
| **Flood** | All ports except arriving port |

---

## VLANs (802.1Q)

| Field | Size |
|-------|------|
| **Tag Marker** | 2 bytes (0x8100) |
| **Priority** | 3 bits (0-7) |
| **Drop Eligible** | 1 bit |
| **VLAN ID** | 12 bits (4,094 usable) |
| **Frame Size** | 1518 → 1522 bytes |

---

## ARP

| Message | Src MAC | Dst MAC | Payload |
|---------|---------|---------|---------|
| **Request** | Sender MAC | FF:FF:FF:FF:FF:FF | "Who has IP X? Tell IP Y" |
| **Reply** | Target MAC | Sender MAC | "IP X is at MAC Z" |

- ARP table TTL: typically minutes
- Broadcast query → unicast reply

---

## 802.11 Wireless

### CSMA/CA Timing
| Interval | Purpose |
|----------|---------|
| **DIFS** | Distributed Inter-Frame Space (before backoff) |
| **SIFS** | Short IFS (before ACK/CTS) |
| **Slot Time** | Backoff granularity |
| **NAV** | Virtual carrier sense (from Duration field) |

### Frame Addresses (up to 4)
| Addr1 | Addr2 | Addr3 | Addr4 |
|-------|-------|-------|-------|
| Receiver | Transmitter | BSSID / Dest | Source (WDS) |

### Hidden/Exposed Terminal
- **Hidden**: A and C can't hear each other → RTS/CTS reserves channel
- **Exposed**: C hears B → defers unnecessarily

---

## Physical Layer Encoding

| Encoding | Description |
|----------|-------------|
| **NRZ** | Low=0, High=1 |
| **Manchester** | Low→High=1, High→Low=0 (self-clocking) |
| **4B/5B** | 4 data bits → 5 code bits (100 Mbps) |
| **8B/10B** | 8 data bits → 10 code bits (Gbps) |

---

## QUICK REFERENCE CARD (Exam Essentials)

| Formula | Equation |
|---------|----------|
| **Transmission Delay** | `d_trans = L / R` |
| **Propagation Delay** | `d_prop = d / s` |
| **End-to-End (N links)** | `N × (d_trans + d_prop)` |
| **Traffic Intensity** | `ρ = (L × a) / R` |
| **Stop-and-Wait Utilization** | `U = (L/R) / (RTT + L/R)` |
| **Pipelined Utilization** | `U = N × (L/R) / (RTT + L/R)` |
| **GBN Window Bound** | `N ≤ 2ᵏ - 1` |
| **SR Window Bound** | `N ≤ 2ᵏ⁻¹` |
| **EstimatedRTT** | `0.875 × EstRTT + 0.125 × SampleRTT` |
| **DevRTT** | `0.75 × DevRTT + 0.25 × \|SampleRTT - EstRTT\|` |
| **TimeoutInterval** | `EstimatedRTT + 4 × DevRTT` |
| **rwnd** | `RcvBuffer - (LastByteRcvd - LastByteRead)` |
| **Sender Constraint** | `LastByteSent - LastByteAcked ≤ min(cwnd, rwnd)` |
| **Slow Start** | `cwnd += 1 MSS` per ACK |
| **Congestion Avoidance** | `cwnd += 1 MSS` per RTT |
| **Timeout Reaction** | `ssthresh = cwnd/2; cwnd = 1 MSS` |
| **3 Dup ACKs** | `ssthresh = cwnd/2; cwnd = ssthresh + 3 MSS` |
| **Macroscopic Throughput** | `0.75 × W / RTT` |
| **Loss Rate Model** | `1.22 × MSS / (RTT × √L)` |
| **TIME_WAIT** | `2 × MSL ≈ 2 minutes` |

---

*End of Formulae Sheet — Covers Chapters 1–6 (Units 1–4)*