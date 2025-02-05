# Bit Stuffing and Destuffing in Python

## 📌 Description
This project implements **Bit Stuffing and Destuffing** in Python. 

### What is Bit Stuffing? 🤔
Bit stuffing is a **data transmission technique** used in communication protocols to ensure that special control sequences (such as frame delimiters) are not misinterpreted as data. It prevents the accidental appearance of **flag sequences** within the data by inserting additional bits where necessary.

### Why is Bit Stuffing Used? 🚀
- **Ensures data integrity** by preventing unintentional flag patterns.
- **Allows proper frame synchronization** in serial data transmission.
- **Used in protocols** like **HDLC (High-Level Data Link Control)** and **PPP (Point-to-Point Protocol).**

## ✨ Features
- **Bit Stuffing:** Inserts a `'0'` after every five consecutive `'1'`s.
- **Bit Destuffing:** Removes the extra `'0'` bits to restore the original data.
- **Displays the number of bits added** during stuffing.
- Uses **01111110** as the default **frame flag**.

---

## 🛠️ How It Works
### 1️⃣ Bit Stuffing:
- A `'0'` is inserted **after every five consecutive `'1'`s** in the binary string.
- The flag `01111110` is **added at the beginning and end** of the stuffed frame.
- The program outputs the stuffed data along with the **count of added `'0'`s**.

### 2️⃣ Bit Destuffing:
- The **flag `01111110` is removed** from the stuffed frame.
- Any **extra `'0'`** inserted during stuffing is **removed**.
- The **original binary data is restored**.

---

## 🚀 Installation and Usage
### ✅ Requirements
- Python **3.x** installed

### ▶️ Run the Program
1. Clone this repository or download the script.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python bit_stuffing.py
