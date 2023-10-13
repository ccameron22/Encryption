
from base64 import b64decode
import rsa

f = open("Private Key.pem", "r")
privateKey = f.read()
privateKey = rsa.PrivateKey.load_pkcs1(privateKey)

encryptedPassword = input("Enter encrypted password: ")
encryptedPassword = b64decode(encryptedPassword.encode())

decryptedPassword = rsa.decrypt(encryptedPassword, privateKey)
decryptedPassword = decryptedPassword.decode()
print('\n', "Password: ", decryptedPassword)

