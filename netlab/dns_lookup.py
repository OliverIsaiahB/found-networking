"""DNS: turning a human name into a machine address."""
import socket


def resolve(hostname: str) -> str:
    """Ask the system resolver for the IP address behind a name."""
    # gethostbyname performs a DNS lookup and returns one IPv4 address.
    return socket.gethostbyname(hostname)


def explain(hostname: str) -> None:
    ip = resolve(hostname)
    # You type a NAME; the network routes by the ADDRESS DNS returned.
    print(f"name '{hostname}' resolves to address {ip}")


if __name__ == "__main__":
    # Resolving localhost works without any network.
    explain("localhost")
