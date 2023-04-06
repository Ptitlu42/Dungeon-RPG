import socket

hote = "192.168.157.229"
port = 6666

# Créer un socket pour le client
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print(f"Connexion établie avec le serveur sur le port {port}")

msg_a_envoyer = ""
while msg_a_envoyer != "fin":
    msg_a_envoyer = input("> ")
    # Envoyer le message au serveur
    connexion_avec_serveur.send(msg_a_envoyer.encode())

    # Recevoir les messages des autres clients
    messages_recus = connexion_avec_serveur.recv(1024).decode()
    print(messages_recus)

print("Fermeture de la connexion")
connexion_avec_serveur.close() 