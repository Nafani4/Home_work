from socket import *


class Client(object):
    def __init__(self, HOST, PORT, bytes_limit):
        self.HOST = HOST
        self.PORT = PORT
        self.bytes_limit = bytes_limit

    def conn_to_server(self):
        self.conn = socket(AF_INET, SOCK_STREAM)
        self.conn.connect((self.HOST, self.PORT))

    def string_to_bytes(self, incoming_string):
        bytes_string = bytes(incoming_string, 'utf-8')
        return bytes_string

    def send_data(self, incoming_string):
        self.conn.send(self.string_to_bytes(incoming_string))

    def receive_data(self):
        data = self.conn.recv(self.bytes_limit)
        return data

    def close_conn(self):
        self.conn.close()

class ConsoleClient(object):
    def __init__(self, client_1):
        self.client_1 = client_1
    def input_data(self):
        while 1:
            my_massage = input()
            self.client_1.send_data(my_massage)


client_1 = Client('localhost', 40001, 1024)
client_1.conn_to_server()
massager = ConsoleClient(client_1)
massager.input_data()
client_1.receive_data()
client_1.close_conn()
