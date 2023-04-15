from cryptography.fernet import Fernet
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def initializeWrite():
    try: 
        os.remove("message.txt")
    except Exception:
        pass    

def initializeRead():
    global file
    file = open("message.txt", "r")

def encryptMessage(user, password, message):
    fernet = _getKey(user, password)
    return fernet.encrypt(message.encode())

def decryptMessage(user, password, message):
    fernet = _getKey(user, password)
    try:
        decryptedMessage = fernet.decrypt(message).decode() 
        return decryptedMessage
    except Exception:
        print("Not  possible to decrypt!")    

def saveNewLine(message):
    file = open('message.txt', 'a')    
    file.write(message.decode() + "\n")
    file.close()

def readAllLines():
    global file
    lines = file.readlines()
    lines = [line.rstrip('\n') for line in lines]
    return [line.encode() for line in lines]

def readNextLine():
    global file    
    return file.readline().rstrip('\n').encode()

def _getKey(user, password):
    user = user.encode()
    password = password.encode()    
    salt = user
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return Fernet(key)    
