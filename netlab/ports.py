"""Ports: how one machine offers many services at one IP address."""

# An IP address gets you to the HOST. A PORT picks the SERVICE on it.
# Together, (ip, port) names exactly one service endpoint.
WELL_KNOWN = {
    22:  "SSH   (secure shell login)",
    53:  "DNS   (name resolution)",
    80:  "HTTP  (web, unencrypted)",
    443: "HTTPS (web, encrypted)",
}


def endpoint(ip: str, port: int) -> str:
    """Render an (ip, port) pair the way the network thinks of it."""
    service = WELL_KNOWN.get(port, "unknown service")
    return f"{ip}:{port}  ->  {service}"


if __name__ == "__main__":
    for p in (22, 80, 443, 9999):
        print(endpoint("192.168.1.10", p))
