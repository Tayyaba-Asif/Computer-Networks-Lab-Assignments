from socket import *
from PIL import Image,UnidentifiedImageError
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
 connectionSocket, addr = serverSocket.accept()
 filename=connectionSocket.recv(2048)
 try:
     img=Image.open(f"{filename.decode()}.tga")
     img.show()
 except UnidentifiedImageError:
     print("No file exist")
     connectionSocket.send("No file exist".decode().upper().encode())    
     connectionSocket.close()
connectionSocket.close()     