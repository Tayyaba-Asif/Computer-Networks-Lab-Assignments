from email import message
from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message=input("Please enter filename to be displayed: ")
clientSocket.send(message.encode())
clientSocket.close()