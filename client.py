import socket, pickle

from client_data import ClientData

import settings

class Client:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.server.connect((settings.HOST, settings.PORT))

    def send_data(self, data):
        cdata = ClientData(data)
        data_str = pickle.dumps(cdata)
        self.server.send(data_str)
        print('Data Sent to Server')

    def close_conn(self):
        self.server.close()
