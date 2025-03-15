import socket

HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 5555       # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server is listening on port {PORT}...")

while True:  # Main server loop
    client_socket, client_address = server_socket.accept()
    print(f"[INFO] Connected with {client_address[0]}:{client_address[1]}")

    while True:  # Handle messages from the client
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break  # If no data, client disconnected

        print(f"Client: {data}")

        if data.strip().lower() == "exit":
            print("[INFO] Client requested disconnection.")
            client_socket.sendall("Server: Goodbye!".encode("utf-8"))
            client_socket.close()
            server_socket.close()  # Close the server
            print("[INFO] Server shutting down.")
            exit(0)  # Terminate the program

        client_socket.sendall("Server: Message received".encode("utf-8"))

    client_socket.close()
    print("[INFO] Connection closed.")
