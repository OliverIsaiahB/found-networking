"""The networking stack as layers, each handling one concern."""

# A text diagram of the stack. Data travels DOWN as it is sent, each layer
# wrapping (encapsulating) the layer above, and UP as it is received.
#
#   OSI (7 layers)        TCP/IP (4 layers)     example
#   -----------------     -----------------     --------------------
#   7 Application   \
#   6 Presentation   >--- Application          HTTP, DNS
#   5 Session       /
#   4 Transport    ------- Transport           TCP, UDP, ports
#   3 Network      ------- Internet            IP addresses, routing
#   2 Data Link    \
#   1 Physical      >----- Link                Ethernet, Wi-Fi, cables
#
TCP_IP_LAYERS = ["Application", "Transport", "Internet", "Link"]


def describe(layer: str) -> str:
    jobs = {
        "Application": "what the user's program speaks (HTTP, DNS)",
        "Transport":   "end-to-end delivery and ports (TCP, UDP)",
        "Internet":    "addressing and routing between networks (IP)",
        "Link":        "moving bits over one physical hop (Ethernet)",
    }
    return f"{layer}: {jobs[layer]}"
