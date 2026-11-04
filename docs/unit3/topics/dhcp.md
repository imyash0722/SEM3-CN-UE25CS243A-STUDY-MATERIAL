# DHCP (Dynamic Host Configuration Protocol)

## Goal
Host dynamically obtains IP address from network server when it "joins" network
- Can renew lease on address in use
- Allows reuse of addresses (only hold while connected/on)
- Supports mobile users

## DORA Process
1. **DHCP Discover**: Client broadcasts (src: 0.0.0.0, dst: 255.255.255.255)
2. **DHCP Offer**: Server responds with IP offer (yiaddr, lease time)
3. **DHCP Request**: Client requests offered IP
4. **DHCP ACK**: Server confirms assignment

## DHCP Returns
- Allocated IP address
- Address of first-hop router (default gateway)
- Name and IP address of DNS server
- Network mask