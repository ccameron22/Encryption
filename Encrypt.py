from keyGenerator import publicKey
from base64 import b64encode
import rsa

password = input("Enter password: ")
encodedPassword = password.encode()
encryptedPassword = rsa.encrypt(encodedPassword, publicKey)
b64Pass = b64encode(encryptedPassword).decode()
print(encryptedPassword)