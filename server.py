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
        except:
            print("WARNING ! Server DOWN - bind problem (Wrong IP or PORT)")
        self.sck.listen()
        self.clients = []
        self.game_launched = False
        self.player_list = []

    def gerer_client(self, conn, addr):
        conn.send(str.encode("Client connected"))
        self.clients.append(conn)

        while True:
            try:
                data = conn.recv(2048).decode()
                if data:
                    # New method
                    print(f"Server received : {data}")
                    """ Old method
                            if self.game_launched:
                                for client in self.clients:
                                    client.send(data.encode())
                            else:
                                for client in self.clients:
                                    client.send(data.encode())"""
                else:
                    self.clients.remove(conn)
                    conn.close()
                    print("Missing data : Client Disconnected")
                    break
                data_s = "from server : " + data
                #conn.sendall(str.encode(data_s))
                if data == "Player_list":
                    for element in self.player_list:
                        #print(f"element : {element}")
                        element_s = f"IP, {element}"
                        #print("server send : ", element_s)
                        conn.sendall(str.encode(element_s))

            except:
                self.clients.remove(conn)
                conn.close()
                print("Thread Error : Client Disconnected")
                break

    def send_address(self):
        return self.server_ip

    def start_server(self):
        # loop that accepts new connections and creates threads
        while True:
            # accept new connections
            conn, addr = self.sck.accept()
            self.player_list.append(addr)
            print(f"Connection established with {addr}")
            # Threads creation
            thread_client = threading.Thread(target=self.gerer_client, args=(conn, addr))
            thread_client.start()