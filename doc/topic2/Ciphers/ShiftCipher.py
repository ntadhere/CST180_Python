def Main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))

    encryptedText = ShiftCipher(text, shift)
    print("Encrypted text:", encryptedText)

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

Main()
