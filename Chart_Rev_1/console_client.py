from client import IncomingThread, Client, OutputThread

class ConsoleIncomingThread(IncomingThread):
    def __init__(self, client):
        super().__init__(client)

    def handle_msg(self, msg):
        print(msg)

    def client_update_status(self, client_update_status):
        print(client_update_status)

    # def update_chart_list(self, clients_list):
    #     print('Список участников чата {}'.format(clients_list))


class ConsoleClientControl(object):
    """Данный класс обеспечивает старт всех необходимых для подключения к серверу методов других классов.
    Тут стартуем входящий и исходящий потоки"""
    def __init__(self):
        self.__client = Client('localhost', 40001, 3000)
        self.__data_thread = ConsoleIncomingThread(self.__client)
        self.__console_thread = OutputThread(self.__client)

    def start_client(self):
        self.__client.ask_name()
        self.__client.conn_to_server()
        self.__data_thread.start()
        self.__console_thread.start()

client_control = ConsoleClientControl()
client_control.start_client()