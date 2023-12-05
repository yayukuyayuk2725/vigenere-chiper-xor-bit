def string_to_bits(input_string):
    return ''.join(format(ord(char), '08b') for char in input_string)

def bits_to_string(bit_string):
    if len(bit_string) % 8 != 0:
        raise ValueError("Panjang string bit harus merupakan kelipatan dari 8")

    return ''.join(chr(int(bit_string[i:i+8], 2)) for i in range(0, len(bit_string), 8))

def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]

    for i in range(len(plaintext)):
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i]))
        encrypted_text += encrypted_char

    return string_to_bits(encrypted_text)

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key * (len(ciphertext) // len(key)) + key[:len(ciphertext) % len(key)]

    for i in range(len(ciphertext)):
        decrypted_char = chr(ord(ciphertext[i]) ^ ord(key[i]))
        decrypted_text += decrypted_char

    return bits_to_string(decrypted_text)

def xor_encrypt_decrypt(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        encrypted_char = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        encrypted_text += encrypted_char
    return string_to_bits(encrypted_text)

def xor_decrypt(text, key):
    decrypted_text = ""
    for i in range(len(text)):
        decrypted_char = chr(ord(text[i]) ^ ord(key[i % len(key)]))
        decrypted_text += decrypted_char
    return bits_to_string(decrypted_text)


plaintext = input("Masukkan plaintext: ")[:7]  
key = input("Masukkan kunci: ")[:7]  

encrypted_text_vigenere = vigenere_encrypt(plaintext, key)
print("Teks Terenkripsi dengan Vigenère Cipher (dalam bit):", encrypted_text_vigenere)

try:
    decrypted_text_vigenere = vigenere_decrypt(encrypted_text_vigenere, key)
    print("Teks Terdekripsi dengan Vigenère Cipher:", decrypted_text_vigenere)
except ValueError as e:
    print("Error:", e)
