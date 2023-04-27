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
            self.client.send(str.encode(data))
            data_r = self.client.recv(2048).decode()
            print(f"Client received in send fonction : {data_r}")

        except socket.error as e:
            print(e)



        # Original send method
        # print(f"Client send : {data}")
        ## data = data.encode()
        #self.client.send(data)

    def receive(self):
        data = self.client.recv(2048)
        print(f"Client received in receive function : {data.decode()}")
        return data.decode()
