# Main function that handles user input and displays the encrypted and decrypted results
def Main():
    # Prompt the user to enter the text they want to encrypt
    text_to_encrypt = input("Enter the text to encrypt: ")

    try:
        # Prompt the user to enter a shift value (used for the cipher)
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Error: Please enter a valid integer for the shift value.")
        return

    # Encrypt the input text using the ShiftCipher function
    encrypted_text = ShiftCipher(text_to_encrypt, shift)
    # Display the encrypted text
    print("Encrypted text:", encrypted_text)

    # Prompt the user to enter the text they want to decrypt
    text_to_decrypt = input("Enter the text to decrypt: ")
    # Decrypt the input text using the DecryptShiftCipher function
    decrypted_text = DecryptShiftCipher(text_to_decrypt, shift)
    # Display the decrypted text
    print("Decrypted text:", decrypted_text)


# Function to perform Caesar Cipher encryption
def ShiftCipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char

    return result


# Function to perform Caesar Cipher decryption
def DecryptShiftCipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char

    return result


# Start the program
Main()
