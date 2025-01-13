import random
import sys

# Character Pools
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+'

def get_user_input(prompt):
    """Get and validate user input as a positive integer."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def generate_password(nr_letters, nr_numbers, nr_symbols):
    """Generate a random password based on the specified number of letters, numbers, and symbols."""
    # Select random characters
    letters_selected = [random.choice(LETTERS) for _ in range(nr_letters)]
    numbers_selected = [random.choice(NUMBERS) for _ in range(nr_numbers)]
    symbols_selected = [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    
    # Combine all characters
    password_list = letters_selected + numbers_selected + symbols_selected
    
    # Shuffle the combined list to ensure randomness
    random.shuffle(password_list)
    
    # Join the list into a string to form the password
    password = ''.join(password_list)
    return password

def main():
    print("Welcome to the PyPassword Generator!")

    # Get user inputs with validation
    nr_letters = get_user_input("How many letters would you like in your password?\n")
    nr_symbols = get_user_input("How many symbols would you like?\n")
    nr_numbers = get_user_input("How many numbers would you like?\n")

    # Generate password
    password = generate_password(nr_letters, nr_numbers, nr_symbols)

    print(f"Your password is: {password}")

if __name__ == "__main__":
    main()
