from keyGenerator import privateKey
from base64 import b64decode
import rsa

encryptedPassword = input("Enter encrypted password: ")
encryptedPassword = b64decode(encryptedPassword.encode())
decryptedPassword = rsa.decrypt(encryptedPassword, privateKey).decode()
print(decryptedPassword)

