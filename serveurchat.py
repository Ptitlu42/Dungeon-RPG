import socket

hote = "192.168.157.229"
port = 6666

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print(f"Le serveur écoute à présent sur le port {port}")

connexion_avec_client, infos_connexion = connexion_principale.accept()

msg_recu = b""
while msg_recu != b"fin":
    msg_recu = connexion_avec_client.recv(1024)
    print (msg_recu.decode())
    msg_a_envoyer = input("> ")
    msg_a_envoyer = msg_a_envoyer.encode()
    connexion_avec_client.send(msg_a_envoyer)

print("FERMETURE DE LA CONNEXION")
connexion_avec_client.close()
connexion_principale.close()