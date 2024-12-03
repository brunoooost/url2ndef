# **url2ndef** 

This script takes a URL, detects its protocol, and converts the URL into a properly formatted NFC NDEF (NFC Data Exchange Format) message. It’s perfect for **NFC applications** where a URL needs to be encoded onto a tag. The script processes the URL, identifies the protocol, calculates the URL length, converts it into hexadecimal format, and generates the corresponding NFC NDEF message. 

---

## 🚀 **Features** 

- **🔍 Protocol Detection**: Automatically detects common URL protocols like `http://`, `https://`, `tel:`, and `mailto:`.
- **💻 Hexadecimal Conversion**: Converts the URL (excluding the protocol) into a hex representation.
- **📡 NFC NDEF Structure**: Generates an NFC-compatible NDEF message that includes the protocol identifier, URL length, and hex-encoded URL.
- **👨‍💻 User-friendly**: Simply input a URL, and the script will return the corresponding NFC NDEF message.

---

## ⚙️ **How It Works**

1. **🔧 Protocol Identification**:
   - The script checks the URL’s protocol (e.g., `https://`, `http://`, etc.).
   - Each protocol gets a specific identifier (e.g., `02` for `https://`).

2. **🔢 URL Processing**:
   - After the protocol is identified, the script calculates the length of the remaining URL (without the protocol).
   - The rest of the URL is converted into a **hexadecimal** format, which is NFC-compatible.

3. **📑 Generate NFC NDEF Message**:
   - The script assembles the data into an **NFC NDEF message** with:
     - **Protocol identifier**
     - **Length of the URL (excluding the protocol)**
     - **Hexadecimal representation of the URL content**

---

## 💡 **Example**

### 📥 **Input** 

When prompted, paste a URL:

```bash
Paste the URL link: https://www.example.com
```

### 📤 **Output**

The script will output the corresponding **NFC NDEF message**:

```
D1 01 1A 55 02 68 74 74 70 73 3A 2F 2F 77 77 77 2E 65 78 61 6D 70 6C 65 2E 63 6F 6D
```

---

## 🛠️ **How to Use**

### Step 1: Clone or Download the Script

Clone or download the script to your local machine to get started.

### Step 2: Run the Script

Run the Python script in a **Python 3.x** environment.

### Step 3: Input a URL

When prompted, **paste a URL**, and the script will process it and output the NFC NDEF message.

Example:

```bash
Paste the URL link: https://www.example.com
```

The script will then generate and display the NFC NDEF message.

---

## 📋 **Requirements**

- **Python 3.x**: Make sure you have Python 3.x installed on your system.
- No additional libraries are needed—just Python itself.

---

