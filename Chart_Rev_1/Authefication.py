while 1:
                """Аутефикация пользователя"""
                self.stream.send('Существующий пользователь - введите 1. Если хотите зарегистрироваться - введите 0'.encode('utf-8'))
                msg = self.server.incoming_data(self.stream)
                if msg == '1':
                    self.stream.send('Введите имя пользователя'.encode('utf-8'))
                    msg = self.server.incoming_data(self.stream)
                    if msg != database.read_name_by_name(msg):
                        self.stream.send('Имя пользователя не существует, попробуйте снова'.encode('utf-8'))
                        break
                    self.stream.send('Введите пароль'.encode('utf-8'))
                    msg = self.server.incoming_data(self.stream)
                    if msg != database.read_pass_by_name(msg):
                        self.stream.send('Пароль введён неверно, попробуйте снова'.encode('utf-8'))
                        break