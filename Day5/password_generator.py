letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

le = [] # A new list contains the numbers of letter decided by user
nu = [] # A new list contains the numbers of number decided by user
sy = [] # A new list contains the numbers of symbol decided by user
idx = 0

for i in range(nr_letters):
    idx = random.randint(0, len(letters))
    print(idx)
    le.append(letters[idx])
idx = 0
for i in range(nr_letters):
    idx = random.randint(0, len(numbers))
    nu.append(numbers[idx])
idx = 0
for i in range(nr_letters):
    idx = random.randint(0, len(symbols))
    sy.append(symbols[idx])

print(le, nu, sy)

ls = le+ nu
ls = ls + sy
print(ls)

pw = random.shuffle(ls)

print(ls)
password = ""
for i in ls:
    password += i
    pass
print(f"Your password is: {password}")
