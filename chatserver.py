import socket
import threading

hote = "192.168.157.229"
port = 6666

# Cette liste contiendra toutes les connexions client
clients = []

def gerer_client(connexion_client, adresse_client):
    """Fonction qui gère la connexion avec un client"""
    # Ajouter la connexion client à la liste globale de connexions
    clients.append(connexion_client)

    while True:
        try:
            # Recevoir un message du client
            message = connexion_client.recv(1024).decode()
            if message:
                print(f"{adresse_client} : {message}")
                # Transmettre le message à tous les autres clients
                for client in clients:
                    if client != connexion_client:
                        client.send(f"{adresse_client} : {message}".encode())
            else:
                # Si le message est vide, supprimer la connexion client et sortir de la boucle
                clients.remove(connexion_client)
                connexion_client.close()
                break
        except:
            # Si une erreur se produit, supprimer la connexion client et sortir de la boucle
            clients.remove(connexion_client)
            connexion_client.close()
            break

# Créer un socket pour le serveur
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((hote, port))

# Ecouter les connexions de clients
serveur.listen()

print(f"Le serveur écoute à présent sur le port {port}")

while True:
    # Accepter une nouvelle connexion client
    connexion_client, adresse_client = serveur.accept()
    print(f"Connexion établie avec {adresse_client[0]}:{adresse_client[1]}")

    # Créer un thread pour gérer la connexion client
    thread_client = threading.Thread(target=gerer_client, args=(connexion_client, adresse_client))
    thread_client.start()