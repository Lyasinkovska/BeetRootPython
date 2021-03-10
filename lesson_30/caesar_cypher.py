import string


def encrypt_caesar(message: str, key: int = 3):
    alphabet = string.ascii_letters
    encrypted_message = []
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter) + key
            encrypted_letter = alphabet[index % len(alphabet)]
        else:
            encrypted_letter = letter
        encrypted_message.append(encrypted_letter)
    return ''.join(encrypted_message)


def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


if __name__ == '__main__':
    print(encrypt_caesar('Z455a', -5))
    print(encrypt('@', 1))
