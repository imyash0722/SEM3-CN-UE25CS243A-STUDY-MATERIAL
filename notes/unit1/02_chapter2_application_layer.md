# Unit 1: Application Layer (Chapter 2)

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

### 2.1.4 Transport Services Provided by the Internet
- **TCP**: Reliable byte stream; used by HTTP, SMTP, FTP, SSH
- **UDP**: Unreliable datagram; used by DNS, RTP, DHCP, QUIC
- **Additional**: TLS/SSL for security (runs on top of TCP)

### 2.1.5 Application-Layer Protocols
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

### 2.2.4 User-Server Interaction: Cookies
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

### 2.5.4 Case Studies: Netflix and YouTube
**Netflix**:
- Own CDN (Open Connect Appliances) deployed at ISPs
- Pre-positions content based on viewing predictions
- Uses adaptive streaming (DASH-like)
- ~15% of global Internet traffic

**YouTube**:
- Google Global Cache (GGC) at ISPs
- Transcodes to many formats/resolutions
- Uses QUIC/HTTP/3 for transport

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
| Persistent + Pipelining | `2×RTT + K×L/R` |
| HTTP/2 / HTTP/3 | `RTT_handshake + RTT_req/resp + L/R` |

**DNS**: 3-level lookup = 8 messages (4 queries + 4 replies)
**TTL**: Typically 2 days = 172,800 seconds

---

## Review Questions

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