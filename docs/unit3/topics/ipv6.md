# IPv6 (Chapter 4/5)

## IPv6 Rationale
- **Larger address space**: 128-bit (340 undecillion addresses)
- **Better header format**: 40-byte fixed length header
- **No checksum**: Removed to speed processing
- **No fragmentation/reassembly**: Only sender fragments
- **Options**: Available as extension headers (Next Header field)
- **Flow label**: Identify datagrams in same "flow"
- **ICMPv6**: New version of ICMP

## IPv6 Datagram Format
```
32 bits
ver | pri | flow label (20 bits) | payload len | next hdr | hop limit
128-bit source address
128-bit destination address
payload
```
**Missing from IPv4**: No checksum, no fragmentation, no options in base header

## IPv6 Address Notation
- 128 bits = eight 16-bit blocks (hextets)
- Separated by colons ':'
- Hexadecimal (each hex char = 4 bits)
- **Compression rules**:
  1. Discard leading zeros in each block
  2. Replace consecutive all-zero blocks with `::` (only once!)
  3. Example: `2001:0db8:0000:0000:0000:ff00:0042:8329` → `2001:db8::ff00:42:8329`

## IPv6 Address Types
1. **Unicast** (one-to-one): Single interface
2. **Multicast** (one-to-many): Group of interfaces
3. **Anycast** (one-to-nearest): Group sharing address; delivered to closest
4. **No broadcast**: Implemented via multicast

## Transition from IPv4 to IPv6
- **Tunneling**: IPv6 datagram carried as payload in IPv4 datagram among IPv4 routers
- **Dual stack**: Nodes run both IPv4 and IPv6
- **NAT64/DNS64**: Translation mechanisms