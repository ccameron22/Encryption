
from base64 import b64encode
import rsa

def callEncrypt(plainText: str) -> str:

    f = open("Public Key.pem", "r")
    publicKey = f.read()
    publicKey = rsa.PublicKey.load_pkcs1(publicKey)

    #password = input("Enter password: ")
    password = plainText
    encodedPassword = password.encode()


    encryptedPassword = rsa.encrypt(encodedPassword, publicKey)
    b64Pass = b64encode(encryptedPassword).decode()
    print('\n', "Encrypted Password: ", b64Pass)
    return b64Pass