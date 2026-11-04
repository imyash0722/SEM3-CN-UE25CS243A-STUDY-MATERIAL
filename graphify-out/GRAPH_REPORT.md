# Graph Report - CN  (2026-11-04)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 857 nodes · 2167 edges · 38 communities (27 shown, 11 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 193 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `99f1e11f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- m
- search.c47bb847.min.js
- bundle.77dd0ce9.min.js
- test_suite.py
- ou
- e
- zensical.yml
- ShowcaseRunner
- socket
- sdn_controller.py
- tp
- t
- project.yml
- q
- IDSMonitor
- TCPServer
- AttackGenerator
- TestIntrusionDetectionSystem
- analyze_results.py
- SDNControllerApp
- ko
- SimpleIDSController
- n
- Unit 3: Network Layer
- Chapter 6: Link Layer & LAN
- Chapter 2: Application Layer
- Chapter 3: Transport Layer
- Chapter 1: Computer Networks & the Internet
- lu
- nav
- threading
- oc
- tn
- Chapter 4: Data Plane
- run.sh script

## God Nodes (most connected - your core abstractions)
1. `m()` - 72 edges
2. `e()` - 66 edges
3. `t()` - 42 edges
4. `b()` - 40 edges
5. `r()` - 39 edges
6. `q()` - 32 edges
7. `G()` - 27 edges
8. `ec()` - 25 edges
9. `wc()` - 23 edges
10. `ee()` - 22 edges

## Surprising Connections (you probably didn't know these)
- `ShowcaseRunner` --uses--> `IDSMonitor`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/demo.py → project/first_presentation/network_intrusion_detection/advanced/ids_monitor.py
- `IDSMonitor` --uses--> `SecurityAlert`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/ids_monitor.py → project/first_presentation/network_intrusion_detection/advanced/protocol.py
- `TestIntrusionDetectionSystem` --uses--> `IDSMonitor`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/test_suite.py → project/first_presentation/network_intrusion_detection/advanced/ids_monitor.py
- `ShowcaseRunner` --uses--> `TCPServer`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/demo.py → project/first_presentation/network_intrusion_detection/advanced/tcp_server.py
- `TestIntrusionDetectionSystem` --uses--> `TCPServer`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/test_suite.py → project/first_presentation/network_intrusion_detection/advanced/tcp_server.py

## Import Cycles
- None detected.

## Communities (38 total, 11 thin omitted)

### Community 0 - "m"
Cohesion: 0.08
Nodes (89): Ac(), ae(), af(), Ap(), as(), b(), bc(), bf() (+81 more)

### Community 1 - "search.c47bb847.min.js"
Cohesion: 0.06
Nodes (62): Wt(), A(), ae(), At(), B(), bt(), C(), ce() (+54 more)

### Community 2 - "bundle.77dd0ce9.min.js"
Cohesion: 0.05
Nodes (42): Ba(), Cl(), constructor(), Cs(), D(), dl(), ea(), ei() (+34 more)

### Community 3 - "test_suite.py"
Cohesion: 0.09
Nodes (9): main(), main(), format_alert_log(), parse_ipc_message(), SecurityAlert, serialize_ipc_message(), main(), main() (+1 more)

### Community 4 - "ou"
Cohesion: 0.09
Nodes (41): a(), c(), dr(), f(), Fa(), gf(), hl(), jt() (+33 more)

### Community 5 - "e"
Cohesion: 0.08
Nodes (45): be(), bi(), co(), e(), B(), c(), d(), E() (+37 more)

### Community 6 - "zensical.yml"
Cohesion: 0.05
Nodes (38): property, provider, copyright, extra, analytics, extra_javascript, social, version (+30 more)

### Community 7 - "ShowcaseRunner"
Cohesion: 0.08
Nodes (4): main(), print_banner(), ShowcaseRunner, TCPClient

### Community 8 - "socket"
Cohesion: 0.09
Nodes (9): connection_flood(), main(), port_scan(), main(), send_request(), find_available_port(), ProtectedServer, run_demonstration() (+1 more)

### Community 9 - "sdn_controller.py"
Cohesion: 0.10
Nodes (3): BaseControllerLogic, main(), StandaloneMockController

### Community 10 - "tp"
Cohesion: 0.11
Nodes (28): Bu(), cu(), ds(), Du(), ep(), fp(), gt(), Gu() (+20 more)

### Community 11 - "t"
Cohesion: 0.11
Nodes (27): bn(), Ci(), di(), dn(), Fr(), ft(), Ga(), hi() (+19 more)

### Community 12 - "project.yml"
Cohesion: 0.09
Nodes (22): activation_command, activation_command_timeout, added_modes, default_modes, encoding, excluded_tools, fixed_tools, ignore_all_files_in_gitignore (+14 more)

### Community 13 - "q"
Cohesion: 0.14
Nodes (23): Ai(), an(), ao(), Ar(), at(), cn(), El(), $i() (+15 more)

### Community 18 - "analyze_results.py"
Cohesion: 0.20
Nodes (8): calculate_metrics(), export_reports(), load_json_safe(), main(), print_comparison_table(), clean_processes(), run_experiment.sh script, show_help()

### Community 20 - "ko"
Cohesion: 0.18
Nodes (13): au(), bt(), Da(), es(), Hu(), ko(), se(), tu() (+5 more)

### Community 22 - "n"
Cohesion: 0.22
Nodes (11): fo(), Ie(), pi(), n(), o(), Tl(), uu(), wl() (+3 more)

### Community 23 - "Unit 3: Network Layer"
Cohesion: 0.18
Nodes (11): DHCP, ICMP, IPv6, 4.6 SDN & OpenFlow, 4.7 Data Center Networking, 5.1-5.3 Routing Algorithms (Dijkstra/Bellman-Ford), Unit 3: Network Layer, Additional Topics (+3 more)

### Community 24 - "Chapter 6: Link Layer & LAN"
Cohesion: 0.18
Nodes (11): 6.10 Wireless LANs (802.11), 6.1 Introduction to Link Layer, 6.2 Error Detection & Correction, 6.3 Multiple Access Protocols (CSMA/CD/CA), 6.4 Switched LANs, MAC, ARP, 6.5 Ethernet, 6.6 Ethernet Switches, 6.7 VLANs (+3 more)

### Community 25 - "Chapter 2: Application Layer"
Cohesion: 0.20
Nodes (10): 2.1 Principles of Network Applications, 2.2 The Web and HTTP, 2.3 Electronic Mail, 2.4 DNS, 2.5 Video Streaming & CDNs, 2.6 Socket Programming, Unit 1: Internet & Application Layer, Chapter 2: Application Layer (+2 more)

### Community 26 - "Chapter 3: Transport Layer"
Cohesion: 0.20
Nodes (10): 3.1 Transport Services, 3.2 Multiplexing & Demultiplexing, 3.3 UDP, 3.4 Reliable Data Transfer (GBN/SR), 3.5 TCP, 3.6-3.7 Congestion Control, Unit 2: Transport Layer, Chapter 3: Transport Layer (+2 more)

### Community 27 - "Chapter 1: Computer Networks & the Internet"
Cohesion: 0.25
Nodes (8): 1.1 What Is the Internet?, 1.2 The Network Edge, 1.3 The Network Core, 1.4 Delay, Loss, and Throughput, 1.5 Protocol Layers, 1.6 Network Security, 1.7 History of Networking, Chapter 1: Computer Networks & the Internet

### Community 29 - "lu"
Cohesion: 0.29
Nodes (7): Do(), fs(), Ju(), ku(), lu(), wu(), xu()

### Community 30 - "nav"
Cohesion: 0.29
Nodes (7): nav, Formulae Sheet, Home, Master Index & Study Checklist, Unit 4: Link Layer & LAN, Complete Unit 4 Notes, Overview

### Community 32 - "oc"
Cohesion: 0.40
Nodes (6): Bp(), Gp(), Gr(), oc(), qp(), vn()

### Community 33 - "tn"
Cohesion: 0.40
Nodes (5): ns(), rn(), tn(), vi(), xl()

### Community 34 - "Chapter 4: Data Plane"
Cohesion: 0.40
Nodes (5): 4.1 Network Layer Overview, 4.2 Inside a Router, 4.3-4.4 IPv4 & Fragmentation, 4.5 IPv4 Addressing & NAT, Chapter 4: Data Plane

## Knowledge Gaps
- **11 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `e()` connect `e` to `m`, `oc`, `bundle.77dd0ce9.min.js`, `tn`, `ou`, `search.c47bb847.min.js`, `tp`, `t`, `q`, `n`, `lu`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 24 inferred relationships involving `e()` (e.g. with `bi()` and `d()`) actually correct?**
  _`e()` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Should `m` be split into smaller, more focused modules?**
  _Cohesion score 0.0756545042259328 - nodes in this community are weakly interconnected._
- **Why does `se()` connect `search.c47bb847.min.js` to `e`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `t()` (e.g. with `bundle.77dd0ce9.min.js` and `Cr()`) actually correct?**
  _`t()` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Should `search.c47bb847.min.js` be split into smaller, more focused modules?**
  _Cohesion score 0.06335403726708075 - nodes in this community are weakly interconnected._
- **Why does `BaseControllerLogic` connect `sdn_controller.py` to `test_suite.py`, `SDNControllerApp`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._