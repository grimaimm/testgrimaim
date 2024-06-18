# config.py
class Config:
    DEBUG = True
# from cryptography.fernet import Fernet

# class Config:
#     DEBUG = True

#     # Flask-Mail configuration
#     MAIL_SERVER = 'smtp.gmail.com'
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
    
#     # Load the key
#     with open('secret.key', 'rb') as key_file:
#         key = key_file.read()

#     # Create a cipher object
#     cipher = Fernet(key)

#     # Decrypt the credentials
#     with open('credentials.enc', 'rb') as enc_file:
#         encrypted_email, encrypted_password = enc_file.read().split(b'\n')

#     MAIL_USERNAME = cipher.decrypt(encrypted_email).decode()
#     MAIL_PASSWORD = cipher.decrypt(encrypted_password).decode()
