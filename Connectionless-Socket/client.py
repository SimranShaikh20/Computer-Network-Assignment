import socket
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("127.0.0.1", 12345)

while True:
    message = input("Enter message (type 'exit' to disconnect): ")

    if message.lower() == "exit":
        print("Closing connection.")
        client_socket.sendto(message.encode(), server_address)
        break  # Exit loop

    if random.random() < 0.1:  # 30% chance to drop a packet (client-side)
        print("Simulating packet loss. Message not sent.")
        continue  # Skip sending the message

    client_socket.sendto(message.encode(), server_address)  # Send data

    try:
        client_socket.settimeout(2)  # Set timeout for receiving response
        response, _ = client_socket.recvfrom(1024)
        print("Server:", response.decode())
    except socket.timeout:
        print("No response received. Server might be ignoring messages.")
    except ConnectionResetError:
        print("Connection reset by server. Server might have dropped the packet.")

client_socket.close()
