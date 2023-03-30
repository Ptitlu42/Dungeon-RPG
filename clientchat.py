import socket

hote = "192.168.157.229"
port = 6666

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print(f"Connexion établie avec le serveur sur le port {port}")

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode())

print("Fermeture de la connexion")
connexion_avec_serveur.close()