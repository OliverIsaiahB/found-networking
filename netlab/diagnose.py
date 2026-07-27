"""A reference for the three first-reach troubleshooting tools."""

# Each tool answers a different question at a different layer.
TOOLS = {
    "ping": {
        "asks":  "is the host reachable at all?",
        "layer": "Internet (IP) — sends ICMP echo, waits for a reply",
    },
    "traceroute": {
        "asks":  "what PATH do packets take, and where do they stop?",
        "layer": "Internet (IP) — reveals each router hop to the target",
    },
    "netstat": {
        "asks":  "what connections and listening ports exist on MY host?",
        "layer": "Transport — lists local sockets, ports, and their state",
    },
}


def explain(tool: str) -> str:
    info = TOOLS[tool]
    return f"{tool}: {info['asks']}  [{info['layer']}]"
