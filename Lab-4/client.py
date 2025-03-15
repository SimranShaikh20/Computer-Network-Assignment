import socket

HOST = "127.0.0.1"  # Server address (localhost)
PORT = 5555         # Port to connect to

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter message (type 'exit' to disconnect): ")
    client_socket.sendall(message.encode("utf-8"))

    if message.strip().lower() == "exit":
        break

    response = client_socket.recv(1024).decode("utf-8")
    print(response)

client_socket.close()
print("Connection closed.")
