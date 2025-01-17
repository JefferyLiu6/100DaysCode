alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text = "text", shift_amount = 0):
    temp = ""
    for i in original_text:
        shifted_position = alphabet.index(i) + shift_amount
        shifted_position %= len(alphabet)
        temp += alphabet[shifted_position]
    print(f"Here is the encoded result: {temp}")


encrypt(original_text=text, shift_amount=shift)