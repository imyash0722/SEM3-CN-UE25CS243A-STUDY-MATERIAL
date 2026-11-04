# Unit 1: Application Layer (Chapter 2)

## 2.1 Principles of Network Applications

### 2.1.1 Network Application Architectures
Two main paradigms:

| Architecture | Description | Examples |
|--------------|-------------|----------|
| **Client-Server** | Always-on server (fixed IP) serves clients; clients don't communicate directly; often data centers for scaling | Web, Email, DNS, Video Streaming |
| **Peer-to-Peer (P2P)** | No always-on server; peers act as both clients and servers; self-scaling (new peers bring capacity + demand) | BitTorrent, Bitcoin, Skype (original) |

**Hybrid**: Many modern apps use both (e.g., P2P for content, centralized for discovery/auth).

**Key Insight**: Application architecture ≠ Network architecture. Network architecture (5-layer stack) is fixed; application architecture is chosen by developer.

### 2.1.2 Processes Communicating
- **Process**: Program running within a host (not the program itself, but its execution instance)
- **Client process**: Initiates communication
- **Server process**: Waits to be contacted
- **Inter-process communication**: Same host (OS-defined); Different hosts (exchange messages over network)

### 2.1.3 Sockets
- **Socket**: Interface between application process and transport-layer protocol
- **Analogy**: Process = house, Socket = door
- **Sending process** shoves message out its door (socket)
- **Transport infrastructure** on other side delivers to receiving process's door
- **Application developer controls**: Application-layer side of socket
- **OS controls**: Transport-layer side of socket
- **Developer choices**: (1) Transport protocol (TCP/UDP), (2) Few parameters (buffer sizes, MSS)

### 2.1.4 Addressing Processes
To receive messages, process needs identifier:
- **Host identifier**: 32-bit IP address
- **Process identifier**: **Port number** (16-bit)
- **Example**: Web server: IP + port 80; Mail server: IP + port 25

### 2.1.5 Transport Services Available to Applications
Four dimensions:

| Service | Description |
|---------|-------------|
| **Reliable Data Transfer** | Guaranteed delivery without errors, in order (TCP) vs loss-tolerant (UDP) |
| **Throughput** | Guaranteed minimum rate (not provided by Internet) vs elastic (use whatever) |
| **Timing** | Guaranteed max delay (not provided) vs best-effort |
| **Security** | Encryption, integrity, authentication (TLS enhances TCP) |

**Services NOT provided by Internet transport protocols**: Throughput guarantees, Timing guarantees

### 2.1.6 Transport Services Provided by the Internet

| Feature | TCP | UDP |
|---------|-----|-----|
| **Connection** | Connection-oriented (3-way handshake) | Connectionless |
| **Reliability** | Reliable, in-order byte stream | Unreliable, may arrive out of order |
| **Flow Control** | Yes (receiver buffer) | No |
| **Congestion Control** | Yes (throttles sender) | No |
| **Security** | Via TLS (application layer) | Via DTLS |
| **Header Overhead** | 20+ bytes | 8 bytes |

**Application Protocol Mapping**:
- TCP: HTTP, SMTP, FTP, SSH, IMAP
- UDP: DNS, RTP, DHCP, SIP, QUIC
- Either: Video conferencing (UDP preferred, TCP fallback for firewalls)

### 2.1.7 Application-Layer Protocols
Define:
- Message types (request/response)
- Message syntax (fields, delineation)
- Field semantics (meaning)
- Rules for when/how to send/respond

**Open protocols** (RFCs): HTTP, SMTP, DNS - interoperability
**Proprietary protocols**: Zoom, Skype (original)

---

## 2.2 The Web and HTTP

### 2.2.1 Overview of HTTP
- **HTTP**: HyperText Transfer Protocol (RFC 1945, 7230, 7540, 9114)
- **Client**: Browser (requests, receives, displays objects)
- **Server**: Web server (sends objects in response)
- **Objects**: HTML, JPEG, JavaScript, CSS, video - each addressable by URL
- **Web page**: Base HTML + referenced objects (e.g., HTML + 5 images = 6 objects)
- **URL format**: `http://hostname/path` (hostname + path name)
- **Stateless**: Server maintains no client state between requests

### 2.2.2 Non-Persistent vs Persistent Connections

| Connection Type | Description | RTTs for K objects |
|-----------------|-------------|-------------------|
| **Non-persistent (HTTP/1.0)** | New TCP connection per object | K × 2 RTTs |
| **Persistent (HTTP/1.1)** | Single TCP connection for multiple objects | 2 RTT + K×trans |
| **Pipelined Persistent** | Send requests back-to-back without waiting | 2 RTT + K×trans |

**HTTP/1.0**: Default non-persistent (can use `Connection: keep-alive`)
**HTTP/1.1**: Default persistent, supports pipelining (rarely used due to HOL blocking)

**Numerical Example**: 1 HTML + 6 images, RTT=80ms, transmission negligible
- Non-persistent: 7 × 2 × 80 = 1120 ms
- Persistent (no pipelining): 1 (TCP) + 7 (req/resp) = 8 RTT = 640 ms
- Persistent (pipelining): 1 (TCP) + 1 (HTML) + 1 (all images) = 3 RTT = 240 ms

### 2.2.3 HTTP Message Format

**Request Message**:
```
GET /somedir/page.html HTTP/1.1
Host: www.someschool.edu
Connection: close
User-agent: Mozilla/5.0
Accept-language: fr

[empty line]
[entity body - empty for GET, form data for POST]
```

**Components**:
- **Request line**: Method (GET, POST, HEAD, PUT, DELETE), URL, HTTP version
- **Header lines**: Host, Connection, User-agent, Accept-language, etc.
- **Entity body**: For POST (form data), PUT (file upload)

**Response Message**:
```
HTTP/1.1 200 OK
Connection: close
Date: Mon, 21 Oct 2024 18:58:21 GMT
Server: Apache/2.2.3
Last-Modified: Sun, 20 Oct 2024 13:20:46 GMT
Content-Length: 6821
Content-Type: text/html

<html>...</html>
```

**Components**:
- **Status line**: Version, status code, phrase
- **Header lines**: Date, Server, Last-Modified, Content-Length, Content-Type
- **Entity body**: Requested object

**Common Methods**: GET (retrieve), POST (submit form), HEAD (headers only), PUT (upload), DELETE (remove)

**Common Status Codes**:
- 200 OK, 301 Moved Permanently, 304 Not Modified
- 400 Bad Request, 404 Not Found
- 505 HTTP Version Not Supported

### 2.2.4 User-Server Interaction: Cookies
**Problem**: HTTP is stateless; servers need to identify users across requests
**Solution**: **Cookies** (RFC 6265)

**Four Components**:
1. **Set-cookie header** in HTTP response
2. **Cookie header** in subsequent HTTP requests
3. **Cookie file** on user's host (managed by browser)
4. **Back-end database** at Web site

**How it works**:
1. User visits site first time → Server creates unique ID, stores in database
2. Server responds with `Set-cookie: 1678`
3. Browser stores `hostname, 1678` in cookie file
4. Subsequent requests include `Cookie: 1678`
5. Server tracks user activity, enables shopping cart, recommendations

**Privacy**: Third-party cookies (ad networks) track across sites; restricted by modern browsers

### 2.2.5 Browser Caching
**Goal**: Reduce latency, bandwidth, server load
**Mechanism**:
- Server sends `Cache-Control: max-age=3600` or `Expires`
- Browser caches response
- **Conditional GET**: If stale, send `If-Modified-Since: <date>`
- Server responds **304 Not Modified** (no object) if unchanged
- **304 saves bandwidth and response time**

**Cache-Control directives**: `no-store`, `max-age`, `must-revalidate`, etc.

### 2.2.6 HTTP/2 (RFC 7540)
**Goals**: Reduce latency, eliminate HOL blocking, header compression
**Key Features**:
1. **Binary framing** (not text) - efficient parsing
2. **Multiplexing** - multiple streams over single TCP connection
3. **Header compression (HPACK)** - reduces overhead
4. **Server push** - send resources proactively
5. **Stream prioritization** - critical resources first

**HOL Blocking Problem in HTTP/1.1**: Single TCP connection → large object blocks small ones behind it
**HTTP/2 Solution**: Frame interleaving - break messages into frames, interleave on same connection

**Example**: Video (1000 frames) + 8 small objects (2 frames each)
- With interleaving: Small objects sent after 18 frames
- Without: Small objects wait for 1016 frames

**Limitation**: HOL blocking still at TCP level (lost packet blocks all streams)

### 2.2.7 HTTP/3 and QUIC (RFC 9114, RFC 9000)
**QUIC**: Quick UDP Internet Connections
- Runs over **UDP** (not TCP)
- Implements reliability, congestion control, TLS 1.3 **in user space**
- **0-RTT resumption** for repeat connections
- **Connection migration** - survives IP change (mobile handoff)
- **Per-stream flow control** - no HOL blocking across streams

**HTTP/3** = HTTP semantics over QUIC

**Handshake Comparison**:
- TCP + TLS 1.2: 2 RTT
- TCP + TLS 1.3: 1 RTT
- QUIC + TLS 1.3: 1 RTT
- QUIC 0-RTT: 0 RTT (resumption)

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
Client → MTA → ... → MTA → Recipient's Mail Server
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

### 2.4.2 Overview of How DNS Works
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

**Messages for 3-level lookup**: 8 messages (4 queries + 4 replies)

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

**Netflix Case Study**: 
- Open Connect Appliances deployed at ISPs
- Pre-positions content based on viewing predictions
- ~15% of global Internet traffic

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

### 2.6.3 Socket Programming with QUIC
- Uses libraries like `aioquic` (Python)
- Similar to TCP but with streams, 0-RTT, connection migration
- Application handles TLS certificates

---

## Key Formulas (Chapter 2)

| Scenario | Total Time |
|----------|------------|
| Non-persistent (K objects) | `K × (2×RTT + L/R)` |
| Non-persistent (P parallel) | `ceil(K/P) × (2×RTT + L/R)` |
| Persistent (no pipelining) | `2×RTT + K×L/R` |
| Persistent + Pipelining | `2×RTT + K×L/R` (requests back-to-back) |
| HTTP/2 / HTTP/3 | `RTT_handshake + RTT_req/resp + L/R` |

**DNS**: 3-level lookup = 8 messages (4 queries + 4 replies)
**TTL**: Typically 2 days = 172,800 seconds

---

## Complete Questions, Examples, and MCQs from Slides and Textbook

### Numerical Problems (Exam Practice)

**Q1. HTTP Performance Calculation**: 
A web page consists of a base HTML (100 KB) + 5 embedded images (200 KB each). RTT = 80 ms. Transmission rates: server link = 100 Mbps, client link = 50 Mbps. Calculate total time for:
- a) Non-persistent HTTP
- b) Persistent HTTP (no pipelining)
- c) Persistent HTTP (pipelining)

**Answer**: 
- a) 6 objects × (2 × 80 + 300KB/50Mbps) = 6 × (160 + 48) = 1248 ms
- b) 2×80 + 6×(300KB/50Mbps) = 160 + 288 = 448 ms
- c) 80 + 300KB/50Mbps + 80 + 5×300KB/50Mbps ≈ 240 ms

**Q2. DNS Query Calculation**:
For a 3-level DNS lookup (root → TLD → authoritative), how many messages are exchanged?
- **Answer**: 8 messages (4 queries + 4 replies)

**Q3. DNS Caching**: TTL = 2 days. How many seconds?
- **Answer**: 172,800 seconds

### Review Questions

1. **Client-server vs P2P?**
   - Client-server: dedicated always-on server
   - P2P: peers act as both client/server, self-scaling

2. **What is a socket?**
   - API between application and transport layer; identified by (IP, port)

3. **TCP vs UDP services?**
   - TCP: reliable, ordered, flow/congestion control, connection-oriented
   - UDP: unreliable, unordered, no flow/congestion control, connectionless

4. **Non-persistent vs persistent HTTP?**
   - Non-persistent: new TCP per object (2 RTT each)
   - Persistent: single TCP for multiple objects

5. **How do cookies work?**
   - Server sets cookie via Set-Cookie header
   - Browser sends cookie in future requests to same domain

6. **What is DNS and how does it work?**
   - Hierarchical distributed database mapping names to IPs
   - Recursive/iterative queries; caching with TTL

7. **What is DASH?**
   - HTTP-based adaptive streaming; client selects quality based on bandwidth

8. **What is a CDN?**
   - Geographically distributed servers caching content near users

9. **UDP vs TCP socket programming?**
   - UDP: sendto/recvfrom with address; no connection
   - TCP: connect/accept; send/recv without address; welcoming + connection sockets

10. **HTTP/2 vs HTTP/3?**
    - HTTP/2: TCP, multiplexing, but HOL blocking at TCP level
    - HTTP/3: QUIC over UDP, 0-RTT, connection migration, per-stream control

---

## Multiple Choice Questions (from Slides)

**Q1. Application architecture vs Network architecture:**
- Application architecture: chosen by developer (client-server, P2P)
- Network architecture: fixed (5-layer stack)

**Q2. A process sends messages into, and receives messages from, the network through a software interface called:**
- a) port
- b) **socket**
- c) pipe
- d) channel

**Q3. The socket is the interface between:**
- a) Application layer and network layer
- b) Transport layer and network layer
- c) **Application layer and transport layer**
- d) Physical layer and link layer

**Q4. To identify the receiving process, two pieces of information need to be specified:**
- (1) the address of the host (IP)
- (2) an identifier that specifies the receiving process (port number)

**Q5. Which of the following is NOT a service provided by Internet transport protocols?**
- a) Reliable data transfer
- b) **Throughput guarantees**
- c) Timing guarantees
- d) Security (via TLS)

**Q6. TCP services include:**
- a) Connection-oriented service (handshaking)
- b) Reliable data transfer service
- c) Congestion control (for Internet welfare)
- d) **All of the above**

**Q7. UDP provides:**
- a) Connection-oriented service
- b) Reliable data transfer
- c) **Connectionless, unreliable data transfer**
- d) Congestion control

**Q7. HTTP is stateless. How does server maintain user state?**
- a) Session IDs in URLs
- b) **Cookies** (Set-Cookie / Cookie headers)
- c) Hidden form fields
- d) IP address tracking

**Q8. HTTP/1.1 default connection type:**
- a) Non-persistent
- b) **Persistent**
- c) Pipelined
- d) Parallel

**Q9. HTTP/2 multiplexing solves which problem?**
- a) **Head-of-line blocking**
- b) Slow start
- c) Three-way handshake
- d) DNS lookup

**Q10. HTTP/3 runs over:**
- a) TCP
- b) **UDP (QUIC)**
- c) SCTP
- d) IP directly

**Q11. SMTP is a:**
- a) Pull protocol
- b) **Push protocol**
- c) Peer-to-peer protocol
- d) Connectionless protocol

**Q12. Which port does SMTP use for server-to-server?**
- a) 587
- b) **25**
- c) 110
- d) 143

**Q13. DNS query types:**
- Recursive: Resolver does all work
- Iterative: Resolver asks root → TLD → authoritative step by step

**Q14. For 3-level DNS lookup, total messages = ?**
- a) 4
- b) 6
- c) **8**
- d) 12

**Q15. CDN benefits:**
- Lower latency, higher throughput, reduced origin load, DDoS absorption

**Q16. Socket programming - UDP vs TCP:**
- UDP: `sendto()`/`recvfrom()` with address; no connection
- TCP: `connect()`/`accept()`; `send()`/`recv()` without address

---

## Textbook End-of-Chapter Problems (Chapter 2)

**P1.** Compare client-server and P2P architectures for a video streaming application.
**P2.** Write a simple UDP client-server in Python that echoes messages.
**P3.** Calculate total HTTP response time for a page with K objects under non-persistent, persistent, and pipelined connections.
**P4.** Explain how cookies work with a diagram showing request/response headers.
**P5.** Describe the DNS resolution process for www.example.com with a diagram.
**P6.** What are the differences between POP3, IMAP, and HTTP for email access?
**P7.** Explain DASH adaptive streaming and how it differs from traditional RTSP/RTP streaming.
**P8.** Describe CDN operation: request routing, content placement, content delivery.
**P9.** Write a TCP client-server in Python for a simple file transfer application.
**P10.** Compare HTTP/1.1, HTTP/2, and HTTP/3 in terms of handshake, multiplexing, and HOL blocking.