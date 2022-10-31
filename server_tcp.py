# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
print('Demarrage du serveur TCP sur %s avec le port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('')
    print('Attente de connexion TCP...')
    connection, client_address = sock.accept()
    try:
        print('Connexion de ', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(255)
            print('Recu : "%s"' % data.decode())
            if data:
                print('Renvoi les memes donnees au client')
                connection.sendall(data)
            else:
                print('Plus de donnees de la part de ', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()