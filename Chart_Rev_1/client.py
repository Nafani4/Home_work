from socket import *
from threading import Thread
import sys
import os
import protocol_pb2 #подключаем модуль для серелизации/десерелизации нашего сообщения
from google.protobuf.internal import decoder
import struct


class Client(object):
    """Создаём конструктор клиента, который будет подключаться к заданному хосту сервера"""
    def __init__(self, host, port, bytes_limit):
        self.__host = host
        self.__port = port
        self.__bytes_limit = bytes_limit
        self.__clients_list_client = []

    def ask_name(self):
        """При старте клиента инициализируем его имя"""
        print('Введите имя пользователя')
        self.__client_name = input()
        return self.__client_name

    @property
    def client_name(self):
        return self.__client_name

    def conn_to_server(self):
        """Создаем сокет, подклчаемый к сокету сервера"""
        self.__conn = socket(AF_INET, SOCK_STREAM)
        try:
            self.__conn.connect((self.__host, self.__port))
        except:
            print('Сервер не доступен, попробуйте позже')
            sys.exit(0)

    # def string_to_bytes(self, incoming_string):
    #     bytes_string = incoming_string.encode('utf-8')
    #     return bytes_string

    def read_volume(self, volume):
        result = b''
        while 1:
            real_volume = self.__conn.recv(volume)
            volume -= len(real_volume)
            result += real_volume
            if volume == 0:
                break
        return result

    def write_volume(self, msg):
        real_volume = len(msg)
        while 1:
            sent = self.__conn.send(msg)
            real_volume -= sent
            msg = msg[sent:]
            if real_volume == 0:
                break

    def send_data(self, incoming_string):
        packed_len = struct.pack('>L', len(incoming_string))
        self.write_volume(packed_len + incoming_string)

    def receive_data(self):
        len_buf = self.read_volume(4)
        msg_len = struct.unpack('>L', len_buf)[0]
        data = self.read_volume(msg_len)

        return data

    def add_clients_list(self, clients_list):
        self.__clients_list_client = clients_list

    def get_clients_list(self):
        return self.__clients_list_client

    def close_conn(self):
        self.__conn.close()


class IncomingThread(Thread):
    """Соездаём входящий поток"""
    def __init__(self, client):
        super(IncomingThread, self).__init__()
        self.__client = client

    def run(self):
        while 1:
            try:
                incoming_thread = protocol_pb2.Message()
                a = self.__client.receive_data()
                incoming_thread.ParseFromString(a)
                msg = incoming_thread.msg
                command_key = msg.split(':::')
                if command_key[0] == 'polzovatel2017':
                    client_update_status = ' '.join(command_key[1:])
                    self.client_update_status(client_update_status)
                    continue
                if command_key[0] == 'spisok2017':
                    # clients_list = ' '.join(command_key[1:])
                    clients_list = (command_key[1]).split(';')
                    self.__client.add_clients_list(clients_list)
                    self.update_chart_list(clients_list)
                    continue
                if msg == 'Авторизация не удалась':
                    os._exit(0)
                self.handle_msg(msg)
            except:
                print('Сервер разорвал соединение')
                self.__client.close_conn()
                os._exit(0)

    def update_chart_list(self, clients_list):
        pass

    def client_update_status(self, client_update_status):
        pass

    def handle_msg(self, msg):
        pass



class OutputThread(Thread):
    """Создаём исходящий поток"""
    def __init__(self, client):
        super(OutputThread, self).__init__()
        self.__client = client

    def run(self):
        count = 0
        maxcount = 3
        while count < maxcount:
            my_message = input()
            if not my_message:
                print('Введена пустая строка')
                count += 1
                continue
            if my_message == 'chart_list':
                print(self.__client.get_clients_list())
                continue
            message = protocol_pb2.Message()
            message.msg = my_message
            message.client_name = self.__client.client_name
            self.__client.send_data(message.SerializeToString())
        print('Перезапустите клиент')
        self.__client.close_conn()
        os._exit(0)

    def close_output(self):
        self.__client.close_conn()





