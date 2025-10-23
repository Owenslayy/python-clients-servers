# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('10.20.61.14', 10000)
print('Connexion TCP a %s sur le port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message = 'Ceci est un messsage. Il va etre repete par le serveur.'
    print('Envoi de : "%s"' % message)
    sock.sendall(message.encode())
    

finally:
    print('Fermeture du socket TCP')
    sock.close()