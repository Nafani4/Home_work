from client import IncomingThread, Client, OutputThread
import protocol_pb2 #Подключаем модуль для серелизации/десерелизации нашего сообщения
# from user_interface import MainWindow
from PyQt5.QtCore import pyqtSignal, QObject


class Signals(QObject):
    singal_chart_list_update = pyqtSignal(list)
    signal_client_status_change = pyqtSignal(str)
    signal_incoming_msg = pyqtSignal(str)


class UiIncomingThread(IncomingThread):
    def __init__(self, client):
        super().__init__(client)

        self.__signals = Signals()

    @property
    def get_signals(self):
        return self.__signals

    def handle_msg(self, msg):
        self.__signals.signal_incoming_msg.emit(msg)

    def client_update_status(self, client_update_status):
        self.__signals.signal_client_status_change.emit(client_update_status)

    def update_chart_list(self, clients_list):
        self.__signals.singal_chart_list_update.emit(clients_list)


class UiClientControl(object):
    """Данный класс обеспечивает старт всех необходимых для подключения к серверу методов других классов.
    Тут стартуем входящий и исходящий потоки"""
    def __init__(self):
        self.__client = Client('localhost', 40001, 3000)
        self.__data_thread = UiIncomingThread(self.__client)

    @property
    def signals(self):
        return self.__data_thread.get_signals

    def send_msg(self, msg):
        message = protocol_pb2.Message()
        message.msg = msg
        # message.client_name = self.client.client_name
        self.__client.send_data(message.SerializeToString())

    def start_client(self):
        self.__client.conn_to_server()
        self.__data_thread.start()

# if __name__ == '__main__':
    # ui_incoming_control = UiClientControl()
    # ui_incoming_control.start_client()

