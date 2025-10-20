# Source : https://pymotw.com/2/socket/udp.html

import socket
import sys

server_address = ('localhost', 10000)
message = 'Ceci est un message. Il va être répété par le serveur.'

# Création du socket UDP
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3.0)  # délai d'attente pour la réponse
except socket.error as e:
    print(f"Erreur lors de la création du socket : {e}")
    sys.exit(1)

try:
    print('Envoi UDP à %s sur le port %s' % server_address)
    print('Envoi : "%s"' % message)

    # Envoi du message
    try:
        sent = sock.sendto(message.encode(), server_address)
    except socket.gaierror as e:
        print(f"Erreur d’adresse serveur : {e}")
        sys.exit(1)
    except socket.error as e:
        print(f"Erreur d’envoi : {e}")
        sys.exit(1)

    # Réception de la réponse
    try:
        data, server = sock.recvfrom(4096)
        print('Reçu : "%s"' % data.decode(errors='ignore'))
    except socket.timeout:
        print("Aucune réponse du serveur (délai dépassé).")
    except ConnectionResetError:
        print("Connexion refusée ou serveur non disponible.")
    except socket.error as e:
        print(f"Erreur de réception : {e}")

except KeyboardInterrupt:
    print("\nInterruption par l’utilisateur (Ctrl+C).")

finally:
    sock.close()
    print("Socket fermé.")
