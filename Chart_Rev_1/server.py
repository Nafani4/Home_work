from socket import *
from threading import Thread
import database #Импортируем модуль, отвечающий за соединение с базой данных имён и паролей
import validators #Подключаем модуль, где описаны механизмы валидации имён и паролей
import protocol_pb2 #Подключаем модуль для серелизации/десерелизации нашего сообщения


class Server(object):
    """Создаем конструктор сервера и передаем ему параметры соединения"""
    def __init__(self, host, port, backlog):
        self.host = host
        self.port = port
        self.backlog = backlog

    def start_server(self):
        """Создаем сокер, биндим его на открытое соединение и начинаем прослушивать открытый сокет"""
        self.conn = socket(AF_INET, SOCK_STREAM)
        # self.conn.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.conn.bind((self.host, self.port))
        self.conn.listen(self.backlog)

    def accept_conn(self):
        """Получаем параметры входящее сокета"""
        try:
            in_conn, addr = self.conn.accept()
            return (in_conn, addr)
        except:
            print('Закрываем соединение')
            self.conn.close()

    def close_conn(self):
        self.conn.close()

class ConnThread(Thread):
    """Открываем отдельный поток на входящий сокет"""
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
    """Поток общения после прохождения авторизации"""
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
                # client_name = incoming_thread.client_name
                msg = incoming_thread.msg
                for name in self.connected_clients.dict:
                    self.connected_clients.dict[name].send_data(msg)
            except:
                print('Клиет {} вышел из чата'.format(self.client_ip))
                self.connected_clients.remove_from_online_clients(self.client_name)
                for name in self.connected_clients.dict:
                    self.connected_clients.dict[name].send_data(self.connected_clients.string_of_online_clients())
                    self.connected_clients.dict[name].send_data('polzovatel2017:::Пользователь {} '
                                                                'покинул к чат'.format(self.client_name))
                break
    def send_data(self, msg):
        send_msg(self.stream, msg)


class ConnectedClients(object):
    """Создаём словарик с on-line клиентами"""
    def __init__(self):
        self.connected_clients = {}
    def add_online_clients(self, client_name, data_thread):
        self.connected_clients[client_name] = data_thread
    def remove_from_online_clients(self, client_name):
        del self.connected_clients[client_name]
    def string_of_online_clients(self):
        string_of_of_line_clients = 'spisok2017:::' + ';'.join(self.connected_clients.keys())
        return string_of_of_line_clients
    @property
    def dict(self):
        return self.connected_clients


class Authorization(Thread):
    """Поток авторизация клиента"""
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
                """Аутефикация существующего пользователя"""
                if msg == '1':
                    send_msg(self.stream, 'Введите имя пользователя')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.stream))
                    client_name = incoming_thread.msg
                    if client_name != database.read_name_by_name(client_name):
                        count += 1
                        send_msg(self.stream, 'Имя пользователя не существует, попробуйте снова.'
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.stream, 'Введите пароль')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.stream))
                    msg = incoming_thread.msg
                    if msg != database.read_pass_by_name(msg):
                        count += 1
                        send_msg(self.stream, 'Пароль введён неверно, попробуйте снова. '
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    """Создаём поток для общения авторизованного клиента"""
                    send_msg(self.stream, 'Добро пожаловать в общий чат')
                    data_thread = DataThread(self.stream, self.client_ip, self.connected_clients, client_name)
                    self.connected_clients.add_online_clients(client_name, data_thread)
                    # self.connected_clients.string_of_online_clients()
                    for name in self.connected_clients.dict:
                        self.connected_clients.dict[name].send_data(self.connected_clients.string_of_online_clients())
                        self.connected_clients.dict[name].send_data('polzovatel2017:::Пользователь {} '
                                                                    'присоединился к чату'.format(client_name))
                    # send_msg(self.stream, self.connected_clients.string_of_online_clients())
                    data_thread.start()
                    break
                """Аутефикация нового пользователя"""
                if msg == '0':
                    send_msg(self.stream, 'Введите имя пользователя. Только латинские буквы и цифры')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.stream))
                    client_name = incoming_thread.msg
                    if not client_name or validators.name_validator(client_name) == False:
                        count += 1
                        send_msg(self.stream, 'Неверный ввод, осталось {} попыток'.format(maxcount - count))
                        continue
                    if client_name == database.read_name_by_name(client_name):
                        count += 1
                        send_msg(self.stream, 'Пользователь с таким именем существует, попробуйте снова.'
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.stream, 'Введите пароль')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.stream))
                    client_pass = incoming_thread.msg
                    if not client_pass or validators.name_validator(client_name) == False:
                        count += 1
                        send_msg(self.stream, 'Неверный ввод, осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.stream, 'Пользователь {} добавлен, пройдите '
                                          'авторизацию для существующего пользователя'.format(client_name))
                    database.add_to_base(client_name, client_pass)

                    count = 0

            if count == maxcount:
                send_msg(self.stream, 'Авторизация не удалась')
        except:
            print('Клиет {} вышел из чата'.format(self.client_ip))


def incoming_data(in_conn, bytes_limit=3000):
        data = (in_conn.recv(bytes_limit))
        return data

def send_msg(in_conn, msg):
    message = protocol_pb2.Message()
    message.msg = msg
    in_conn.send(message.SerializeToString())


server_1 = Server('localhost', 40001, 20)
server_1.start_server()
connected_clients = ConnectedClients()
ConnThread(server_1, connected_clients).start()






