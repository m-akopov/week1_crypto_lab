# Function to decrypt the Caesar cipher by shifting letters
def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            # Shift letter and maintain case
            shifted_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
            if char.isupper():
                decrypted_text += shifted_char.upper()
            else:
                decrypted_text += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text += char
    return decrypted_text

# Function to try all shifts and print the results
def brute_force_decrypt(ciphertext):
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

# The given ciphertext
ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

# Perform brute-force decryption
brute_force_decrypt(ciphertext)