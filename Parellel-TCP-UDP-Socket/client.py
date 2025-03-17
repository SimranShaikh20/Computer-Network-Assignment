import socket
import random

def tcp_client(message):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 65432))
        client.sendall(message.encode())
        response = client.recv(1024).decode()
        print(f"[TCP Client] Server responded: {response}")
        client.close()
    except Exception as e:
        print(f"[TCP Client] Error: {e}")

def udp_client(message):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_address = ('127.0.0.1', 65433)
        client.sendto(message.encode(), server_address)
        response, addr = client.recvfrom(1024)
        print(f"[UDP Client] Server responded: {response}")
        client.close()
    except Exception as e:
        print(f"[UDP Client] Error: {e}")

while True:
    user_input = input("Enter message to send (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting client...")
        tcp_client("exit")  # Send shutdown command
        udp_client("exit")  # Send shutdown command
        break

    # Randomly choose between TCP and UDP
    if random.choice(["TCP", "UDP"]) == "TCP":
        tcp_client(user_input)
    else:
        udp_client(user_input)
