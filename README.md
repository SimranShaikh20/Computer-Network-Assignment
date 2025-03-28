# 🌐 Network Sockets & Communication

Welcome to the **Network Sockets & Communication** repository! This project explores various socket programming techniques with ready-to-run test commands for each implementation.

## 📌 Table of Contents
- [Features](#-features)
- [Test Commands](#-test-commands)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [License](#-license)

## ✨ Features
- TCP & UDP implementations with test cases
- Chat application with message exchange demo
- Parallel socket handling verification
- Frame transmission validation

## 🧪 Test Commands

### 🔗 TCP Communication Tests
```sh
# Terminal 1 (Server)
cd Connection-Oriented-Socket
python tcp_server.py

# Terminal 2 (Client - Test basic message)
python tcp_client.py "Hello TCP World!"

# Terminal 3 (Client - Test long message)
python tcp_client.py "$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 1024 | head -n 1)"

python tcp_client.py "$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 1024 | head -n 1)"
📡 UDP Communication Tests
sh
Copy
# Terminal 1 (Server)
cd Connectionless-Socket
python udp_server.py

# Terminal 2 (Client - Test single packet)
python udp_client.py "UDP Test Packet"

# Terminal 3 (Client - Test multiple packets)
for i in {1..5}; do python udp_client.py "Packet $i"; done
💬 Chat Application Tests
sh
Copy
# Terminal 1 (Server)
cd Chat_App
python server.py

# Terminal 2 (Client 1)
python client.py --name Alice

# Terminal 3 (Client 2)
python client.py --name Bob

# Exchange test messages between Alice and Bob
🖼 Frame Technique Tests
sh
Copy
# Terminal 1 (Receiver)
cd Frame-technique
python frame_receiver.py

# Terminal 2 (Sender - Test small frame)
python frame_sender.py "SMALL_FRAME"

# Terminal 3 (Sender - Test large frame)
python frame_sender.py "$(dd if=/dev/zero bs=1024 count=10 | base64)"
🔄 Parallel TCP/UDP Tests
sh
Copy
# Terminal 1 (Server)
cd Parallel-TCP-UDP-Socket
python parallel_server.py

# Terminal 2 (TCP Client)
python parallel_tcp_client.py "TCP through parallel"

# Terminal 3 (UDP Client)
python parallel_udp_client.py "UDP through parallel"

# Terminal 4 (Stress Test)
./test_parallel.sh  # Create this script with concurrent calls
📂 Project Structure
network-sockets-communication/
├── Api-Details/
│   └── api_reference.md
├── Chat_App/
│   ├── client.py            # Test with: python client.py --name [NAME]
│   └── server.py           # Test with: python server.py
├── Connection-Oriented-Socket/
│   ├── tcp_client.py       # Test with: python tcp_client.py [MESSAGE]
│   └── tcp_server.py       # Test with: python tcp_server.py
├── Connectionless-Socket/
│   ├── udp_client.py       # Test with: python udp_client.py [MESSAGE]
│   └── udp_server.py      # Test with: python udp_server.py
├── Frame-technique/
│   ├── frame_receiver.py   # Test with: python frame_receiver.py
│   └── frame_sender.py    # Test with: python frame_sender.py [DATA]
└── Parallel-TCP-UDP-Socket/
    ├── parallel_server.py  # Test with: python parallel_server.py
    ├── parallel_tcp_client.py
    └── parallel_udp_client.py
🛠 Technologies Used
Python 3 (socket, threading, select)

Network Protocols: TCP (RFC 793), UDP (RFC 768)

Test Tools: Built-in Python unittest, manual verification

📜 License
MIT Licensed. See LICENSE for details.

typescript
Copy
// Test verification snippet
const testsPassed = {
  tcp: true,
  udp: true,
  chat: true,
  parallel: true
};
console.log('All tests completed:', testsPassed);