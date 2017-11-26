from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QListView, QApplication, QListWidget
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
import sys
import os
from ui_client import UiClientControl

class MainWindow(QWidget):

    # singal_chart_list_update = pyqtSignal(list)
    # signal_client_status_change = pyqtSignal(str)
    # signal_incoming_msg = pyqtSignal(str)

    def __init__(self, client):
        super().__init__()

        self.__client = client
        self.__initUI()


    # def initUI_list(self):

    def __initUI(self):
        self.__main_win = QHBoxLayout()

        self.__chart_status_win = QVBoxLayout()

        self.__chart_clients = QListWidget()
        self.__chart_status_win.addWidget(self.__chart_clients)

        # self.chart_status = QListView()
        # self.chart_status.setMinimumSize(100, 100)
        # self.chart_status.setWindowTitle('Состояние чата')
        # self.model_chart_status = QStandardItemModel(self.chart_status)
        # self.chart_status_win.addWidget(self.chart_status)

        self.__client_update_status = QListView()
        self.__client_update_status.setMinimumSize(100, 100)
        self.__client_update_status.setWindowTitle('Обновление статуса клиента')
        self.__model_client_status = QStandardItemModel(self.__client_update_status)
        self.__chart_status_win.addWidget(self.__client_update_status)


        self.__msg_window = QListView()
        self.__msg_window.setMinimumSize(700, 400)
        self.__msg_window.setWindowTitle('Общий чат')
        self.__model_chart_list = QStandardItemModel(self.__msg_window)

        self.__msg_input = QLineEdit()
        self.__input_Btn = QPushButton()

        self.__input_Btn.clicked.connect(self.__on_clicked)

        self.__privat_msg_input = QLineEdit()

        self.__main_chart_win = QVBoxLayout()
        self.__main_chart_win.addWidget(self.__msg_window)

        self.__msg_input_with_Btn = QHBoxLayout()
        self.__msg_input_with_Btn.addWidget(self.__msg_input)
        self.__msg_input_with_Btn.addWidget(self.__input_Btn)

        self.__main_chart_win.addLayout(self.__msg_input_with_Btn)

        self.__main_win.addLayout(self.__chart_status_win)
        self.__main_win.addLayout(self.__main_chart_win)

        self.__main_win.addWidget(self.__privat_msg_input)

        self.setLayout(self.__main_win)
        self.setGeometry(300, 300, 300, 100)
        self.show()

        self.__client.signals.singal_chart_list_update.connect(self.__update_chart_status)
        self.__client.signals.signal_client_status_change.connect(self.__print_new_client_status)
        self.__client.signals.signal_incoming_msg.connect(self.__print_msg)

    def __update_chart_status(self, clients_list):
        # clients_list = clients_list.split(';')
        # print(clients_list)
        self.__chart_clients.clear()
        for i in clients_list:
            self.__chart_clients.addItem(i)
        self.__chart_clients.repaint()


    # def update_chart_status(self, clients_list):
    #     clients_list = QStandardIddtem(clients_list)
    #     self.model_chart_status.appendRow(clients_list)
    #     self.client_update_status.setModel(self.model_chart_status)

    def __print_new_client_status(self, client_update_status):
        client_update_status = QStandardItem(client_update_status)
        self.__model_client_status.appendRow(client_update_status)
        self.__client_update_status.setModel(self.__model_client_status)
        self.__client_update_status.repaint()


    # @pyqtSlot(str, name='signal_incoming_msg')
    def __print_msg(self, msg):
        msg = QStandardItem(msg)
        self.__model_chart_list.appendRow(msg)
        self.__msg_window.setModel(self.__model_chart_list)

    def __on_clicked(self):
        msg = self.__msg_input.text()
        self.__client.send_msg(msg)
        self.__msg_input.clear()


    def keyPressEvent(self, event):
        # print(event.key())
        # print(Qt.Key_Enter)
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.__on_clicked()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ui_client = UiClientControl()
    main_win = MainWindow(ui_client)
    ui_client.start_client()
    os._exit(app.exec_())






