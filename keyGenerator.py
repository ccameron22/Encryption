import rsa
from base64 import b64encode

publicKey, privateKey = rsa.newkeys(512)
print(publicKey.save_pkcs1().decode('utf-8'))

f = open("Public Key.pem", "wb")
f.write(publicKey.save_pkcs1())
f.close()


f = open("Private Key.pem", "w")
f.write((privateKey.save_pkcs1().decode('utf-8')))
f.close()