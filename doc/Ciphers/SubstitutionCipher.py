import string

def Main():
    key="qwertyuiopasdfghjklzxcvbnm"
    translationTable = CreateTranslationTable(key)

    text = input("Enter the text to encrypt: ").lower()
    encryptedText = SubstitutionCipher(text, translationTable)
    print("Encrypted text: ", encryptedText)

def CreateTranslationTable(key):
    alphabet = string.ascii_lowercase
    return str.maketrans(alphabet, key)

def SubstitutionCipher(text, translationTable):
    return text.translate(translationTable)

Main()