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

        self.client = client
        self.initUI()


    # def initUI_list(self):

    def initUI(self):
        self.main_win = QHBoxLayout()

        self.chart_status_win = QVBoxLayout()

        self.chart_clients = QListWidget()
        self.chart_status_win.addWidget(self.chart_clients)

        # self.chart_status = QListView()
        # self.chart_status.setMinimumSize(100, 100)
        # self.chart_status.setWindowTitle('Состояние чата')
        # self.model_chart_status = QStandardItemModel(self.chart_status)
        # self.chart_status_win.addWidget(self.chart_status)

        self.client_update_status = QListView()
        self.client_update_status.setMinimumSize(100, 100)
        self.client_update_status.setWindowTitle('Обновление статуса клиента')
        self.model_client_status = QStandardItemModel(self.client_update_status)
        self.chart_status_win.addWidget(self.client_update_status)


        self.msg_window = QListView()
        self.msg_window.setMinimumSize(700, 400)
        self.msg_window.setWindowTitle('Общий чат')
        self.model_chart_list = QStandardItemModel(self.msg_window)

        self.msg_input = QLineEdit()
        self.input_Btn = QPushButton()

        self.input_Btn.clicked.connect(self.on_clicked)

        self.privat_msg_input = QLineEdit()

        self.main_chart_win = QVBoxLayout()
        self.main_chart_win.addWidget(self.msg_window)

        self.msg_input_with_Btn = QHBoxLayout()
        self.msg_input_with_Btn.addWidget(self.msg_input)
        self.msg_input_with_Btn.addWidget(self.input_Btn)

        self.main_chart_win.addLayout(self.msg_input_with_Btn)

        self.main_win.addLayout(self.chart_status_win)
        self.main_win.addLayout(self.main_chart_win)

        self.main_win.addWidget(self.privat_msg_input)

        self.setLayout(self.main_win)
        self.setGeometry(300, 300, 300, 100)
        self.show()

        self.client.signals.singal_chart_list_update.connect(self.update_chart_status)
        self.client.signals.signal_client_status_change.connect(self.print_new_client_status)
        self.client.signals.signal_incoming_msg.connect(self.print_msg)

    def update_chart_status(self, clients_list):
        # clients_list = clients_list.split(';')
        # print(clients_list)
        self.chart_clients.clear()
        for i in clients_list:
            self.chart_clients.addItem(i)
        self.chart_clients.repaint()


    # def update_chart_status(self, clients_list):
    #     clients_list = QStandardIddtem(clients_list)
    #     self.model_chart_status.appendRow(clients_list)
    #     self.client_update_status.setModel(self.model_chart_status)

    def print_new_client_status(self, client_update_status):
        client_update_status = QStandardItem(client_update_status)
        self.model_client_status.appendRow(client_update_status)
        self.client_update_status.setModel(self.model_client_status)
        self.client_update_status.repaint()


    # @pyqtSlot(str, name='signal_incoming_msg')
    def print_msg(self, msg):
        msg = QStandardItem(msg)
        self.model_chart_list.appendRow(msg)
        self.msg_window.setModel(self.model_chart_list)

    def on_clicked(self):
        msg = self.msg_input.text()
        self.client.send_msg(msg)
        self.msg_input.clear()


    def keyPressEvent(self, event):
        # print(event.key())
        # print(Qt.Key_Enter)
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.on_clicked()



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ui_client = UiClientControl()
    main_win = MainWindow(ui_client)
    ui_client.start_client()
    os._exit(app.exec_())






