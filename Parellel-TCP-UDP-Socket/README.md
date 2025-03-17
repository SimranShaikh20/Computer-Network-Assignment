# **Parallel TCP and UDP Communication in Python**

## **📌 Overview**
This project demonstrates how to implement both **connection-oriented (TCP)** and **connectionless (UDP)** communication in Python. The server listens on both protocols **simultaneously**, and the client sends messages randomly using either TCP or UDP.

The key features of this implementation:
- **Parallel TCP and UDP servers** running in the same program.
- **Client randomly chooses TCP or UDP** when sending a message.
- **Exit functionality:** If a client sends "exit", the server shuts down both TCP and UDP servers.
- **Threading is used** to run both servers concurrently.

---

## **📁 Project Structure**
```
|-- socket_communication_project
    |-- server.py  # Runs both TCP and UDP servers
    |-- client.py  # Sends messages randomly using TCP or UDP
    
```

---

## **⚙️ How It Works**

### **🖥️ Server (server.py)**
1. The server creates two sockets:
   - A **TCP socket** that listens for incoming client connections.
   - A **UDP socket** that waits for incoming datagrams.
2. Both sockets run in parallel using **multithreading**.
3. When the server receives a message from a client, it responds accordingly:
   - If the client sends `exit`, the server shuts down.
4. The server continuously listens for new messages unless stopped.

### **💻 Client (client.py)**
1. The client asks for user input.
2. It randomly decides whether to send the message over **TCP or UDP**.
3. The selected protocol is used to send data to the server.
4. If the user types `exit`, the client sends the command to both TCP and UDP servers, shutting them down.

---

## **🚀 How to Run**
### **1️⃣ Start the Server**
Open a terminal and run:
```sh
python server.py
```
This will start both the TCP and UDP servers, listening for incoming messages.

### **2️⃣ Start the Client**
Open another terminal and run:
```sh
python client.py
```
Enter messages to send to the server. The client will randomly use TCP or UDP.

### **3️⃣ Stopping the Server**
To stop the server, send `exit` from the client:
```
Enter message to send (or type 'exit' to quit): exit
```
The server will print shutdown messages and terminate.

---

## **📜 Example Output**

### **Server Output**
```sh
[TCP Server] Listening on port 65432...
[UDP Server] Listening on port 65433...
[TCP Server] Received from ('127.0.0.1', 56789): Hello
[UDP Server] Received from ('127.0.0.1', 56790): Hi there!
[UDP Server] Received from ('127.0.0.1', 56791): exit
[UDP Server] Shutdown command received. Stopping server...
[TCP Server] Shutdown command received. Stopping server...
[Server] All services stopped.
```

### **Client Output**
```sh
Enter message to send (or type 'exit' to quit): Hello
[TCP Client] Server responded: [TCP Server] Your message was received!

Enter message to send (or type 'exit' to quit): Hi there!
[UDP Client] Server responded: [UDP Server] Your message was received!

Enter message to send (or type 'exit' to quit): exit
[UDP Client] Server responded: [UDP Server] Server shutting down...
[TCP Client] Server responded: [TCP Server] Server shutting down...
Exiting client...
```

---

## **🔧 Technical Details**
### **🔹 TCP vs. UDP**
| Feature       | TCP (Connection-Oriented) | UDP (Connectionless) |
|--------------|--------------------------|----------------------|
| Reliability  | Ensures delivery, retransmits lost packets | No guarantee of delivery |
| Speed        | Slower due to acknowledgment overhead | Faster as it doesn’t require acknowledgment |
| Use Cases    | File transfers, web browsing | Streaming, VoIP, gaming |

### **🔹 Key Technologies Used**
- **Python** 🐍
- **Sockets (socket module)** for network communication
- **Threading** for parallel execution of TCP and UDP servers

---


## **📜 License**
This project is open-source and can be freely modified and distributed.

---

## **💡 Conclusion**
This project demonstrates an efficient way to run TCP and UDP servers concurrently, allowing a client to send messages over **random protocols**. It provides a **real-world understanding** of how different networking protocols work in Python. 🚀

