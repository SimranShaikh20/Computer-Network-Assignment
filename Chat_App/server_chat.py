import socket
import threading

HOST = "127.0.0.1"  # Server IP (localhost)
PORT = 5555         # Port to listen on

# Global flag to stop the server
server_running = True

# Function to handle communication with each client
def handle_client(client_socket, client_address):
    global server_running
    print(f"[NEW CONNECTION] {client_address} connected.")

    client_socket.send("Welcome to the chat server! What's your name?".encode("utf-8"))
    
    user_name = client_socket.recv(1024).decode("utf-8").strip()
    print(f"[{client_address}] Username: {user_name}")
    
    client_socket.send(f"Hello {user_name}, you are now connected!".encode("utf-8"))

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8").strip()
            if not message:
                break  # If no data received, client disconnected

            print(f"[{user_name}] {message}")

            if message.lower() == "exit":
                print(f"[{user_name}] Disconnected. Shutting down server...")
                client_socket.send("Server is shutting down. Goodbye!".encode("utf-8"))
                server_running = False  # Stop the server
                break

            response_message = f"Server: I received your message - '{message}'"
            client_socket.send(response_message.encode("utf-8"))
        except ConnectionResetError:
            print(f"[ERROR] Connection lost with {client_address}")
            break

    client_socket.close()
    print(f"[CONNECTION CLOSED] {client_address}")

# Create and bind the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Listen for up to 5 connections

print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

while server_running:
    try:
        server_socket.settimeout(1)  # Prevent blocking
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()
    except socket.timeout:
        continue  # Allow checking of `server_running` flag

print("[SERVER] Shutting down...")
server_socket.close()
