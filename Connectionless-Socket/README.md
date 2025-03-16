# 📨 UDP Chat Application with Simulated Packet Loss

This project is a **UDP-based client-server chat application** built using Python's `socket` module. Unlike TCP, **UDP (User Datagram Protocol)** does not guarantee message delivery, making it a **connectionless communication** protocol.  

Additionally, this implementation introduces **simulated packet loss**—the server **randomly drops 30% of incoming messages** to demonstrate the unreliable nature of UDP.(we can change drop amount time)

---

## 🚀 Features
- **Connectionless Communication** using UDP.
- **Simulated Packet Loss (30%)** for real-world testing.
- **Message Exchange Between Client and Server**.
- **Graceful Disconnection** when the client sends `"exit"`.

---

## 📌 Requirements
- Python 3.x installed on your system.

---

## 🔧 Setup & Usage

### **1️⃣ Run the Server**
Open a terminal and run:
```bash
python server.py
# UDP Client-Server Communication with Simulated Packet Loss

## 2️⃣ Run the Client
Open another terminal and run:

```bash
python client.py
```

The client will allow sending messages to the server.

## 🛠️ How It Works
A socket is an endpoint for sending and receiving data over a network. This application uses UDP sockets for communication.

### 🔹 Steps in UDP Client-Server Communication

#### Server Initialization
- The server creates a UDP socket and binds it to an IP and port.
- It continuously listens for messages from clients.

#### Client Sends Message
- The client creates a UDP socket and sends a message to the server.

#### Simulated Packet Loss (30%)
- The server drops 30% of incoming messages randomly.
- If a message is dropped, the server does not respond.

#### Client Receives Response
- If the server processes the message, it replies with "Message received".
- If no response is received (packet loss), the client detects it and displays an appropriate message.

#### Exit Mechanism
- When the client sends "exit", the server recognizes it and stops responding.
- The client closes its socket.


## 📌 Expected Output

### 🖥️ Server Terminal

```sql
UDP Server is listening...
Received from ('127.0.0.1', 54302): Hello Server!
Received from ('127.0.0.1', 54302): How are you?
Simulating packet loss. Ignoring message from ('127.0.0.1', 54302)
Received from ('127.0.0.1', 54302): What's up?
Client disconnected.
```

### 💻 Client Terminal

```pgsql
Enter message (type 'exit' to disconnect): Hello Server!
Server: Message received
Enter message (type 'exit' to disconnect): How are you?
Server: Message received
Enter message (type 'exit' to disconnect): What's up?
No response received. Server might be ignoring messages.
Enter message (type 'exit' to disconnect): exit
Closing connection.
```

## 🎯 Notes
- UDP does not guarantee message delivery, making it faster but unreliable.
- Packet loss (30%) is simulated intentionally to demonstrate the unreliable nature of UDP.
- The client detects message loss if no response is received within 2 seconds.

## 📜 License
This project is open-source and licensed under the MIT License.
