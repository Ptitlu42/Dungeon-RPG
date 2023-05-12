import socket
import threading

hote = "192.168.157.229"
port = 6666

def envoyer_messages(connexion):
    while True:
        message = input("> ")
        message = message.replace('"', '\\"')  # Échapper les guillemets doubles
        message = message.encode()
        connexion.send(message)

def recevoir_messages(connexion):
    while True:
        message = connexion.recv(1024)
        print(message.decode())

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print(f"Connexion établie avec le serveur sur le port {port}")

thread_envoi = threading.Thread(target=envoyer_messages, args=(connexion_avec_serveur,))
thread_reception = threading.Thread(target=recevoir_messages, args=(connexion_avec_serveur,))

thread_envoi.start()
thread_reception.start()

thread_envoi.join()
thread_reception.join()

print("Fermeture de la connexion")
connexion_avec_serveur.close() 