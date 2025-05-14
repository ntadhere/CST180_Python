# Main function that handles user input and displays the encrypted result
def Main():
    # Prompt the user to enter the text they want to encrypt
    text = input("Enter the text to encrypt: ")
    # Prompt the user to enter a shift value (used for the cipher)
    shift = int(input("Enter the shift value: "))
    # Encrypt the input text using the ShiftCipher function
    encryptedText = ShiftCipher(text, shift)
    # Display the encrypted text
    print("Encrypted text:", encryptedText)

    # Prompt the user to enter the text they want to decrypt
    text = input("Enter the text to decrypt: ")
    # Encrypt the input text using the ShiftCipher function
    encryptedText = DecryptShiftCipher(text, shift)
    # Display the encrypted text
    print("Decrypted text:", encryptedText)

# Function to perform the Caesar Cipher (Shift Cipher) encryption
def ShiftCipher(text, shift):
    result = ""  # Initialize an empty string to build the encrypted result

    # Loop through each character in the input text
    for char in text:
        if char.isupper():
            # Encrypt uppercase characters (A-Z)
            # Shift within the range 65-90 (ASCII for 'A' to 'Z')
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            # Encrypt lowercase characters (a-z)
            # Shift within the range 97-122 (ASCII for 'a' to 'z')
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave non-alphabetic characters unchanged
            result += char

    # Return the final encrypted string
    return result

def DecryptShiftCipher(text, shift):
    result = ""

    for char in text:
        if char.isupper():
            # Decrypt uppercase letters
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            # Decrypt lowercase letters
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            # Leave non-alphabet characters unchanged
            result += char

    return result


# Call the main function to start the program
Main()
