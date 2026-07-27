"""Open a real TCP connection and see the transport layer at work."""
import socket


def connect(host: str, port: int, timeout: float = 3.0) -> str:
    """Open a TCP connection, then close it. Return what happened."""
    # AF_INET = IPv4, SOCK_STREAM = TCP (a reliable, ordered byte stream).
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        # connect() performs the TCP three-way handshake under the hood.
        sock.connect((host, port))
        return f"connected to {host}:{port} (handshake completed)"
    except OSError as err:
        return f"could not connect to {host}:{port}: {err}"
    finally:
        sock.close()


if __name__ == "__main__":
    # Many systems run an echo-like service; adjust host/port as needed.
    print(connect("localhost", 22))
