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