# Client-Server Chat Application (Python Sockets)

This project is a **simple client-server chat application** built using Python's `socket` module. The **server** listens for connections and responds to messages sent by the **client**. The connection remains open until the client sends `"exit"`, at which point both the server and client close.

---

## 🚀 Features
- Two-way communication between client and server.
- Server can handle multiple messages from the client.
- Gracefully handles client disconnection.
- Server shuts down when `"exit"` is received.

---

## 📌 Requirements
- Python 3.x installed on your system.

---

## 🔧 Setup & Usage

### **1️⃣ Run the Server**
Open a terminal and run:
```bash
python server.py
```
The server starts and listens for client connections.

### **2️⃣ Run the Client**
Open another terminal and run:
```bash
python client.py
```
The client will connect to the server and allow you to send messages.

---

## 🛠️ How Sockets Work
A **socket** is an endpoint for sending and receiving data across a network. In this chat application, both the client and the server communicate using **TCP (Transmission Control Protocol)** sockets.

### **🔹 Steps in a Client-Server Socket Communication**
1. **Server Initialization**
   - The server creates a socket and binds it to an IP address and port.
   - It then listens for incoming client connections.

2. **Client Connection**
   - The client creates a socket and connects to the server using its IP address and port.

3. **Data Transmission**
   - The client sends a message to the server.
   - The server receives the message and sends a response.
   - This process continues until the client sends an "exit" command.

4. **Connection Termination**
   - When the client sends "exit", the server acknowledges it and both close their sockets.

### **🔹 Diagram of Socket Communication**
```
Client                              Server
   |                                   |
   | ---- Connect to Server ---->     |
   |                                   |
   | ---- Send Message 1 ---->         |
   |                                   |
   | <--- Respond to Message 1 ----    |
   |                                   |
   | ---- Send Message 2 ---->         |
   |                                   |
   | <--- Respond to Message 2 ----    |
   |                                   |
   | ---- Send "exit" ---->            |
   |                                   |
   | <--- Acknowledge "exit" ----      |
   |                                   |
   | ---- Close Connection ---->       |
   |                                   |
```

---

## 📌 Expected Output

### **🖥️ Server Terminal**
```
Server is listening on port 5555...
[INFO] Connected with 127.0.0.1:54302
Client: Hello Server!
Client: exit
[INFO] Client requested disconnection.
[INFO] Server shutting down.
```

### **💻 Client Terminal**
```
Enter message (type 'exit' to disconnect): Hello Server!
Server: Message received
Enter message (type 'exit' to disconnect): exit
Server: Goodbye!
Connection closed.
```

---

## 🎯 Notes
- The server should be started before running the client.
- The client and server should be run in separate terminal windows.
- The server exits when the client sends `"exit"`.

---

## 🤝 Contributions
Feel free to contribute by improving the project! Fork the repository and submit a pull request.

---

## 📜 License
This project is open-source and licensed under the MIT License.

---

### ✅ **How to Use**
1. **Save the above content in a file named `README.md`.**
2. **Include it in your project directory.**
3. **Run `server.py` first, then `client.py`.**
