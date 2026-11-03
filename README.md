# UE25CS243A — Computer Networks (Semester 3)

Welcome to the course repository for **Computer Networks (UE25CS243A)**. This directory is organized into three main sections: **Labs**, **Project**, and **Course Resources**.

---

## Directory Overview

```text
/mnt/shared/sem3/CN/
│
├── labs/                                     # 🧪 All laboratory manuals, exercises & reports
│   ├── lab1_cisco/                           # Lab 1: Cisco Packet Tracer Simulation + Lab Manual
│   ├── lab2_wireshark/                       # Lab 2: Wireshark HTTP & Web Analysis + Lab Manual & Video
│   ├── lab3_wireshark/                       # Lab 3: Wireshark UDP & DNS Exploration + Lab Manual & Report
│   ├── lab4_wireshark/                       # Lab 4: Wireshark TCP Connection Analysis + Report
│   ├── lab6_hardware/                        # Lab 6: Hardware Program Manual
│   └── setup_and_tools/                      # Wireshark & VM installation guides, basic command demos
│
├── project/                                  # 🛡️ Mini Project: SDN + Socket Programming
│   ├── network_intrusion_detection/          # Working SDN Intrusion Detection & Response implementation
│   │   ├── server.py                         # Protected TCP server on port 8080 (~40 lines)
│   │   ├── client.py                         # Legitimate TCP client (~35 lines)
│   │   ├── attacker.py                       # Port scanner & connection flooder (~50 lines)
│   │   ├── controller.py                     # Ryu OpenFlow 1.3 controller with dynamic drop flow (~115 lines)
│   │   ├── topology.py                       # Mininet 3-host, 1-switch topology (~40 lines)
│   │   ├── README.md                         # Quick start & testing guide
│   │   └── advanced/                         # Test suite, 5-phase demo showcase & benchmark tools
│   ├── network-intrusion-detection-guide.md  # Comprehensive Project Guide & Viva Masterclass
│   ├── project.md                            # Assigned project specification (Project 25)
│   ├── SDN-Socket Programming-Guidelines_Rubrics.pdf # Official evaluation guidelines
│   └── SDN-Socket Programming-Guidelines_Rubrics.txt # Plain-text rubric
│
└── resources/                                # 📚 Official course slides, textbooks & references
    ├── Unit 1/                               # Network Fundamentals & Application Layer
    │   ├── Slides_Unit_1_Part_1.pdf
    │   ├── Slides_Unit_1_Part_2.pdf
    │   └── CN_Chapter1_Reference.md          # Comprehensive Chapter 1 reference notes
    ├── Unit 2/                               # Transport Layer & Socket Programming
    │   ├── Slides_Unit_2_Part_1.pdf
    │   ├── Slides_Unit_2_Part_2.pdf
    │   └── PythonScripts-Socket programming/ # Reference socket scripts (Echo, UDP, TCP)
    ├── SDN-Socket Programming Project/       # Mininet Ubuntu installation guide & 30 Projects list
    ├── Textbook & Course Info/               # Kurose & Ross (8th & 9th Ed), syllabus, evaluation policy
    ├── Formulae_Sheet_Units_1_and_2.pdf      # Complete formulae sheet for Units 1 & 2
    ├── Extra Problems.pdf                    # Practice numerical problems
    └── archive/                              # Original student share archive (.zip)
```

---

## Quick Navigation

### 1. Working on the Mini Project
* **Main Implementation:** [`project/network_intrusion_detection/`](file:///mnt/shared/sem3/CN/project/network_intrusion_detection/)
* **Project Guide & Viva Answers:** [`project/network-intrusion-detection-guide.md`](file:///mnt/shared/sem3/CN/project/network-intrusion-detection-guide.md)
* **To run the project in Mininet:**
  ```bash
  cd /mnt/shared/sem3/CN/project/network_intrusion_detection
  ryu-manager controller.py --verbose     # Terminal 1: Controller
  sudo python3 topology.py                 # Terminal 2: Mininet
  ```

### 2. Accessing Labs & Instruction Manuals
* **Lab 1 (Cisco Packet Tracer):** [`labs/lab1_cisco/`](file:///mnt/shared/sem3/CN/labs/lab1_cisco/)
* **Lab 2 (HTTP Wireshark):** [`labs/lab2_wireshark/`](file:///mnt/shared/sem3/CN/labs/lab2_wireshark/)
* **Lab 3 (DNS/UDP Wireshark):** [`labs/lab3_wireshark/`](file:///mnt/shared/sem3/CN/labs/lab3_wireshark/)
* **Lab 4 (TCP Wireshark):** [`labs/lab4_wireshark/`](file:///mnt/shared/sem3/CN/labs/lab4_wireshark/)
* **Lab 6 (Hardware):** [`labs/lab6_hardware/`](file:///mnt/shared/sem3/CN/labs/lab6_hardware/)
* **VM & Wireshark Setup Guides:** [`labs/setup_and_tools/`](file:///mnt/shared/sem3/CN/labs/setup_and_tools/)

### 3. Studying Course Material
* **Textbook (Kurose & Ross 8th/9th ed):** [`resources/Textbook & Course Info/`](file:///mnt/shared/sem3/CN/resources/Textbook%20&%20Course%20Info/)
* **Formulae Sheet:** [`resources/Formulae_Sheet_Units_1_and_2.pdf`](file:///mnt/shared/sem3/CN/resources/Formulae_Sheet_Units_1_and_2.pdf)
* **Lecture Slides:** [`resources/Unit 1/`](file:///mnt/shared/sem3/CN/resources/Unit%201/) and [`resources/Unit 2/`](file:///mnt/shared/sem3/CN/resources/Unit%202/)
