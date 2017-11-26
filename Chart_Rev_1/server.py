from socket import *
from threading import Thread
import database #Импортируем модуль, отвечающий за соединение с базой данных имён и паролей
import validators #Подключаем модуль, где описаны механизмы валидации имён и паролей
import protocol_pb2 #Подключаем модуль для серелизации/десерелизации нашего сообщения
import struct #Штука в которой нихера не понимаю


class Server(object):
    """Создаем конструктор сервера и передаем ему параметры соединения"""
    def __init__(self, host, port, backlog):
        self.__host = host
        self.__port = port
        self.__backlog = backlog

    def start_server(self):
        """Создаем сокер, биндим его на открытое соединение и начинаем прослушивать открытый сокет"""
        self.__conn = socket(AF_INET, SOCK_STREAM)
        # self.conn.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.__conn.bind((self.__host, self.__port))
        self.__conn.listen(self.__backlog)

    def accept_conn(self):
        """Получаем параметры входящее сокета"""
        try:
            in_conn, addr = self.__conn.accept()
            return (in_conn, addr)
        except:
            print('Закрываем соединение')
            self.__conn.close()

    def close_conn(self):
        self.__conn.close()

class ConnThread(Thread):
    """Открываем отдельный поток на входящий сокет"""
    def __init__(self, server, connected_clients):
        super().__init__()
        self.__server = server
        self.__connected_clients = connected_clients
    def run(self):
        while 1:
            (stream, client_ip) = self.__server.accept_conn()
            """Начало авторизации"""
            Authorization(stream, client_ip, self.__connected_clients).start()


class DataThread(Thread):
    """Поток общения после прохождения авторизации"""
    def __init__(self, stream, client_ip, connected_clients, client_name):
        super(DataThread, self).__init__()
        self.__stream = stream
        self.__client_ip = client_ip
        self.__connected_clients = connected_clients
        self.__client_name = client_name
    def run(self):
        while 1:
            """Приём собщений"""
            try:
                incoming_thread = protocol_pb2.Message()
                incoming_thread.ParseFromString(incoming_data(self.__stream))
                # client_name = incoming_thread.client_name
                msg = incoming_thread.msg
                # if msg == 'chart_list':
                #     for name in self.connected_clients.dict:
                #         for name in self.connected_clients.dict:
                #             self.connected_clients.dict[name].send_data(
                #                 self.connected_clients.string_of_online_clients()
                #             )
                for name in self.__connected_clients.dict:
                    self.__connected_clients.dict[name].send_data(msg)
            except:
                print('Клиет {} вышел из чата'.format(self.__client_ip))
                self.__connected_clients.remove_from_online_clients(self.__client_name)
                self.__stream.close()
                for name in self.__connected_clients.dict:
                    self.__connected_clients.dict[name].send_data(self.__connected_clients.string_of_online_clients())
                    self.__connected_clients.dict[name].send_data('polzovatel2017:::Пользователь {} '
                                                                'покинул чат'.format(self.__client_name))
                break

    def send_data(self, msg):
        send_msg(self.__stream, msg)


class ConnectedClients(object):
    """Создаём словарик с on-line клиентами"""
    def __init__(self):
        self.__connected_clients = {}
    def add_online_clients(self, client_name, data_thread):
        self.__connected_clients[client_name] = data_thread
    def remove_from_online_clients(self, client_name):
        del self.__connected_clients[client_name]
    def string_of_online_clients(self):
        string_of_of_line_clients = 'spisok2017:::' + ';'.join(self.__connected_clients.keys())
        return string_of_of_line_clients
    def find_by_name(self, client_name):
        for i in self.__connected_clients:
            if client_name == i:
                return True
        return False
    @property
    def dict(self):
        return self.__connected_clients


class Authorization(Thread):
    """Поток авторизация клиента"""
    def __init__(self, stream, client_ip, connected_clients):
        super().__init__()
        self.__stream = stream
        self.__client_ip = client_ip
        self.__connected_clients = connected_clients
    def run(self):
        count = 0
        maxcount = 3
        try:
            while count<maxcount:
                """Аутефикация пользователя"""
                send_msg(self.__stream,
                         'Существующий пользователь - введите 1. Если хотите зарегистрироваться - введите 0'
                         )
                incoming_thread = protocol_pb2.Message()
                incoming_thread.ParseFromString(incoming_data(self.__stream))
                msg = incoming_thread.msg
                if msg != '1' and msg != '0':
                    send_msg(self.__stream, 'Введите либо 0 либо 1')
                    count += 1
                    continue
                """Аутефикация существующего пользователя"""
                if msg == '1':
                    send_msg(self.__stream, 'Введите имя пользователя')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.__stream))
                    client_name = incoming_thread.msg
                    if client_name != database.read_name_by_name(client_name) or self.__connected_clients.find_by_name(client_name):
                        count += 1
                        send_msg(self.__stream, 'Имя пользователя не существует или пользователь онлайн,'
                                              ' попробуйте снова.'
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.__stream, 'Введите пароль')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.__stream))
                    msg = incoming_thread.msg
                    if msg != database.read_pass_by_name(client_name):
                        count += 1
                        send_msg(self.__stream, 'Пароль введён неверно, попробуйте снова. '
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    """Создаём поток для общения авторизованного клиента"""
                    send_msg(self.__stream, 'Добро пожаловать в общий чат')
                    data_thread = DataThread(self.__stream, self.__client_ip, self.__connected_clients, client_name)
                    self.__connected_clients.add_online_clients(client_name, data_thread)
                    for name in self.__connected_clients.dict:
                        self.__connected_clients.dict[name].send_data(self.__connected_clients.string_of_online_clients())
                    for name in self.__connected_clients.dict:
                        self.__connected_clients.dict[name].send_data('polzovatel2017:::Пользователь {} '
                                                                    'присоединился к чату'.format(client_name))
                    data_thread.start()
                    break
                """Аутефикация нового пользователя"""
                if msg == '0':
                    send_msg(self.__stream, 'Введите имя пользователя. Только латинские буквы и цифры')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.__stream))
                    client_name = incoming_thread.msg
                    if not client_name or validators.name_validator(client_name) == False:
                        count += 1
                        send_msg(self.__stream, 'Неверный ввод, осталось {} попыток'.format(maxcount - count))
                        continue
                    if client_name == database.read_name_by_name(client_name):
                        count += 1
                        send_msg(self.__stream, 'Пользователь с таким именем существует, попробуйте снова.'
                                              'Осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.__stream, 'Введите пароль')
                    incoming_thread = protocol_pb2.Message()
                    incoming_thread.ParseFromString(incoming_data(self.__stream))
                    client_pass = incoming_thread.msg
                    if not client_pass or validators.name_validator(client_name) == False:
                        count += 1
                        send_msg(self.__stream, 'Неверный ввод, осталось {} попыток'.format(maxcount - count))
                        continue
                    send_msg(self.__stream, 'Пользователь {} добавлен, пройдите '
                                          'авторизацию для существующего пользователя'.format(client_name))
                    database.add_to_base(client_name, client_pass)

                    count = 0

            if count == maxcount:
                send_msg(self.__stream, 'Авторизация не удалась')
        except:
            print('Клиет {} вышел из чата'.format(self.__client_ip))
            self.__stream.close()


def read_volume(in_conn, volume):
    result = b''
    while 1:
        real_volume = in_conn.recv(volume)
        volume -= len(real_volume)
        result += real_volume
        if volume == 0:
            break
    return result

def write_volume(in_conn, msg):
    real_volume = len(msg)
    while 1:
        sent = in_conn.send(msg)
        real_volume -= sent
        msg = msg[sent:]
        if real_volume == 0:
            break


def incoming_data(in_conn, bytes_limit=10000):
    len_buf = read_volume(in_conn, 4)
    msg_len = struct.unpack('>L', len_buf)[0]
    data = read_volume(in_conn, msg_len)

    return data

def send_msg(in_conn, msg):
    message = protocol_pb2.Message()
    message.msg = msg
    message = message.SerializeToString()
    packed_len = struct.pack('>L', len(message))
    write_volume(in_conn, packed_len + message)

server_1 = Server('localhost', 40001, 20)
server_1.start_server()
connected_clients = ConnectedClients()
ConnThread(server_1, connected_clients).start()

