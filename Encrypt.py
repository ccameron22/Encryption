
from base64 import b64encode
import rsa

f = open("Private Key.pem", "r")
privateKey = f.read()
print(privateKey.encode('utf-8'))
privateKey = rsa.PrivateKey.load_pkcs1(privateKey)

password = input("Enter password: ")
encodedPassword = password.encode()
encryptedPassword = rsa.encrypt(encodedPassword, privateKey)
b64Pass = b64encode(encryptedPassword).decode()
print(encryptedPassword)