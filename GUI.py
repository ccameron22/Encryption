import tkinter as tk
from tkinter import *
import Encrypt as en
import Decrypt as de

window = Tk()
window.geometry("400x500")
window.title("Password Crypt")

spaceLabel = tk.Label()
spaceLabelOne = tk.Label()
spaceLabelTwo = tk.Label()
spaceLabelThree = tk.Label()
spaceLabelFour = tk.Label()
############################################

#Encryption

def printEncrypted():
    encryptedText.delete(1.0,END)
    inp = plainText.get(1.0, "end-1c")
    encrypted = en.callEncrypt(inp)
    encryptedText.insert(INSERT, encrypted)


# TextBox Creation
spaceLabel.pack()
lbl = tk.Label(text = "Enter Plaintext Password")
lbl.pack()

plainText = tk.Text(height=1, width=30)
plainText.pack()

# Button Creation
printButton = tk.Button(text="Encrypt", command=printEncrypted)
printButton.pack()

# Output Text Box
spaceLabelOne.pack()
lbl = tk.Label(text = "Encrypted Password")
lbl.pack()

encryptedText = tk.Text(height=4, width=30)
encryptedText.pack()
spaceLabelTwo.pack()
spaceLabelThree.pack()

########################################################
########################################################
########################################################

#Decryption


def printDecrypted():
    decryptedText.delete(1.0,END)
    inp = encryptText.get(1.0, "end-1c")
    encryptText.delete(1.0, END)
    decrypted = de.callDecrypt(inp)
    decryptedText.insert(INSERT, decrypted)


# TextBox Creation
lbl = tk.Label(text = "Enter Encrypted Password")
lbl.pack()

encryptText = tk.Text(height=4, width=30)
encryptText.pack()

# Button Creation
printButton = tk.Button(text="Decrypt", command=printDecrypted)
printButton.pack()

# Output Text Box
spaceLabelFour.pack()
lbl = tk.Label(text = "Decrypted Password")
lbl.pack()

decryptedText = tk.Text(height=1, width=30)
decryptedText.pack()

####################################################
####################################################
####################################################



window.mainloop()