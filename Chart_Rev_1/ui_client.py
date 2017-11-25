from client import IncomingThread, Client, OutputThread
import protocol_pb2 #Подключаем модуль для серелизации/десерелизации нашего сообщения


class UiIncomingThread(IncomingThread):
    def __init__(self, client, main_win):
        super().__init__(client)
        self.main_win = main_win

    def handle_msg(self, msg):
        self.main_win.print_msg(msg)

    def client_update_status(self, client_update_status):
        self.main_win.print_new_client_status(client_update_status)

    def update_chart_list(self, clients_list):
        self.main_win.update_chart_status(clients_list)


class UiClientControl(object):
    """Данный класс обеспечивает старт всех необходимых для подключения к серверу методов других классов.
    Тут стартуем входящий и исходящий потоки"""
    def __init__(self, main_win):
        self.client = Client('localhost', 40001, 3000)
        self.data_thread = UiIncomingThread(self.client, main_win)
        self.output_thread = OutputThread(self.client)

    def send_msg(self, msg):
        message = protocol_pb2.Message()
        message.msg = msg
        # message.client_name = self.client.client_name
        self.client.send_data(message.SerializeToString())

    def start_client(self):
        self.client.conn_to_server()
        self.data_thread.start()
        self.output_thread.start()

# if __name__ == '__main__':
    # ui_incoming_control = UiClientControl()
    # ui_incoming_control.start_client()

