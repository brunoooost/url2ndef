# url2ndef

This script is designed to process a URL and generate an NFC NDEF (NFC Data Exchange Format) message. It identifies the protocol of the URL, calculates the length of the rest of the URL (excluding the protocol), and converts it into a hexadecimal format. The result is a formatted NFC NDEF message that can be used for NFC tag encoding or other related applications.

## Features

1. **Protocol Detection**: The script identifies the protocol of the URL (e.g., HTTP, HTTPS, FTP, etc.) and assigns a specific identifier for each.
2. **Hexadecimal Conversion**: The part of the URL after the protocol is converted into a hexadecimal string for NFC encoding.
3. **NFC NDEF Message Creation**: The script structures the data in the format required for NFC NDEF messages, including the protocol identifier and the hex-encoded URL.
4. **User Input**: The script allows the user to paste a URL, and it automatically processes and generates the NFC NDEF message.

## How it Works

### Step 1: **Identify Protocol**
The script checks the beginning of the URL to determine which protocol it uses (HTTP, HTTPS, Tel, Mailto, etc.). Each protocol is assigned a specific identifier.

### Step 2: **Process the URL**
After identifying the protocol, the script calculates the length of the remaining URL and converts it to a hex-encoded string.

### Step 3: **Generate NFC NDEF Message**
Using the protocol identifier, the length of the URL's content, and the hex-encoded URL, the script builds an NFC NDEF message.

### Example

If you input the URL `https://www.example.com`, the script will generate the following NFC NDEF message:

```
D1 01 1A 55 02 68 74 74 70 73 3A 2F 2F 77 77 77 2E 65 78 61 6D 70 6C 65 2E 63 6F 6D
```

Where:
- `D1` indicates NFC Type 1.
- `01` is the length of the record.
- `1A` is the length of the payload (in this case, the URL after the protocol).
- `55` indicates a URI type.
- `02` is the identifier for the `https://` protocol.
- The rest is the hexadecimal representation of `www.example.com`.

## How to Use

1. **Clone or Download** the script to your local machine.
2. **Run the script** in a Python environment (e.g., Python 3.x).
3. **Paste the URL** when prompted. The script will process the URL and output the NFC NDEF message.

Example usage:

```bash
Paste the URL link: https://www.example.com
```

The result will be an NFC NDEF message, which can be used for NFC tag encoding or other applications.

## Requirements

- Python 3.x


