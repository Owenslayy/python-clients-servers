# Source : https://pymotw.com/2/socket/tcp.html

import socket
import sys

server_address = ('localhost', 10000)
message = 'Ceci est un message. Il va être répété par le serveur.'

# Création du socket TCP
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5.0)  # timeout global pour éviter le blocage
except socket.error as e:
    print(f"Erreur lors de la création du socket : {e}")
    sys.exit(1)

print('Connexion TCP à %s sur le port %s' % server_address)

# Tentative de connexion
try:
    sock.connect(server_address)
except socket.timeout:
    print("Délai de connexion dépassé (timeout).")
    sys.exit(1)
except ConnectionRefusedError:
    print("Connexion refusée : le serveur n’est probablement pas lancé.")
    sys.exit(1)
except socket.gaierror as e:
    print(f"Erreur d’adresse serveur : {e}")
    sys.exit(1)
except socket.error as e:
    print(f"Erreur de connexion : {e}")
    sys.exit(1)

try:
    # Envoi du message
    print('Envoi de : "%s"' % message)
    try:
        sock.sendall(message.encode())
    except socket.error as e:
        print(f"Erreur lors de l’envoi : {e}")
        sys.exit(1)

    # Réception de la réponse
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        try:
            data = sock.recv(255)
            if not data:
                print("Connexion fermée par le serveur.")
                break
            amount_received += len(data)
            print('Reçu : "%s"' % data.decode(errors='ignore'))
        except socket.timeout:
            print("Aucune donnée reçue (timeout).")
            break
        except socket.error as e:
            print(f"Erreur de réception : {e}")
            break

except KeyboardInterrupt:
    print("\nInterruption par l’utilisateur (Ctrl+C).")

finally:
    print("Fermeture du socket TCP.")
    sock.close()
