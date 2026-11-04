# Unit 1: Computer Networks and the Internet + Application Layer

## Overview
This unit covers Chapters 1-2 of Kurose & Ross (9th Edition):
- Chapter 1: Computer Networks and the Internet
- Chapter 2: Application Layer

**Course Hours**: 14 hours

---

## 1.1 What Is the Internet?

### A Nuts-and-Bolts Description
The Internet is a **global network of networks** - a complex infrastructure consisting of:
- **End systems (hosts)**: Computers, smartphones, servers, IoT devices (41+ billion IoT devices by 2027)
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

**NIXI (National Internet Exchange of India)**: Nonprofit under MeitY, ~77 operational exchange nodes, handles >1.5 Tbps peak traffic. Keeps India-to-India traffic local.

---

## 1.4 Delay, Loss, and Throughput in Packet-Switched Networks

### 1.4.1 Overview of Delay
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

### 1.4.4 Throughput
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

## Chapter 2: Application Layer

## 2.1 Principles of Network Applications

### 2.1.1 Network Application Architectures
Two main paradigms:

| Architecture | Description | Examples |
|--------------|-------------|----------|
| **Client-Server** | Always-on server (fixed IP) serves clients; clients don't communicate directly | Web, Email, DNS |
| **Peer-to-Peer (P2P)** | No always-on server; peers act as both clients and servers; self-scaling | BitTorrent, Bitcoin, Skype (original) |

**Hybrid**: Many modern apps use both (e.g., P2P for content, centralized for discovery/auth).

### 2.1.2 Processes Communicating
- **Process**: Program running on end system
- **Client process**: Initiates communication
- **Server process**: Waits for contact
- **Socket**: API between application and transport layer ("door")
- **Addressing**: IP address + port number (16-bit)

**Multiplexing/Demultiplexing**:
- Transport layer uses port numbers to deliver data to correct process
- TCP: 4-tuple (src IP, src port, dst IP, dst port)
- UDP: 2-tuple (dst IP, dst port)

### 2.1.3 Transport Services Available to Applications
| Service | TCP | UDP |
|---------|-----|-----|
| **Reliable delivery** | ✓ | ✗ |
| **In-order delivery** | ✓ | ✗ |
| **Flow control** | ✓ | ✗ |
| **Congestion control** | ✓ | ✗ |
| **Connection setup** | 3-way handshake | None |
| **Header overhead** | 20+ bytes | 8 bytes |

**Neither TCP nor UDP provides**:
- Delay guarantees (max latency)
- Bandwidth guarantees (min throughput)

### 2.1.4 Application-Layer Protocols
Define:
- Message types (request/response)
- Message syntax (fields, headers)
- Field semantics (meaning)
- Rules for when/how processes send/respond

**Open protocols** (standards): HTTP, SMTP, DNS - defined in RFCs
**Proprietary protocols**: Skype (original), some gaming protocols

---

## 2.2 The Web and HTTP

### 2.2.1 Overview of HTTP
- **HTTP** (HyperText Transfer Protocol): Web's application-layer protocol
- **Client**: Browser (requests objects)
- **Server**: Web server (responds with objects)
- **Objects**: HTML, images, CSS, JS, videos - each addressable by URL
- **Stateless**: Server maintains no client state between requests

**URL format**: `http://host:port/path`

### 2.2.2 Non-Persistent vs Persistent Connections

| Connection Type | Description | RTTs for K objects |
|-----------------|-------------|-------------------|
| **Non-persistent (HTTP/1.0)** | New TCP connection per object | K × 2 RTTs |
| **Persistent (HTTP/1.1)** | Single TCP connection for multiple objects | 2 RTT + K×transmission |
| **Pipelined Persistent** | Send requests back-to-back without waiting | 2 RTT + K×transmission |

**HTTP/1.0**: Default non-persistent (can use `Connection: keep-alive`)
**HTTP/1.1**: Default persistent, supports pipelining (rarely used due to head-of-line blocking)

### 2.2.3 HTTP Message Format

**Request Message**:
```
GET /path/to/object HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
Connection: keep-alive

[optional body for POST/PUT]
```

**Response Message**:
```
HTTP/1.1 200 OK
Date: Mon, 03 Nov 2026 12:00:00 GMT
Server: Apache/2.4
Content-Type: text/html
Content-Length: 1234
Connection: keep-alive

<html>...</html>
```

**Common Methods**: GET, POST, HEAD, PUT, DELETE, OPTIONS
**Common Status Codes**:
- 200 OK, 301 Moved Permanently, 302 Found, 304 Not Modified
- 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
- 500 Internal Server Error, 503 Service Unavailable

### 2.2.4 Cookies
**Problem**: HTTP is stateless; servers need to identify users across requests
**Solution**: **Cookies** (RFC 6265)

**How it works**:
1. Server sends `Set-Cookie: id=12345` in response header
2. Browser stores cookie locally
3. Browser includes `Cookie: id=12345` in future requests to same domain
4. Server uses cookie to maintain session state

**Components**: Name, value, expiry, domain, path, Secure flag, HttpOnly flag

### 2.2.5 Browser Caching
**Goal**: Reduce latency, bandwidth, server load
**Mechanism**:
- Server sends `Cache-Control: max-age=3600` or `Expires` header
- Browser caches response
- On subsequent request: if fresh, use cached copy; if stale, conditional GET with `If-Modified-Since` or `If-None-Match` (ETag)
- Server responds 304 Not Modified if unchanged

### 2.2.6 HTTP/2 (RFC 7540)
**Improvements over HTTP/1.1**:
1. **Binary framing** (not text) - more efficient parsing
2. **Multiplexing** - multiple streams over single TCP connection
3. **Header compression** (HPACK) - reduces overhead
4. **Server push** - server can send resources proactively
5. **Stream prioritization** - critical resources first

**Problem**: Head-of-line blocking still exists at TCP level (one lost packet blocks all streams)

### 2.2.7 HTTP/3 and QUIC
**QUIC** (Quick UDP Internet Connections):
- Runs over **UDP** (not TCP)
- Implements reliability, congestion control, TLS 1.3 **in user space**
- **0-RTT resumption** for repeat connections
- **Connection migration** - survives IP change (mobile handoff)
- **Per-stream flow control** - no head-of-line blocking across streams

**HTTP/3** = HTTP semantics over QUIC
- Same request/response model as HTTP/2
- But no TCP head-of-line blocking

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
Client → MTA (Mail Transfer Agent) → ... → MTA → Recipient's Mail Server
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

### 2.4.2 How DNS Works
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