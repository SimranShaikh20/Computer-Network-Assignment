import socket
import random  # Import for simulating packet loss

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))

print("UDP Server is listening...")

while True:
    try:
        data, client_address = server_socket.recvfrom(1024)

        if random.random() < 0.3:  # 30% chance to drop a packet
            print(f"Simulating packet loss. Ignoring message from {client_address}")
            continue  # Skip responding

        print(f"Received from {client_address}: {data.decode()}")

        if data.decode().lower() == "exit":
            print("Client disconnected.")
            continue  # Don't send a response for exit

        response_message = "Message received"
        server_socket.sendto(response_message.encode(), client_address)

    except Exception as e:
        print(f"Error: {e}")
