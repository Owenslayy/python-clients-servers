# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print('Demarrage du serveur UDP sur %s avec le port %s' % server_address)
sock.bind(server_address)

# Wait for a connection
print('')
print('Attente de messages UDP...')

while True:
    bytesAddressPair = sock.recvfrom(255)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    print('Adresse "%s"' % bytesAddressPair[0].decode())
    print('Message "%s"' % str(bytesAddressPair[1]))

    # Sending a reply to client
    print('Renvoi les memes donnees au client')
    sock.sendto(bytesAddressPair[0], bytesAddressPair[1])
