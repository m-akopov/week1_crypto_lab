import base64

# Base64 encoded ciphertext and passphrase
ciphertext_base64 = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
passphrase = "secure"

# Decode the base64 ciphertext
ciphertext = base64.b64decode(ciphertext_base64)

# Perform XOR decryption with the passphrase
decrypted_message = bytearray()
for i in range(len(ciphertext)):
    decrypted_message.append(ciphertext[i] ^ ord(passphrase[i % len(passphrase)]))

# Convert decrypted bytes to a string
decrypted_text = decrypted_message.decode("utf-8", errors="ignore")
print(decrypted_text)