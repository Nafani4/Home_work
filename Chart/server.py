from socket import *

class Server(object):
    def __init__(self, HOST, PORT, BACKLOG, bytes_limit):
        self.HOST = HOST
        self.PORT = PORT
        self.BACKLOG = BACKLOG
        self.bytes_limit = bytes_limit

    def start_server(self):
        self.conn = socket(AF_INET, SOCK_STREAM)
        self.conn.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.conn.bind((self.HOST, self.PORT))
        self.conn.listen(self.BACKLOG)

    def accept_conn(self):
        try:
            in_conn, addr = self.conn.accept()
            return (in_conn, addr)
        finally:
            print('Закрываем соединение')
            self.conn.close()

    def echo(self, in_conn):
        while 1:
            data = in_conn.recv(self.bytes_limit)
            print(data)
            if not data:
                break
            in_conn.send(data)
        self.conn.close()
        in_conn.close()

server_1 = Server('localhost', 40001, 20, 1024)
server_1.start_server()
opens = server_1.accept_conn()[0]
server_1.echo(opens)
