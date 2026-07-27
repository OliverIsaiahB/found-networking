"""Subnetting: splitting an address into a NETWORK part and a HOST part."""

# An IP address has two parts. The leftmost bits identify the NETWORK;
# the rest identify the HOST within it. CIDR notation /n says how many
# leading bits are the network part.
#
#   192.168.1.10 /24
#   |__________|  |__|
#    network(24)  host(8 bits) -> up to 254 usable hosts
#
def to_int(ip: str) -> int:
    """Pack a dotted quad into a single 32-bit integer."""
    a, b, c, d = (int(p) for p in ip.split("."))
    return (a << 24) | (b << 16) | (c << 8) | d


def to_ip(n: int) -> str:
    """Unpack a 32-bit integer back into a dotted quad."""
    return f"{(n >> 24) & 255}.{(n >> 16) & 255}.{(n >> 8) & 255}.{n & 255}"


def network_address(ip: str, prefix: int) -> str:
    """Zero out the host bits to get the network's base address."""
    mask = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
    return to_ip(to_int(ip) & mask)
