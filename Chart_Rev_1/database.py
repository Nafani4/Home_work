from datetime import datetime
from pony.orm import *


db = Database()


class LoginBase(db.Entity):
    client_name = Required(str)
    client_pass = Required(str)


class Logs(db.Entity):
    from_client = Required(str)
    to_client = Optional(str)
    message = Required(str)
    time = Required(datetime)


db.bind(provider='sqlite', filename='names_and_pass.sql', create_db=True)

db.generate_mapping(create_tables=True)

def add_to_base(client_name, client_pass):
    with db_session():
         client = LoginBase(client_name=client_name, client_pass=client_pass)

def read_name_by_name(name):
    with db_session():
        u = LoginBase.get(client_name=name)
        if u:
            return u.client_name
        return None

def read_pass_by_name(name):
    with db_session():
        u = LoginBase.get(client_name=name)
        if u:
            return u.client_pass
        return None

# def read_by_from_client(name):
#     with db_session():
#         u = Logs.get(client_name=name)
#         if u:
#             return show(u)

# def del_client_by_name(name):
#     with db_session():
#         del u = LoginBase.get(client_name=name)

if __name__ == '__main__':
    with db_session:
        LoginBase.select().show()
        print(read_name_by_name('ss'))
        print(read_pass_by_name('ss'))
        # Logs.select().show()
        # print(read_by_from_client('ss'))





