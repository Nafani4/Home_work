from socket import *
from threading import Thread


class Client(object):
    def __init__(self, HOST, PORT, bytes_limit):
        self.HOST = HOST
        self.PORT = PORT
        self.bytes_limit = bytes_limit

    def conn_to_server(self):
        self.conn = socket(AF_INET, SOCK_STREAM)
        self.conn.connect((self.HOST, self.PORT))

    def string_to_bytes(self, incoming_string):
        bytes_string = incoming_string.encode('utf-8')
        return bytes_string

    def send_data(self, incoming_string):
        self.conn.send(self.string_to_bytes(incoming_string))

    def receive_data(self):
        data = self.conn.recv(self.bytes_limit)
        return data

    def close_conn(self):
        self.conn.close()

class DataThread(Thread):
    def __init__(self, client):
        super(DataThread, self).__init__()
        self.client = client
    def run(self):
        while 1:
            try:
                msg = self.client.receive_data().decode('utf-8')
                print(msg)
            except:
                print('Сервер разорвал соединение')
                break

class ConsoleThread(Thread):
    def __init__(self, client):
        super(ConsoleThread, self).__init__()
        self.client = client
    def run(self):
        while 1:
            my_massage = input()
            self.client.send_data(my_massage)
    def close_outpit(self):
        self.client.close_conn()

class ClientControl(object):
    def __init__(self):
        self.client = Client('localhost', 40001, 1024)
        self.data_thread = DataThread(self.client)
        self.console_thread = ConsoleThread(self.client)
    def start_client(self):
        self.client.conn_to_server()
        self.data_thread.start()
        self.console_thread.start()

client_control = ClientControl()
client_control.start_client()