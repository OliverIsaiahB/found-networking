# netlab/

Tiny Python programs that make networking concepts concrete, built up while
learning networking fundamentals. Read them as much as run them.

## Modules
- `address.py`    — what an IP address is; validating a dotted quad
- `layers.py`     — the OSI / TCP-IP layered model
- `dns_lookup.py` — resolving a name to an address with DNS
- `tcp_client.py` — opening a real TCP connection (the handshake)
- `ports.py`      — ports and well-known service numbers
- `subnet.py`     — subnetting: network vs host bits, CIDR, masks
- `routing.py`    — local-vs-gateway routing decisions
- `diagnose.py`   — ping / traceroute / netstat, mapped to layers

## Troubleshooting cheatsheet
- Can't reach a host at all?      -> `ping` it (Internet layer).
- Reachable, but where does it die? -> `traceroute` to see the failing hop.
- Is my own service even listening? -> `netstat` for local ports/state.
