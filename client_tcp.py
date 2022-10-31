# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('Connexion a %s sur le port %s' % server_address)
sock.connect(server_address)

try:
    
    # Send data
    message = 'Ceci est un messsage. Il va etre repete par le serveur.'
    print('Envoi de : "%s"' % message)
    sock.sendall(message.encode())
    
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(255)
        amount_received += len(data)
        print('Recu :  "%s"' % data.decode())

finally:
    print('Fermeture du socket TCP')
    sock.close()