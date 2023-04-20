import socket


class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.42" # server ip
        self.port = 6666
        self.client.connect((self.host, self.port))

    def send(self, data):
        print(data)
        # data = data.encode()
        self.client.send(data)

    def receive(self):
        while True:
            data = self.client.recv(2048)
            print(data.decode())