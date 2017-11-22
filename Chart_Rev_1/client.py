from socket import *
from threading import Thread
import sys
import os
import protocol_pb2



class Client(object):
    def __init__(self, HOST, PORT, bytes_limit):
        self.HOST = HOST
        self.PORT = PORT
        self.bytes_limit = bytes_limit

    def ask_name(self):
        print('Введите имя: ')
        self.client_name = input()

    def conn_to_server(self):
        self.conn = socket(AF_INET, SOCK_STREAM)
        try:
            self.conn.connect((self.HOST, self.PORT))
        except:
            print('Сервер не доступен, попробуйте позже')
            sys.exit(0)

    # def string_to_bytes(self, incoming_string):
    #     bytes_string = incoming_string.encode('utf-8')
    #     return bytes_string

    def send_data(self, incoming_string):
        self.conn.send(incoming_string)

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
                if msg == 'Авторизация не удалась':
                    os._exit(0)
                print(msg)
            except:
                print('Сервер разорвал соединение')
                os._exit(0)

class ConsoleThread(Thread):
    def __init__(self, client):
        super(ConsoleThread, self).__init__()
        self.client = client
    def run(self):
        count = 0
        maxcount = 3
        while count<maxcount:
            my_message = input()
            if not my_message:
                print('Введена пустая строка')
                count += 1
            message = protocol_pb2.Message()
            message.client_name = self.client.client_name
            message.msg = my_message
            self.client.send_data(message.SerializeToString())
        print('Перезапустите клиент')
        os._exit(0)
    def close_outpit(self):
        self.client.close_conn()

class ClientControl(object):
    def __init__(self):
        self.client = Client('localhost', 40001, 1024)
        self.data_thread = DataThread(self.client)
        self.console_thread = ConsoleThread(self.client)
    def start_client(self):
        self.client.ask_name()
        self.client.conn_to_server()
        self.data_thread.start()
        self.console_thread.start()

client_control = ClientControl()
client_control.start_client()