# Caesar Cipher

This is a Python implementation of the Caesar Cipher, a simple encryption technique that shifts the letters of a message by a specified number of places in the alphabet. This program allows you to encode (encrypt) or decode (decrypt) a message interactively.

---

## Features

- **Encryption**: Shifts the letters of a message to encode it.
- **Decryption**: Reverses the shift to decode an encrypted message.
- Handles non-alphabetic characters (e.g., spaces, punctuation) without altering them.
- Supports user interaction to repeatedly encode or decode messages.

---

## Prerequisites

- Python 3.x installed on your machine.
- The `art` Python package to display the logo. Install it using:
  ```bash
  pip install art
  ```

---

## Usage

1. Clone this repository or copy the script to your local environment.
2. Ensure you have Python 3.x installed.
3. Run the script:
   ```bash
   python caesar_cipher.py
   ```
4. Follow the interactive prompts:
   - **Encode**: Encrypt a message.
   - **Decode**: Decrypt a message.

### Example

#### Input:
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
```

#### Output:
```
Here is the encoded result: khoor zruog
