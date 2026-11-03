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