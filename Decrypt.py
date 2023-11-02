
from base64 import b64decode
import rsa


def callDecrypt(encryptedText: str) -> str:

    f = open("Private Key.pem", "r")
    privateKey = f.read()
    privateKey = rsa.PrivateKey.load_pkcs1(privateKey)

    #encryptedPassword = input("Enter encrypted password: ")
    encryptedPassword = encryptedText
    encryptedPassword = b64decode(encryptedPassword.encode())

    decryptedPassword = rsa.decrypt(encryptedPassword, privateKey)
    decryptedPassword = decryptedPassword.decode()
    print('\n', "Password: ", decryptedPassword)
    return decryptedPassword

