from socket import *
from threading import Thread

class Server(object):
    def __init__(self, HOST, PORT, BACKLOG, bytes_limit):
        self.HOST = HOST
        self.PORT = PORT
        self.BACKLOG = BACKLOG
        self.bytes_limit = bytes_limit

    def start_server(self):
        self.conn = socket(AF_INET, SOCK_STREAM)
        # self.conn.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.conn.bind((self.HOST, self.PORT))
        self.conn.listen(self.BACKLOG)

    def accept_conn(self):
        try:
            in_conn, addr = self.conn.accept()
            return (in_conn, addr)
        except:
            print('Закрываем соединение')
            self.conn.close()

    def incoming_data(self, in_conn):
        while 1:
                data = in_conn.recv(self.bytes_limit)
                return data

    def print_data(self, data):
        print(data)

    def close_conn(self):
        self.conn.close()

class CachDataThread(Thread):
    def __init__(self, stream, server):
        super(CachDataThread, self).__init__()
        self.stream = stream
        self.server = server
    def run(self):
        while 1:
            print(self.server.incoming_data(self.stream))





server_1 = Server('localhost', 40001, 20, 1024)
server_1.start_server()
data_stream = server_1.accept_conn()[0]
data_stream_1 = server_1.accept_conn()[0]
print('connection done')

thread_1 = CachDataThread(data_stream, server_1)
thread_1.start()
thread_2 = CachDataThread(data_stream_1, server_1)
thread_2.start()






