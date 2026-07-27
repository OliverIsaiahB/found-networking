"""How a host decides: deliver locally, or hand off to the router?"""
from netlab.subnet import network_address


def same_network(ip_a: str, ip_b: str, prefix: int) -> bool:
    """True if both addresses are on the same subnet."""
    return network_address(ip_a, prefix) == network_address(ip_b, prefix)


def next_hop(src: str, dst: str, prefix: int, gateway: str) -> str:
    """Decide where a packet to `dst` goes first."""
    if same_network(src, dst, prefix):
        # On my own network: deliver directly, no router needed.
        return f"deliver directly to {dst}"
    # Off my network: send to the default gateway (the router).
    return f"send to gateway {gateway} (router forwards onward)"


if __name__ == "__main__":
    src, prefix, gw = "192.168.1.10", 24, "192.168.1.1"
    print(next_hop(src, "192.168.1.50", prefix, gw))   # local
    print(next_hop(src, "93.184.216.34", prefix, gw))  # remote
