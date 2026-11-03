# Computer Networks (UE25CS243A) — Unit 4

## Link Layer & LAN

**Course**: UE25CS243A | **Semester**: III (Aug-Dec 2026) | **Credits**: 4
**Textbook**: Kurose & Ross, *Computer Networking: A Top-Down Approach*, 9th Edition (2026)
**Chapter**: 6 | **Hours**: 14 | **Evaluation**: ISA-2 (40 marks → 15%)

---

## 📚 Unit Overview

| Topic | Section | Key Concepts |
|-------|---------|--------------|
| Link Layer Services | 6.1 | Framing, link access, MAC addressing, reliable delivery, error detection/correction, flow control, half/full duplex |
| Error Detection | 6.2 | Parity (1-bit, 2D), Internet checksum, CRC (polynomial) |
| Multiple Access | 6.3 | CSMA/CD (Ethernet), CSMA/CA (WiFi), TDMA/FDMA/CDMA, binary exponential backoff |
| Switched LANs | 6.4 | MAC addresses, ARP, Ethernet frames, switches (self-learning, forwarding) |
| VLANs | 6.5 | 802.1Q tag (4 bytes, 12-bit VLAN ID), access/trunk ports, inter-VLAN routing |
| A Day in the Life | 6.6 | DHCP → ARP → DNS → TCP handshake → HTTP → link layer encapsulation |
| Physical Layer | 6.7 | NRZ, Manchester, 4B/5B, 8B/10B; twisted pair, coax, fiber, wireless |
| Wireless LANs | 6.8 | 802.11 architecture (BSS/ESS), CSMA/CA, RTS/CTS, hidden/exposed terminal |

---

## 📖 Quick Navigation

- [Complete Unit 4 Notes](unit4_complete.md)

---

## ✅ Study Checklist (ISA-2)

### Link Layer Fundamentals
- [ ] Services: framing, link access, MAC addressing (48-bit), reliable delivery (rare on wired), error detection/correction, flow control
- [ ] Implementation: NIC or on-chip, hardware/software/firmware
- [ ] Encapsulation: datagram → frame (header + trailer)

### Error Detection & Correction
- [ ] Single-bit parity: even parity, detects odd flips only
- [ ] 2D parity: row + column, detects AND corrects single-bit errors
- [ ] Internet checksum: 1's complement sum of 16-bit words, weak (misses compensating errors)
- [ ] CRC: D×2ʳ mod G, detects all burst errors < r+1 bits, Ethernet uses CRC-32

### Multiple Access Protocols
- [ ] Channel partitioning: TDMA (time slots), FDMA (frequency), CDMA (codes)
- [ ] Random access: ALOHA, slotted ALOHA, CSMA, CSMA/CD, CSMA/CA
- [ ] CSMA/CD (Ethernet): listen before transmit, detect collision → abort, binary exponential backoff (K ∈ {0..2ⁿ⁻¹}, wait K×512 bit times)
- [ ] CSMA/CA (WiFi): DIFS → random backoff → transmit → wait ACK → retry on failure
- [ ] Why no CD in modern Ethernet: switched full-duplex = dedicated channels = no collisions
- [ ] WiFi still shared → CSMA/CA with RTS/CTS for hidden terminal

### Ethernet & Switches
- [ ] Frame: preamble (8B) | dst MAC (6B) | src MAC (6B) | type (2B) | data (46-1500B) | CRC (4B)
- [ ] Min frame: 64 bytes (512 bits = collision budget), Max: 1518 bytes
- [ ] Unreliable, connectionless: no ACKs, dropped frames recovered by TCP
- [ ] Switch: self-learning (src MAC → port on arrival), flooding if dest unknown, forwarding table with TTL (~60s)
- [ ] Hub vs Switch: hub = 1 collision domain, switch = per-port collision domain (full duplex)

### VLANs
- [ ] 802.1Q tag: 4 bytes after src MAC (TPID=0x8100, priority 3b, DEI 1b, VLAN ID 12b = 4094 usable)
- [ ] Access port: 1 VLAN, untagged frames to/from device
- [ ] Trunk port: multiple VLANs, tagged frames
- [ ] Native VLAN: 1 VLAN crosses trunk untagged, both ends must agree
- [ ] VLAN-aware forwarding: lookup (VLAN, dest MAC), flood only within VLAN + trunks
- [ ] Inter-VLAN routing: router or L3 switch, each VLAN = separate IP subnet

### ARP
- [ ] Broadcast query "Who has IP X? Tell IP Y" → unicast reply "IP X is at MAC Z"
- [ ] ARP table: IP/MAC mappings with TTL (minutes)
- [ ] Both requester and responder update their tables

### Physical Layer
- [ ] Encoding: NRZ (low=0, high=1), Manchester (transition=bit, self-clocking), 4B/5B (100 Mbps), 8B/10B (Gbps)
- [ ] Media: twisted pair (Cat5e 1G, Cat6 10G, 100m), coax (cable TV), fiber (SMF/MMF, km, immune EMI), wireless (radio, half-duplex)

### Wireless LANs (802.11)
- [ ] BSS: hosts + AP; ESS: multiple BSSs + distribution system
- [ ] Channels: 2.4 GHz (11), 5 GHz, 6 GHz (WiFi 6E)
- [ ] Association: scan → select AP → authenticate → DHCP
- [ ] CSMA/CA: DIFS → random backoff → transmit → SIFS → ACK
- [ ] RTS/CTS: reserve channel, solve hidden terminal
- [ ] Hidden terminal: A and C can't hear each other, both transmit to B → collision
- [ ] Exposed terminal: C hears B → defers unnecessarily
- [ ] Standards: 802.11b (11M), g (54M), n (600M), ac (3.47G), ax (14G), be (46G)

---

## 🧠 Key Formulas (Memorize)

| Formula | Equation |
|---------|----------|
| CRC | Remainder of D × 2ʳ ÷ G (mod 2) |
| Ethernet Min Frame | 64 bytes = 512 bits |
| Ethernet Max Frame | 1518 bytes |
| Binary Exponential Backoff | Wait K × 512 bit times, K ∈ {0, ..., 2ⁿ⁻¹} |
| CSMA/CA Backoff | Wait random slots × slot_time after DIFS |
| NAV (Virtual Carrier) | Duration field in RTS/CTS/Data frames |

---

## ❓ Quick Self-Test

1. **Link layer services?**
2. **Where is link layer implemented?**
3. **Parity vs CRC?**
4. **Internet checksum?**
5. **CSMA/CD vs CSMA/CA?**
6. **Why no collision detection in modern Ethernet?**
7. **MAC vs IP address?**
8. **ARP operation?**
9. **Switch self-learning?**
10. **VLAN purpose?**
11. **Access vs trunk port?**
12. **Inter-VLAN routing?**
13. **802.11 CSMA/CA?**
14. **Hidden terminal problem?**
15. **Physical layer encoding?**

---

## 🎯 Exam-Relevant MCQ Patterns

- Numerical: CRC calculation for given data and generator polynomial
- Numerical: Ethernet min/max frame size, collision domain counting
- Conceptual: CSMA/CD vs CSMA/CA scenarios
- Conceptual: Switch forwarding decision (flood vs forward vs drop)
- Conceptual: VLAN tag interpretation, access vs trunk behavior
- Conceptual: 802.11 frame exchange (RTS/CTS/DATA/ACK)
- Code: Identify encoding from waveform description

---

*Unit 4 covers Chapter 6. ISA-2 evaluates Units 3 & 4 (40 marks → 15%).*