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
            data = (in_conn.recv(self.bytes_limit)).decode('utf-8')
            return data

    def print_data(self, data):
        print(data)

    def close_conn(self):
        self.conn.close()

class DataThread(Thread):
    def __init__(self, stream, server, client_ip, remove_thread, send_msg):
        super(DataThread, self).__init__()
        self.stream = stream
        self.server = server
        self.client_ip = client_ip
        self.remove_thread = remove_thread
        self.send_msg = send_msg
    def run(self):
        while 1:
            try:
                """Аутефикация пользователя"""
                self.stream.send('Введите имя пользователя'.encode('utf-8'))
                msg = self.server.incoming_data(self.stream)
                self.stream.send('Введите пароль'.encode('utf-8'))
                msg = self.server.incoming_data(self.stream)
                """Приём собщений"""
                msg = self.server.incoming_data(self.stream).encode('utf-8')
                self.send_msg(msg)
            except:
                print('Клиет {} вышел из чата'.format(self.client_ip))
                self.remove_thread(self)
                break
    def close_thread(self):
        self.stream.close()

    def send_data(self, msg):
        self.stream.send(msg)

class ConnThread(Thread):
    def __init__(self, server):
        super(ConnThread, self).__init__()
        self.server = server
        self.conn_list = []
    def run(self):
        while 1:
            (a, b) = self.server.accept_conn()
            in_thread = DataThread(a, self.server, b, self.remove_thread, self.send_msg)
            self.conn_list.append(in_thread)
            in_thread.start()

    def remove_thread(self, disconnected_thread):
        disconnected_thread.close_thread()
        self.conn_list.remove(disconnected_thread)
    def send_msg(self, msg):
        for i in self.conn_list:
            i.send_data(msg)


server_1 = Server('localhost', 40001, 20, 1024)
server_1.start_server()

incoming_thread = ConnThread(server_1).start()







