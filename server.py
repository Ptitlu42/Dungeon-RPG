import socket
import threading


class Server:
    def __init__(self):
        #socket creation
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        hostname = socket.gethostname()
        self.server_ip = socket.gethostbyname(hostname)
        self.server_port = 6666
        try:
            self.sck.bind((self.server_ip, self.server_port))
            print("Serveur UP")
            print(self.server_ip)
        except:
            print("WARNING ! Server DOWN - bind problem (Wrong IP or PORT)")
        self.sck.listen()
        self.clients = []

    def gerer_client(self, conn, addr):
        self.clients.append(conn)
        while True:
            try:
                data = conn.recv(2048).decode()
                if data:
                    print(data)
                    for client in self.clients:
                        client.send(data.encode())
                else:
                    self.clients.remove(conn)
                    conn.close()
                    break
            except:
                self.clients.remove(conn)
                conn.close()
                break

    def start_server(self):
        # loop that accepts new connections and creates threads
        while True:
            # accept new connections
            conn, addr = self.sck.accept()
            print(f"Connection established with {addr}")
            # Threads creation
            thread_client = threading.Thread(target=self.gerer_client, args=(conn, addr))
            thread_client.start()