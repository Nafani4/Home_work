from datetime import date
from pony.orm import *


db = Database()

# class ClientMassage(db.Entity):
#     massage_time = Required(date)
#     massage_body = Required(str)
#     massage_sent_by = Required(str)
#     massage_sent_to = Optional(str)
#
# db.bind(provider='sqlite', filename='massage_base.sql', create_db=True)
# db.generate_mapping(create_tables=True)
#
# def add_to_base(massage_time, massage_body, massage_sent_by):
#     with db_session():
#          current_massage = ClientMassage(massage_time=massage_time, massage_body=massage_body, massage_sent_by=massage_sent_by)
#
# def read_by_name(name):
#     with db_session():
#         return select(p for p in ClientMassage if p.massage_sent_by == name)

class LoginBase(db.Entity):
    client_name = Required(str)
    client_pass = Required(str)

db.bind(provider='sqlite', filename='logs_and_pass.sql', create_db=True)

db.generate_mapping(create_tables=True)

def add_to_base(client_name, client_pass):
    with db_session():
         client = LoginBase(client_name=client_name, client_pass=client_pass)

def read_by_name(name):
    with db_session():
        return select (p for p in LoginBase if p.client_name == name)[:]

# @db_session
# def get_pass_by_name(client_name):
#     p = LoginBase(client_name=client_name)
#     return p.client_pass


