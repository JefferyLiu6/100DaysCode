# Password Manager & Generator

This project is a **Password Manager with a Password Generator**, built using Python. It provides a graphical user interface (GUI) for storing login credentials and generating secure passwords.

## Features

### Password Manager (`main.py`)
- **Graphical Interface**: Built using Tkinter for easy interaction.
- **Password Storage**: Saves website login credentials (website, email, password) in a file (`output.txt`).
- **Password Generation**: Integrates with the password generator to create strong passwords.

### Password Generator (`password_generator.py`)
- Generates random passwords with:
  - Letters (uppercase & lowercase)
  - Numbers
  - Symbols
- Ensures strong and unpredictable passwords by shuffling characters.