import socket
import threading

from chat import envoyer_messages, recevoir_messages

hote = "192.168.1.68"
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

"""
creation de 2 threads, un pour l'envoi de message, l'autre pour la reception

"""
thread_envoi = threading.Thread(target=envoyer_messages, args=(connexion_avec_serveur,))
thread_reception = threading.Thread(target=recevoir_messages, args=(connexion_avec_serveur,))

#demarrage des threads
thread_envoi.start()
thread_reception.start()

#empeche la perte  de messages -> join() -> permet d'attendre que le threads se termine correctement
thread_envoi.join()
thread_reception.join()

print("Fermeture de la connexion")
connexion_avec_serveur.close() 