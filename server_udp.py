# Source : https://pymotw.com/2/socket/udp.html

import socket

# Crée un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('0.0.0.0', 10000)
sock.bind(server_address)
sock.settimeout(1.0)  # permet d'interrompre avec Ctrl+C

print(f"Serveur UDP démarré sur {server_address[0]}:{server_address[1]}")
print("Attente de messages UDP...")

try:
    while True:
        try:
            data, address = sock.recvfrom(4096)
        except socket.timeout:
            continue  # revient dans la boucle, permet à Ctrl+C de fonctionner

        print(f"Reçu {len(data)} octets de {address}")
        print(f"Contenu : {data.decode(errors='ignore')}")

        if data:
            sent = sock.sendto(data, address)
            print(f"Renvoi de {sent} octets au client {address}")

except KeyboardInterrupt:
    print("\nArrêt du serveur via Ctrl+C.")

finally:
    sock.close()
    print("Socket fermé.")
