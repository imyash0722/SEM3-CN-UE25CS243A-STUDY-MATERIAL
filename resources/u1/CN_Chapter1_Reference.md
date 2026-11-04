# Chapter 1: Computer Networks and the Internet
### Reference Sheet — *Computer Networking: A Top-Down Approach (Kurose & Ross, 8th Ed.)*

> Add your notes in the `📝` sections as you study each topic.

---

## 📚 Topic Map

| Section | Title |
|---------|-------|
| 1.1 | What Is the Internet? |
| 1.1.1 | A Nuts-and-Bolts Description |
| 1.1.2 | A Services Description |
| 1.1.3 | What Is a Protocol? |
| 1.2 | The Network Edge |
| 1.2.1 | Access Networks |
| 1.2.2 | Physical Media |
| 1.3 | The Network Core |
| 1.3.1 | Packet Switching |
| 1.3.2 | Circuit Switching |
| 1.3.3 | A Network of Networks |
| 1.4 | Delay, Loss, and Throughput in Packet-Switched Networks |
| 1.4.1 | Overview of Delay in Packet-Switched Networks |
| 1.4.2 | Queuing Delay and Packet Loss |
| 1.4.3 | End-to-End Delay |
| 1.4.4 | Throughput in Computer Networks |
| 1.5 | Protocol Layers and Their Service Models |
| 1.5.1 | Layered Architecture |
| 1.5.2 | Encapsulation |
| 1.6 | Networks Under Attack |
| 1.7 | History of Computer Networking and the Internet |
| 1.8 | Summary |

---

## 🔤 Abbreviations

| Abbreviation | Full Form |
|---|---|
| **AON** | Active Optical Network |
| **AP** | Access Point (wireless) |
| **ARPA** | Advanced Research Projects Agency |
| **ARPANET** | Advanced Research Projects Agency Network |
| **ATM** | Asynchronous Transfer Mode |
| **BGP** | Border Gateway Protocol |
| **CO** | Central Office (telco's local switching center) |
| **CMTS** | Cable Modem Termination System |
| **CRC** | Cyclic Redundancy Check |
| **CSMA** | Carrier Sense Multiple Access |
| **DNS** | Domain Name System |
| **DOCSIS** | Data Over Cable Service Interface Specification |
| **DSL** | Digital Subscriber Line |
| **DSLAM** | Digital Subscriber Line Access Multiplexer |
| **FDM** | Frequency-Division Multiplexing |
| **FTTH** | Fiber to the Home |
| **GEO** | Geostationary Earth Orbit (satellite) |
| **HFC** | Hybrid Fiber-Coaxial (cable) |
| **HTTP** | HyperText Transfer Protocol |
| **IETF** | Internet Engineering Task Force |
| **IMP** | Interface Message Processor (ARPANET's packet switch) |
| **IP** | Internet Protocol |
| **ISP** | Internet Service Provider |
| **ITU** | International Telecommunication Union |
| **IXP** | Internet Exchange Point |
| **LAN** | Local Area Network |
| **LEO** | Low-Earth Orbit (satellite) |
| **MAN** | Metropolitan Area Network |
| **MIMO** | Multiple-Input Multiple-Output |
| **MTU** | Maximum Transmission Unit |
| **NAP** | Network Access Point |
| **NIC** | Network Interface Card |
| **NSF** | National Science Foundation |
| **NSFNET** | National Science Foundation Network |
| **OC** | Optical Carrier (speed standard, e.g. OC-n = n × 51.8 Mbps) |
| **OLT** | Optical Line Terminator |
| **ONT** | Optical Network Terminator |
| **OSI** | Open Systems Interconnection |
| **OSPF** | Open Shortest Path First |
| **PAN** | Personal Area Network |
| **PDU** | Protocol Data Unit |
| **PON** | Passive Optical Network |
| **QoS** | Quality of Service |
| **RFC** | Request for Comments (IETF standards documents) |
| **RTT** | Round-Trip Time |
| **SDU** | Service Data Unit |
| **SMTP** | Simple Mail Transfer Protocol |
| **TCP** | Transmission Control Protocol |
| **TDM** | Time-Division Multiplexing |
| **TTL** | Time to Live |
| **UDP** | User Datagram Protocol |
| **UTP** | Unshielded Twisted Pair |
| **WAN** | Wide Area Network |
| **WiFi** | Wireless Fidelity (IEEE 802.11 wireless LAN standard) |

---

## 📖 Definitions

### 1.1 — What Is the Internet?

| Term | Definition |
|---|---|
| **Internet** | A computer network that interconnects billions of computing devices worldwide; also described as an infrastructure that provides services to distributed applications. |
| **Host / End System** | Any computing device connected to the Internet (desktops, laptops, smartphones, servers, IoT devices, etc.). The terms are interchangeable. |
| **Client** | An end system (typically a desktop, laptop, or smartphone) that requests services from servers. |
| **Server** | A high-capacity end system that stores and distributes content (Web pages, video, email, etc.) to clients; mostly reside in data centers. |
| **Communication Link** | A physical connection (copper wire, fiber, radio spectrum, etc.) over which bits are transmitted between devices. |
| **Transmission Rate** | The rate at which a link can transmit data, measured in **bits per second (bps)**. |
| **Packet** | A chunk of data with added header bytes that is sent through the network; the basic unit of data in packet-switched networks. |
| **Packet Switch** | A network device (router or link-layer switch) that takes an incoming packet and forwards it on an outgoing link toward its destination. |
| **Router** | A packet switch used in the **network core** to forward packets between networks. |
| **Link-Layer Switch** | A packet switch used in **access networks** to forward packets within a local network segment. |
| **Route / Path** | The sequence of communication links and packet switches traversed by a packet from source to destination. |
| **ISP (Internet Service Provider)** | A company providing end systems with Internet access; itself a network of packet switches and links (e.g., residential cable/DSL, university, corporate, cellular ISPs). |
| **Protocol** | A set of rules defining the **format**, **order** of messages exchanged between two or more communicating entities, and the **actions** taken on sending/receiving a message or other event. |
| **TCP/IP** | The Internet's principal protocol suite; TCP (Transmission Control Protocol) and IP (Internet Protocol) are the most important. |
| **IP Protocol** | Specifies the format of the packets sent and received between routers and end systems. |
| **RFC (Request for Comments)** | Technical standards documents published by the IETF that define Internet protocols (e.g., TCP, IP, HTTP, SMTP). |
| **IETF (Internet Engineering Task Force)** | The standards body responsible for developing Internet standards (RFCs). |
| **IEEE 802** | IEEE committee that specifies link-layer and physical-layer standards for LANs (e.g., Ethernet = 802.3, WiFi = 802.11). |
| **Socket Interface** | An API on end systems that specifies how an application program asks the Internet to deliver data to another program on a remote host. |
| **Distributed Application** | An application involving multiple end systems that exchange data with each other (e.g., Web, email, streaming, social media). |
| **Data Center** | A facility housing tens to hundreds of thousands of servers (blades); the backbone behind large Internet services and cloud computing. |
| **Blade** | A commodity host (resembling a pizza box) with CPU, memory, and disk; stacked in racks inside data centers. |

---

### 1.2 — The Network Edge

| Term | Definition |
|---|---|
| **Network Edge** | The periphery of the Internet where end systems (hosts) and their applications reside. |
| **Access Network** | The network that physically connects an end system to the **first (edge) router** on the path to any other remote end system. |
| **Edge Router** | The first router an end system's traffic encounters when entering the wider Internet. |
| **DSL (Digital Subscriber Line)** | Residential broadband technology using existing twisted-pair telephone lines to connect a home DSL modem to the telco's DSLAM at the CO. Asymmetric: downstream faster than upstream. |
| **DSLAM (DSL Access Multiplexer)** | Equipment at the telco's CO that aggregates DSL signals from many homes and feeds them into the Internet backbone. |
| **Splitter** | A device at the home (and CO) that separates voice telephone signals (0–4 kHz) from DSL data signals on the same copper pair. |
| **Asymmetric Access** | An access technology where downstream (to home) and upstream (from home) data rates differ; downstream is typically much higher. |
| **HFC (Hybrid Fiber-Coaxial)** | Cable Internet architecture: fiber from the cable headend to neighborhood junctions, then coaxial cable to individual homes. |
| **Cable Modem** | The customer-premises device for cable Internet; connects the home PC to the HFC network via an Ethernet port. |
| **CMTS (Cable Modem Termination System)** | Equipment at the cable headend that converts analog signals from cable modems back into digital format; analogous to the DSLAM. |
| **Shared Broadcast Medium** | A medium where all devices on a segment share bandwidth; a packet sent by any one device is received by all (e.g., HFC upstream). |
| **FTTH (Fiber to the Home)** | Broadband technology providing optical fiber directly from the telco CO to the residence; capable of Gbps speeds. |
| **PON (Passive Optical Network)** | An FTTH distribution architecture using optical splitters (no active electronics in the field) to share one fiber among many homes (< 100). |
| **ONT (Optical Network Terminator)** | The device at the customer's home in a PON/FTTH network; converts optical signals to electrical for home use. |
| **OLT (Optical Line Terminator)** | Equipment at the telco's CO in a PON architecture; provides optical-to-electrical conversion and connects to the Internet. |
| **AON (Active Optical Network)** | An FTTH distribution architecture using active (powered) switching elements; essentially switched Ethernet. |
| **5G Fixed Wireless** | Residential broadband delivered wirelessly from a provider's base station to a home modem using beam-forming technology; eliminates the need for physical last-mile cabling. |
| **Ethernet (IEEE 802.3)** | The most prevalent wired LAN technology; uses twisted-pair copper to connect hosts to an Ethernet switch; speeds from 100 Mbps to tens of Gbps. |
| **WiFi (IEEE 802.11)** | Wireless LAN standard allowing end systems to wirelessly access a LAN via an Access Point (AP); typical range of tens of meters. |
| **Access Point (AP)** | A wireless device that connects wireless hosts to a wired LAN. |
| **4G LTE / 5G** | Wide-area wireless cellular standards; 4G provides tens of Mbps, 5G provides hundreds of Mbps to Gbps; coverage range of tens of kilometers. |
| **Guided Media** | Physical media where electromagnetic signals are channeled along a solid conductor (twisted pair, coaxial cable, fiber optic). |
| **Unguided Media** | Physical media where signals propagate freely through the air or space (terrestrial radio, satellite). |
| **Twisted-Pair Copper Wire** | Cheapest, most common guided medium; two insulated copper wires twisted to reduce EMI; used for DSL, LANs (UTP, Cat 5e/6/6a). |
| **UTP (Unshielded Twisted Pair)** | Standard twisted-pair cable without additional shielding; common in LANs (10 Mbps to 10 Gbps). |
| **Coaxial Cable** | Two concentric copper conductors; higher data rates than twisted pair; used in HFC cable TV/Internet systems; can serve as shared medium. |
| **Fiber Optic Cable** | Thin glass/plastic strands that carry pulses of light (1 pulse = 1 bit); supports tens to hundreds of Gbps; immune to EMI; very low attenuation over 100 km; used for long-haul backbone and FTTH. |
| **OC (Optical Carrier)** | Speed standard for fiber links; OC-n = n × 51.8 Mbps (e.g., OC-192 = 9.95 Gbps, OC-768 = 39.8 Gbps). |
| **Terrestrial Radio Channels** | Unguided electromagnetic signals traveling through air; require no cabling; affected by path loss, shadow fading, multipath fading, and interference. |
| **Path Loss** | Signal strength reduction as a radio wave travels through distance and obstructions. |
| **Shadow Fading** | Signal attenuation caused by a radio wave passing around or through objects. |
| **Multipath Fading** | Signal degradation caused by the same signal arriving via multiple reflected paths. |
| **Geostationary (GEO) Satellite** | Communication satellite fixed above one point on Earth at ~36,000 km altitude; introduces ~280 ms propagation delay. |
| **LEO (Low-Earth Orbit) Satellite** | Satellite orbiting much closer to Earth; lower latency than GEO; requires constellation of many satellites for continuous coverage (e.g., Starlink). |

---

### 1.3 — The Network Core

| Term | Definition |
|---|---|
| **Network Core** | The mesh of routers and high-speed links that interconnects the Internet's end systems. |
| **Packet Switching** | A network approach where data is broken into packets, each forwarded independently through the network; routers use **store-and-forward** transmission. |
| **Store-and-Forward Transmission** | A packet switch must receive (store) the **entire** packet before it can begin transmitting (forwarding) it onto the next outbound link. |
| **Output Buffer / Output Queue** | Memory on a packet switch that holds packets waiting to be transmitted on an outgoing link. |
| **Queuing Delay** | The time a packet waits in a router's output buffer because the link is busy transmitting another packet. |
| **Packet Loss** | Occurs when a router's buffer is full and an arriving packet must be dropped. |
| **Forwarding Table** | A table inside a router that maps destination addresses (or prefixes) to outgoing links; used to determine where to send each packet. |
| **Routing Protocol** | A protocol (e.g., OSPF, BGP) that automatically fills and updates a router's forwarding table. |
| **Circuit Switching** | A network approach where resources (bandwidth, buffers) along a path are **reserved** for the duration of a communication session before data is sent (e.g., traditional telephone network). |
| **FDM (Frequency-Division Multiplexing)** | Circuit-switching technique that divides the link bandwidth into frequency bands, with each circuit assigned one band for its entire duration. |
| **TDM (Time-Division Multiplexing)** | Circuit-switching technique that divides time into frames of fixed slots, with each circuit assigned one slot per frame for its entire duration. |
| **Silent Periods** | Periods during a circuit-switched call where no data is transmitted but reserved bandwidth is still held (wasted). |
| **Multiplexing** | Sharing a link's capacity among multiple users/circuits simultaneously (FDM, TDM, or statistical). |
| **Statistical Multiplexing** | Packet switching's sharing approach where link capacity is shared dynamically on-demand; no reservations made. |
| **Tier-1 ISP** | The highest level of ISP; national/international ISPs with high-speed fiber-optic links that interconnect directly with each other (e.g., AT&T, Sprint, NTT). |
| **Tier-2 ISP** | Regional ISPs that connect to one or more Tier-1 ISPs; may also peer with other Tier-2 ISPs. |
| **Tier-3 ISP** | Local ISPs / access ISPs that connect to Tier-2 ISPs and provide last-mile access to end users. |
| **Peering** | When two ISPs at the same level connect their networks directly without payment to exchange traffic. |
| **IXP (Internet Exchange Point)** | A physical facility where multiple ISPs can peer and exchange traffic directly. |
| **Content Provider Network** | A private network built by large companies (e.g., Google, Netflix) to bypass ISPs and deliver content directly from their data centers to end users. |

---

### 1.4 — Delay, Loss, and Throughput

| Term | Definition |
|---|---|
| **Nodal Processing Delay (d_proc)** | Time a router takes to examine the packet header and determine the output link; typically < 1 millisecond. |
| **Queuing Delay (d_queue)** | Time the packet waits in the router's output queue before being transmitted; depends on congestion level; highly variable. |
| **Transmission Delay (d_trans)** | Time to push all the packet's bits onto the link; = **L/R** (L = packet length in bits, R = link transmission rate in bps). |
| **Propagation Delay (d_prop)** | Time for a bit to travel from sender to receiver along the physical medium; = **d/s** (d = distance, s = propagation speed ≈ 2×10⁸ m/s for copper/fiber). |
| **Total Nodal Delay** | d_nodal = d_proc + d_queue + d_trans + d_prop |
| **End-to-End Delay** | Total delay from source to destination across all N links: d_end-end = N(d_proc + d_trans + d_prop) (ignoring queuing). |
| **Traffic Intensity** | The ratio **La/R** (L = packet size in bits, a = average packet arrival rate in packets/s, R = link rate); when La/R → 1, queuing delay → ∞. |
| **Packet Loss** | When traffic intensity is high and the queue is full, arriving packets are dropped/lost. |
| **Throughput** | The rate (bits/sec) at which bits are successfully delivered from sender to receiver. |
| **Instantaneous Throughput** | Throughput at a specific instant in time. |
| **Average Throughput** | Total bits transferred divided by total time taken. |
| **Bottleneck Link** | The link on the end-to-end path with the minimum transmission rate; limits the overall throughput. |
| **Traceroute** | A network diagnostic tool that sends packets to each router on the path to a destination and measures their RTT; reveals path and per-hop delays. |
| **RTT (Round-Trip Time)** | The time for a small packet to travel from a client to a server and back again. |

---

### 1.5 — Protocol Layers and Their Service Models

| Term | Definition |
|---|---|
| **Protocol Layering** | The organization of network protocols and hardware into a **stack of layers**, each providing services to the layer above and using services from the layer below. |
| **Service Model** | The set of services a layer provides to the layer above it. |
| **Internet Protocol Stack (5-Layer)** | The five layers of the Internet model (top to bottom): **Application → Transport → Network → Link → Physical**. |
| **OSI Model (7-Layer)** | The ISO standard with 7 layers (top to bottom): **Application → Presentation → Session → Transport → Network → Data Link → Physical**. |
| **Application Layer** | Topmost layer; where network applications and their protocols reside (HTTP, SMTP, FTP, DNS, etc.); messages at this layer are called **messages**. |
| **Transport Layer** | Transports application-layer messages between application endpoints; provides multiplexing/demultiplexing and (in TCP) reliable delivery and congestion control; PDU = **segment**. |
| **Network Layer** | Routes datagrams from source to destination host across multiple networks; protocols include IP and routing protocols; PDU = **datagram**. |
| **Link Layer** | Moves data between adjacent nodes (host-to-router or router-to-router) over a single link; protocols include Ethernet, WiFi; PDU = **frame**. |
| **Physical Layer** | Moves individual **bits** within a frame from one node to the next; protocol depends on actual link medium (copper, fiber, radio). |
| **Presentation Layer** | (OSI only) Provides services for data interpretation, encryption, compression between communicating applications. |
| **Session Layer** | (OSI only) Provides for delimiting and synchronization of data exchange between communicating applications. |
| **Encapsulation** | The process by which each layer adds its own header information to the data received from the layer above, forming the PDU for that layer. |
| **PDU (Protocol Data Unit)** | The unit of data at each layer: message (application), segment (transport), datagram (network), frame (link), bit (physical). |
| **Header** | Control information prepended (and sometimes appended as a trailer) to a PDU's payload by a layer for communication with its peer layer on the remote host. |
| **Payload** | The data field of a PDU; contains the PDU from the layer above. |

---

### 1.6 — Networks Under Attack

| Term | Definition |
|---|---|
| **Malware** | Malicious software that can infect a host; includes viruses, worms, trojans, spyware, ransomware. |
| **Virus** | Malware that requires some form of user interaction (e.g., opening an attachment) to infect a host. |
| **Worm** | Malware that can enter a device without any explicit user interaction; self-replicating. |
| **Botnet** | A network of compromised (infected) hosts controlled by an attacker; used for spam, DDoS attacks, etc. |
| **DoS Attack (Denial-of-Service)** | An attack that makes a network, host, or infrastructure resource unavailable to legitimate users. |
| **DDoS Attack (Distributed Denial-of-Service)** | A DoS attack that uses multiple compromised hosts (a botnet) to flood the target with traffic. |
| **Vulnerability Attack** | An attacker sends a well-crafted message to a vulnerable application or OS to crash or hijack a host. |
| **Bandwidth Flooding** | An attacker sends a deluge of packets to overwhelm the target's access link, preventing legitimate traffic from getting through. |
| **Connection Flooding** | An attacker establishes a large number of half-open or fully-open TCP connections with the target, bogging it down. |
| **Packet Sniffer** | A passive receiver that records a copy of every packet flowing through a network; used for eavesdropping. |
| **Wireshark** | A popular, free, open-source packet sniffer/analyzer used for network diagnosis and study. |
| **IP Spoofing** | Injecting packets into the Internet with a false source address; the receiver cannot easily tell if the source is authentic. |
| **End-Point Authentication** | A mechanism that allows communicating parties to verify they are actually talking to whom they think they are (addressed in Chapter 8). |

---

### 1.7 — History of Computer Networking

| Term | Definition |
|---|---|
| **ARPANET** | The precursor to the Internet; first packet-switched network, launched in 1969 by ARPA; connected four university nodes. |
| **IMP (Interface Message Processor)** | The packet switch used in ARPANET; a forerunner of modern routers. |
| **NCP (Network Control Protocol)** | The first host-to-host protocol used on ARPANET; predecessor to TCP/IP. |
| **TCP/IP** | Developed by Cerf and Kahn (1974); became the standard protocol for the Internet, replacing NCP in ARPANET in 1983. |
| **NSFNET** | A backbone network funded by the National Science Foundation (NSF) in the 1980s that interconnected supercomputer centers and allowed broader Internet access. |
| **WWW (World Wide Web)** | Invented by Tim Berners-Lee (1989–1991); uses HTTP to share and link documents on the Internet; popularized Internet use in the 1990s. |
| **Mosaic** | The first graphical Web browser (1993); dramatically increased Web accessibility and adoption. |

---

## 📝 My Notes

> *(Write your own key takeaways here as you study each section.)*

### 1.1 — What Is the Internet?


### 1.2 — The Network Edge


### 1.3 — The Network Core


### 1.4 — Delay, Loss, and Throughput


### 1.5 — Protocol Layers


### 1.6 — Networks Under Attack


### 1.7 — History


---

*Last updated: Chapter 1 complete*
