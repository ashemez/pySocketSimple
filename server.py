import socket, pickle, struct

import settings


class Server:

    def receive_exact(self, conn, length):
        buffer = b''
        while len(buffer) < length:
            data = conn.recv(length - len(buffer))
            if not data:
                raise Exception("Connection lost")
            buffer += data
        return buffer

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((settings.HOST, settings.PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    length = self.receive_exact(conn, 4)
                    body_size = struct.unpack("!L", length)[0]
                    body = self.receive_exact(conn, body_size)
                    data = pickle.loads(body)
                    print('Data received from client:')
                    print(data[1])

# test
server = Server()
server.run()
