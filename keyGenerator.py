import rsa
from base64 import b64encode

publicKey, privateKey = rsa.newkeys(512)

f = open("Public Key.pem", "wb")
f.write(publicKey.save_pkcs1())
f.close()


f = open("Private Key.pem", "wb")
f.write(privateKey.save_pkcs1())
f.close()