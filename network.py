import socket


class Network:

    def __init__(self, server_ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = server_ip
        self.port = 6666
        # new connect method
        self.addr = (self.host, self.port)
        self.id = self.connect()
        # original connect method
        #self.client.connect((self.host, self.port))

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
            print("Client connection : OK")
        except:
            print("Client connection : error")

    def send(self, data):
        # New send method
        try:
            data_return = ""
            data_player_list = []
            self.client.send(str.encode(data))
            data_r = self.client.recv(2048).decode()
            #print(f"Client received in send fonction : {data_r}")
            data_split = data_r.split(", ")
            """print("data_r : ", data_r)
            print("data_split[0] : ", data_split[0])"""
            data_split_len = len(data_split)
            if data_split[0] == "IP":
                for i in range(1, data_split_len, 2):
                    data_split[i] = data_split[i].replace("(", "")
                    data_split[i] = data_split[i].replace("'", "")
                    data_player_list.append(data_split[i])
            if data_player_list:
                return data_player_list

        except socket.error as e:
            print(e)



        # Original send method
        # print(f"Client send : {data}")
        ## data = data.encode()
        #self.client.send(data)

    def receive(self):
        data = self.client.recv(2048)
        print(f"Client received in receive function : {data.decode()}")


