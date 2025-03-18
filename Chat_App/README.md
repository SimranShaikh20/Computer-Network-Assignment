# 📢 TCP Chat Application

This is a simple **Chat Server and Client** implementation using Python's `socket` and `threading` modules. It enables multiple clients to connect to a server and exchange messages in a connected-oriented communication (TCP-based chat).

## 🚀 Features
- 🖥️ **Multi-client support** - Multiple clients can connect to the server simultaneously.
- 💬 **Two-way communication** - Clients can send and receive messages.
- 🛑 **Graceful shutdown** - Clients can exit by typing `exit`, which also shuts down the server.
- ⚡ **Threading** - Each client runs on a separate thread to allow concurrent connections.

---

## ⚙️ How It Works

### 1️⃣ Server (`server.py`)
The server listens for incoming connections and handles each client in a separate thread. When a client connects:
1. **`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`** - Creates a TCP socket.
2. **`bind((HOST, PORT))`** - Binds the socket to a specific IP and port.
3. **`listen(5)`** - Allows up to 5 clients to connect simultaneously.
4. **`accept()`** - Accepts a new client connection.
5. **`recv(1024).decode("utf-8")`** - Receives messages from clients.
6. **`send()`** - Sends responses to clients.
7. **`threading.Thread(target=handle_client, args=(client_socket, client_address))`** - Runs each client in a separate thread.

If a client sends `exit`, the server shuts down gracefully. 🛑

### 2️⃣ Client (`client.py`)
The client connects to the server and enables message exchange:
1. **`socket.socket(socket.AF_INET, socket.SOCK_STREAM)`** - Creates a TCP client socket.
2. **`connect((HOST, PORT))`** - Connects to the server.
3. **`send()`** - Sends messages to the server.
4. **`recv(1024).decode("utf-8")`** - Receives and prints responses from the server.
5. **`threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()`** - Listens for server messages in a separate thread.

---

## 🔧 Setup & Usage

### 🏗️ Prerequisites
Ensure you have **Python 3.x** installed.

### 💻 Running the Server
1. Open a terminal and navigate to the project directory.
2. Run the server script:
   ```sh
   python server.py
   ```
   The server will start listening for incoming connections.

### 📲 Running the Client
1. Open another terminal and navigate to the project directory.
2. Run the client script:
   ```sh
   python client.py
   ```
3. Enter a username when prompted.
4. Start chatting! 🎉
5. Type `exit` to disconnect and shut down the server.

---

## 📌 Example Usage
### Server Output:
```
[LISTENING] Server is listening on 127.0.0.1:5555
[NEW CONNECTION] ('127.0.0.1', 54321) connected.
[('127.0.0.1', 54321)] Username: Simran
[Simran] Hello
[Simran] How are you?
[Simran] exit
[Simran] Disconnected. Shutting down server...
[SERVER] Shutting down...
```

### Client Output:
```
Welcome to the chat server! What's your name?
Enter your name: Simran
Hello Simran, you are now connected!
Hello
Server: I received your message - 'Hello'
How are you?
Server: I received your message - 'How are you?'
exit
Disconnecting from server...
Connection closed.
```

---

## 🛠️ Technologies Used
- 🐍 Python
- 🖧 `socket` (for networking)
- ⚡ `threading` (for concurrent connections)

## 🙌 Contributions
Feel free to contribute or suggest improvements! 🤝

---

Happy Coding! 🎉🚀

