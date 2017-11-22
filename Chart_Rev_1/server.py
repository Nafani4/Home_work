from socket import *
from threading import Thread
import sys
import database
import validators
import protocol_pb2



class Server(object):
    def __init__(self, HOST, PORT, BACKLOG):
        self.HOST = HOST
        self.PORT = PORT
        self.BACKLOG = BACKLOG

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

    def close_conn(self):
        self.conn.close()

class ConnThread(Thread):
    def __init__(self, server, connected_clients):
        super().__init__()
        self.server = server
        self.connected_clients = connected_clients
    def run(self):
        while 1:
            (stream, client_ip) = self.server.accept_conn()
            """Начало авторизации"""
            Authorization(stream, client_ip, self.connected_clients).start()



class DataThread(Thread):
    def __init__(self, stream, client_ip, connected_clients, client_name):
        super(DataThread, self).__init__()
        self.stream = stream
        self.client_ip = client_ip
        self.connected_clients = connected_clients
        self.client_name = client_name
    def run(self):
        while 1:
            """Приём собщений"""
            try:
                incoming_thread = protocol_pb2.Message()
                incoming_thread.ParseFromString(incoming_data(self.stream))
                client_name = incoming_thread.client_name
                msg = incoming_thread.msg
                for name in self.connected_clients.dict:
                    self.connected_clients.dict[name].send_data(msg)
            except:
                print('Клиет {} вышел из чата'.format(self.client_ip))
                self.connected_clients.remove_from_online_users(self.client_name)
                break
    def send_data(self, msg):
        send_msg(self.stream, msg)


class ConnectedClients(object):
    def __init__(self):
        self.connected_users = {}
    def add_online_user(self, client_name, data_thread):
        self.connected_users[client_name] = data_thread
    def remove_from_online_users(self, client_name):
        del self.connected_users[client_name]
    @property
    def dict(self):
        return self.connected_users


class Authorization(Thread):
    def __init__(self, stream, client_ip, connected_clients):
        super().__init__()
        self.stream = stream
        self.client_ip = client_ip
        self.connected_clients = connected_clients
    def run(self):
        count = 0
        maxcount = 3
        try:
            while count<maxcount:
                """Аутефикация пользователя"""
                send_msg(self.stream,
                         'Существующий пользователь - введите 1. Если хотите зарегистрироваться - введите 0'
                )
                incoming_thread = protocol_pb2.Message()
                incoming_thread.ParseFromString(incoming_data(self.stream))
                msg = incoming_thread.msg
                if msg != '1' and msg != '0':
                    send_msg(self.stream,'Введите либо 0 либо 1')
                    count += 1
                    continue
                if msg == '1':
                    send_msg(self.stream, 'Введите имя пользователя')
                    incoming_thread.ParseFromString(incoming_data(self.stream))
                    client_name = incoming_thread.client_name
                    if client_name != database.read_name_by_name(client_name):
                        count += 1
                        send_msg(self.stream, 'Имя пользователя не существует, попробуйте снова.'
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.stream, 'Введите пароль')
                    incoming_thread.ParseFromString(incoming_data(self.stream))
                    msg = incoming_thread.msg
                    if msg != database.read_pass_by_name(msg):
                        count += 1
                        send_msg(self.stream, 'Пароль введён неверно, попробуйте снова. '
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    """Создать поток для общения"""
                    data_tread = DataThread(self.stream, self.client_ip, self.connected_clients, client_name)
                    self.connected_clients.add_online_user(client_name, data_tread)
                    data_tread.start()
                    break
                if msg == '0':
                    send_msg(self.stream, 'Введите имя пользователя. Только латинские буквы и цифры')
                    client_name = incoming_data(self.stream)
                    if not client_name or validators.name_validator(client_name) == False:
                        count += 1
                        send_msg(self.stream, 'Неверный ввод, осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.stream, 'Введите пароль')
                    clent_pass = incoming_data(self.stream)
                    if not clent_pass or validators.name_validator(client_name) == False:
                        count += 1
                        send_msg(self.stream, 'Неверный ввод, осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.stream, 'Пользователь {} добавлен, пройдите '
                                          'авторизацию для существующего пользователя'.format(client_name))
                    database.add_to_base(client_name, clent_pass)
                    count = 0

            if count == maxcount:
                send_msg(self.stream, 'Авторизация не удалась')
        except:
            print('Клиет {} вышел из чата'.format(self.client_ip))


def incoming_data(in_conn, bytes_limit=3000):
        data = (in_conn.recv(bytes_limit))
        return data


def send_msg(in_conn, msg):
    in_conn.send(msg.encode('utf-8'))


server_1 = Server('localhost', 40001, 20)
server_1.start_server()
connected_clients = ConnectedClients()
ConnThread(server_1, connected_clients).start()






