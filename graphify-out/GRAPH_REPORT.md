# Graph Report - CN  (2026-11-04)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 814 nodes · 2124 edges · 48 communities (35 shown, 13 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 193 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b899c83b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 12
- Community 13
- Community 14
- Community 15
- Community 16
- Community 17
- Community 18
- Community 19
- Community 20
- Community 21
- Community 22
- Community 23
- Community 24
- Community 25
- Community 26
- Community 27
- Community 28
- Community 29
- Community 30
- Community 31
- Community 32
- Community 34
- Community 35
- Community 36
- Community 37
- Community 38
- Community 39
- Community 40
- Community 41
- Community 42
- Community 43
- Community 45
- Community 47

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
- `add()` --indirect_call--> `e()`  [INFERRED]
  site/assets/javascripts/workers/search.c47bb847.min.js → site/assets/javascripts/bundle.77dd0ce9.min.js
- `ShowcaseRunner` --uses--> `IDSMonitor`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/demo.py → project/first_presentation/network_intrusion_detection/advanced/ids_monitor.py
- `IDSMonitor` --uses--> `SecurityAlert`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/ids_monitor.py → project/first_presentation/network_intrusion_detection/advanced/protocol.py
- `TestIntrusionDetectionSystem` --uses--> `IDSMonitor`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/test_suite.py → project/first_presentation/network_intrusion_detection/advanced/ids_monitor.py
- `TestIntrusionDetectionSystem` --uses--> `StandaloneMockController`  [INFERRED]
  project/first_presentation/network_intrusion_detection/advanced/test_suite.py → project/first_presentation/network_intrusion_detection/advanced/sdn_controller.py

## Import Cycles
- None detected.

## Communities (48 total, 13 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.07
Nodes (93): Ac(), ae(), af(), Ap(), Ar(), b(), bc(), bf() (+85 more)

### Community 1 - "Community 1"
Cohesion: 0.06
Nodes (62): A(), add(), ae(), At(), B(), bt(), C(), ce() (+54 more)

### Community 2 - "Community 2"
Cohesion: 0.04
Nodes (43): Ba(), Cl(), Cs(), D(), ea(), ei(), fc(), ff() (+35 more)

### Community 3 - "Community 3"
Cohesion: 0.05
Nodes (4): print_banner(), ShowcaseRunner, TCPClient, TCPServer

### Community 4 - "Community 4"
Cohesion: 0.07
Nodes (4): BaseControllerLogic, main(), SDNControllerApp, StandaloneMockController

### Community 5 - "Community 5"
Cohesion: 0.15
Nodes (6): main(), main(), main(), format_alert_log(), main(), main()

### Community 6 - "Community 6"
Cohesion: 0.16
Nodes (25): e(), B(), c(), d(), E(), f(), h(), Jr() (+17 more)

### Community 7 - "Community 7"
Cohesion: 0.14
Nodes (25): ao(), at(), bi(), co(), eo(), ft(), gn(), ia() (+17 more)

### Community 8 - "Community 8"
Cohesion: 0.09
Nodes (22): activation_command, activation_command_timeout, added_modes, default_modes, encoding, excluded_tools, fixed_tools, ignore_all_files_in_gitignore (+14 more)

### Community 9 - "Community 9"
Cohesion: 0.19
Nodes (19): c(), dr(), f(), Fa(), gf(), l(), nu(), o() (+11 more)

### Community 11 - "Community 11"
Cohesion: 0.15
Nodes (21): Bu(), ds(), Du(), ep(), fp(), gt(), Gu(), Ir() (+13 more)

### Community 12 - "Community 12"
Cohesion: 0.15
Nodes (5): connection_flood(), main(), port_scan(), main(), send_request()

### Community 13 - "Community 13"
Cohesion: 0.15
Nodes (20): Ai(), an(), Ci(), cn(), di(), dn(), El(), hi() (+12 more)

### Community 15 - "Community 15"
Cohesion: 0.14
Nodes (17): bn(), cu(), Fr(), Ga(), lo(), Mr(), np(), pe() (+9 more)

### Community 16 - "Community 16"
Cohesion: 0.15
Nodes (15): au(), bt(), Da(), es(), Hu(), ko(), na(), se() (+7 more)

### Community 19 - "Community 19"
Cohesion: 0.20
Nodes (4): find_available_port(), ProtectedServer, run_demonstration(), SDNIntrusionController

### Community 20 - "Community 20"
Cohesion: 0.24
Nodes (5): calculate_metrics(), export_reports(), load_json_safe(), main(), print_comparison_table()

### Community 22 - "Community 22"
Cohesion: 0.18
Nodes (11): markdown_extensions, pymdownx.highlight, pymdownx.tabbed, pymdownx.tasklist, toc, anchor_linenums, line_spans, pygments_lang_class (+3 more)

### Community 23 - "Community 23"
Cohesion: 0.18
Nodes (11): nav, Formulae Sheet, Home, Master Index & Study Checklist, Unit 2: Transport Layer, Unit 4: Link Layer & LAN, Chapter 3: Transport Layer, Complete Unit 2 Notes (+3 more)

### Community 24 - "Community 24"
Cohesion: 0.18
Nodes (11): accent, primary, scheme, toggle, theme, custom_dir, features, name (+3 more)

### Community 25 - "Community 25"
Cohesion: 0.33
Nodes (10): a(), li(), c(), l(), o(), s(), Tl(), Zr() (+2 more)

### Community 27 - "Community 27"
Cohesion: 0.31
Nodes (4): clean_processes(), run_experiment.sh script, show_help(), run_tests()

### Community 28 - "Community 28"
Cohesion: 0.22
Nodes (9): Do(), fs(), Ju(), ku(), lu(), Qa(), Vu(), wu() (+1 more)

### Community 29 - "Community 29"
Cohesion: 0.22
Nodes (9): property, provider, extra, analytics, social, version, icon, link (+1 more)

### Community 30 - "Community 30"
Cohesion: 0.32
Nodes (8): Bp(), Gp(), Gr(), nc(), oc(), qp(), vn(), Yp()

### Community 31 - "Community 31"
Cohesion: 0.57
Nodes (8): ui(), a(), c(), f(), l(), p(), s(), u()

### Community 32 - "Community 32"
Cohesion: 0.25
Nodes (7): copyright, extra_javascript, repo_name, repo_url, site_description, site_name, site_url

### Community 35 - "Community 35"
Cohesion: 0.40
Nodes (5): ns(), rn(), tn(), vi(), xl()

### Community 36 - "Community 36"
Cohesion: 0.40
Nodes (5): Unit 1: Internet & Application Layer, Chapter 1: Computer Networks & the Internet, Chapter 2: Application Layer, Complete Unit 1 Notes, Overview & Syllabus

### Community 37 - "Community 37"
Cohesion: 0.50
Nodes (4): as(), be(), ge(), jo()

### Community 38 - "Community 38"
Cohesion: 0.50
Nodes (4): dl(), en(), ml(), oa()

### Community 39 - "Community 39"
Cohesion: 0.67
Nodes (3): constructor(), iu(), yt()

### Community 40 - "Community 40"
Cohesion: 0.67
Nodes (3): fo(), Ie(), wl()

### Community 41 - "Community 41"
Cohesion: 0.67
Nodes (3): is(), pu(), Ya()

### Community 43 - "Community 43"
Cohesion: 0.67
Nodes (3): Unit 3: Network Layer, Complete Unit 3 Notes, Overview

## Knowledge Gaps
- **13 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `e()` connect `Community 6` to `Community 0`, `Community 1`, `Community 2`, `Community 35`, `Community 7`, `Community 9`, `Community 11`, `Community 13`, `Community 15`, `Community 25`, `Community 28`, `Community 30`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 24 inferred relationships involving `e()` (e.g. with `bi()` and `d()`) actually correct?**
  _`e()` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.0729955348476024 - nodes in this community are weakly interconnected._
- **Why does `se()` connect `Community 1` to `Community 6`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 27 inferred relationships involving `t()` (e.g. with `bundle.77dd0ce9.min.js` and `Cr()`) actually correct?**
  _`t()` has 27 INFERRED edges - model-reasoned connections that need verification._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.06335403726708075 - nodes in this community are weakly interconnected._
- **Why does `BaseControllerLogic` connect `Community 4` to `Community 18`, `Community 27`?**
  _High betweenness centrality (0.015) - this node is a cross-community bridge._