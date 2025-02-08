# Password Manager

This project is a **Password Manager with JSON Storage and Exception Handling**, built using Python and Tkinter. It allows users to generate strong passwords, save them securely, and retrieve them later.

## What I Learned

- **JSON Handling**: Storing and retrieving password data in JSON format.
- **Exception Handling**:
  - Using `try`, `except`, and `else` to manage errors effectively.
  - Handling file-related errors when reading and writing JSON data.
- **Tkinter GUI**: Creating an interactive interface for password management.
- **Pyperclip**: Copying passwords to the clipboard automatically.

## Features

- **Password Generation**:
  - Generates strong passwords with a mix of letters, numbers, and symbols.
  - Uses `random.choice()` and `random.shuffle()` for randomness.
- **Secure Storage with JSON**:
  - Saves credentials (website, email, password) in a `data.json` file.
  - Allows retrieval of stored credentials.
- **Error Handling**:
  - Catches file handling errors using `try-except` blocks.
  - Ensures smooth execution even if the JSON file does not exist.