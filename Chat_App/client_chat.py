import socket
import threading

HOST = "127.0.0.1"  # Server address (localhost)
PORT = 5555         # Port to connect to

# Function to receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            response = client_socket.recv(1024).decode("utf-8")
            if not response:
                break
            print(response)
        except ConnectionResetError:
            print("[ERROR] Connection lost with server.")
            break

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start a separate thread to receive messages
threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

while True:
    message = input()
    client_socket.send(message.encode("utf-8"))

    if message.strip().lower() == "exit":
        print("Disconnecting from server...")
        break

client_socket.close()
print("Connection closed.")
