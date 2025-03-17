import socket
import threading

# Shared flag to stop the server
server_running = True

# TCP Server Function
def tcp_server():
    global server_running
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 65432))
    server.listen(5)
    print("[TCP Server] Listening on port 65432...")

    while server_running:
        try:
            server.settimeout(1)  # Prevent blocking while checking stop condition
            conn, addr = server.accept()
            data = conn.recv(1024).decode()
            print(f"[TCP Server] Received from {addr}: {data}")

            if data.lower() == "exit":
                print("[TCP Server] Shutdown command received. Stopping server...")
                server_running = False
                conn.sendall("[TCP Server] Server shutting down...".encode())
                conn.close()
                break

            conn.sendall("[TCP Server] Your message was received!".encode())
            conn.close()
        except socket.timeout:
            continue  # Allow checking stop condition

    server.close()

# UDP Server Function
def udp_server():
    global server_running
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('127.0.0.1', 65433))
    print("[UDP Server] Listening on port 65433...")

    while server_running:
        try:
            server.settimeout(1)  # Prevent blocking while checking stop condition
            data, addr = server.recvfrom(1024)
            message = data.decode()
            print(f"[UDP Server] Received from {addr}: {message}")

            if message.lower() == "exit":
                print("[UDP Server] Shutdown command received. Stopping server...")
                server_running = False
                server.sendto("[UDP Server] Server shutting down...".encode(), addr)
                break

            server.sendto("[UDP Server] Your message was received!".encode(), addr)
        except socket.timeout:
            continue  # Allow checking stop condition

    server.close()

# Running both servers in parallel
tcp_thread = threading.Thread(target=tcp_server)
udp_thread = threading.Thread(target=udp_server)

tcp_thread.start()
udp_thread.start()

tcp_thread.join()
udp_thread.join()

print("[Server] All services stopped.")
