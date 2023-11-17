import base64
import os
from cryptography import fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys
import datetime
dir = os.curdir
mysalt = b'q\xeb\xf2X\x0f\xac\x06\xc4\x07\x86F\xe3\xc8\xfc\x96\xe0'

os.system("cls")
print("Directory: "+os.getcwd())

if os.path.exists(".ENCRYPTED") and os.path.exists(".DECRYPTED"):
    print("--ERROR Unknown status--")
    mode = input("Enter mode [e] or [d]: ")
    os.remove(".ENCRYPTED")
    os.remove(".DECRYPTED")
    
elif os.path.exists(".ENCRYPTED"):
    mode = "d"
    print("Status: Encrypted")
    os.remove(".ENCRYPTED")
elif os.path.exists(".DECRYPTED"):
    mode = "e"
    print("Status: Decrypted")
    os.remove(".DECRYPTED")
else:
    mode = input("Enter mode [e] or [d]: ")

passworld = input("Enter Passworld: ")
print()

i = 0

def cryption(text):
    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256,
        length=32,
        salt=mysalt,
        iterations=100000,
        backend=default_backend()
    )
    enpswd = str(passworld).encode()
    key = base64.urlsafe_b64encode(kdf.derive(enpswd))
    
    fkey = fernet.Fernet(key)
    iText = str(text)
    
    if mode=="e":
        output = fkey.encrypt(bytes(str(iText), 'utf-8'))
        print("Encryption... DONE")
        outFile = open(".ENCRYPTED", "a+")
        outFile.write(str(datetime.datetime.now()))
    elif mode=="d":
        output = fkey.decrypt(bytes(str(iText), 'utf-8'))
        print("Decryption... DONE")
        outFile = open(".DECRYPTED", "a+")
        outFile.write(str(datetime.datetime.now()))
        
    ooutput = str(output.decode("utf-8"))
    return ooutput

if mode!= "e" and mode!= "d":
    print("!!Error no valid mode!!")
    exit(1)

for file in os.listdir(dir):
    i = i + 1
    print(file)
    strFile = str(file)
    
    if strFile!= ".DriveEncoder.py" and strFile!= ".ENCRYPTED" and strFile!= ".DECRYPTED" and strFile!= ".DriveEncoder.exe":
        print(">Processing...") 
        
        openf = open(file, "r")
        text = openf.read()
        text2 = str(text)
        openf.close()
        os.remove(file)
        
        openf2 = open(file, "w")
        openf2.write(cryption(text2))
        openf2.close()
        
    else:
        print(">Protected file ignoring...")