from datetime import date
from pony.orm import *


db = Database()

class LoginBase(db.Entity):
    client_name = Required(str)
    client_pass = Required(str)

db.bind(provider='sqlite', filename='logs_and_pass.sql', create_db=True)

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
        u = LoginBase.get(client_pass=name)
        if u:
            return u.client_pass
        return None



if __name__ == '__main__':
    with db_session:
        LoginBase.select().show()



