"""What an IP address is, made concrete."""

# An IPv4 address is 32 bits, written as four 0-255 numbers ("dotted quad").
#   192 . 168 . 1 . 10   ->  one machine on a network
EXAMPLE = "192.168.1.10"


def octets(ip: str) -> list[int]:
    """Split a dotted-quad string into its four numbers."""
    return [int(part) for part in ip.split(".")]


def is_valid_ipv4(ip: str) -> bool:
    """An IPv4 address has exactly four parts, each 0..255."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    return all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)


if __name__ == "__main__":
    print(f"address: {EXAMPLE}")
    print(f"octets:  {octets(EXAMPLE)}")
    print(f"valid?   {is_valid_ipv4(EXAMPLE)}")
