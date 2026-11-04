# ICMP (Internet Control Message Protocol)

## Services
- Used by hosts and routers to communicate network-layer information
- Error reporting: unreachable host/network/port/protocol
- Echo request/reply (used by ping)
- Carried as IP payloads (network-layer "above" IP)

## Common ICMP Types
| Type | Code | Description |
|------|------|-------------|
| 0 | 0 | Echo reply (ping) |
| 3 | 0 | Destination network unreachable |
| 3 | 1 | Destination host unreachable |
| 3 | 2 | Destination protocol unreachable |
| 3 | 3 | Destination port unreachable |
| 8 | 0 | Echo request (ping) |
| 11 | 0 | TTL expired (used by traceroute) |
| 12 | 0 | Bad IP header |

## Utilities
- **ping**: Uses ICMP echo request/reply
- **traceroute**: Uses ICMP TTL expired messages