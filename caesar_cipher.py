def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift  # Reverse shift for decryption

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result


# User Input
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter the message: ")
    shift_value = int(input("Enter the shift value: "))

    if choice in ["encrypt", "decrypt"]:
        output = caesar_cipher(message, shift_value, choice)
        print(f"Result: {output}")
    else:
        print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
