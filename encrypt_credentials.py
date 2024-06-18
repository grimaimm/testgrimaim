from cryptography.fernet import Fernet

# Generate a key and save it to a file
key = Fernet.generate_key()
with open('secret.key', 'wb') as key_file:
    key_file.write(key)

# Load the key
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

# Create a cipher object
cipher = Fernet(key)

# Encrypt the credentials
email = "muhammadrahim@students.amikom.ac.id"
password = "rrgn kbpk wjir gsfu"

encrypted_email = cipher.encrypt(email.encode())
encrypted_password = cipher.encrypt(password.encode())

with open('credentials.enc', 'wb') as enc_file:
    enc_file.write(encrypted_email + b'\n' + encrypted_password)
