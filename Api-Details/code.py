import socket

try:
    # Get the port number for HTTP over TCP
    http_port = socket.getservbyname('http', 'tcp')
    print(f"Port for HTTP over TCP: {http_port}")

    # Get the protocol number for TCP
    tcp_protocol = socket.getprotobyname('tcp')
    print(f"Protocol number for TCP: {tcp_protocol}")

    # Get the IP address of a hostname (google.com)
    hostname = 'google.com'
    ip_address = socket.gethostbyname(hostname)
    print(f"IP Address of {hostname}: {ip_address}")

except socket.error as e:
    print(f"Socket error occurred: {e}")
