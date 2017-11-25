from client import IncomingThread, Client, OutputThread

class ConsoleIncomingThread(IncomingThread):
    def __init__(self, client):
        super().__init__(client)

    def handle_msg(self, msg):
        print(msg)

    def client_update_status(self, client_update_status):
        print(client_update_status)


class ConsoleClientControl(object):
    """Данный класс обеспечивает старт всех необходимых для подключения к серверу методов других классов.
    Тут стартуем входящий и исходящий потоки"""
    def __init__(self):
        self.client = Client('localhost', 40001, 3000)
        self.data_thread = ConsoleIncomingThread(self.client)
        self.console_thread = OutputThread(self.client)

    def start_client(self):
        self.client.ask_name()
        self.client.conn_to_server()
        self.data_thread.start()
        self.console_thread.start()

client_control = ConsoleClientControl()
client_control.start_client()