alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, rotate):
    encrypted = ""
    for char in text:
        encrypted += rotate_character(char, rotate)
    return encrypted

def alphabet_position(letter):
    return int(alphabet.index(letter.lower()))

def rotate_character(char, rotate):
    if char.lower() in alphabet:
        newIndex = (alphabet.index(char.lower()) + int(rotate)) % 26
        if char.isupper():
            return alphabet[newIndex].upper()
        else:
            return alphabet[newIndex].lower()
    else:
        return char
