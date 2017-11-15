from datetime import date
from pony.orm import *


db = Database()

class ClientMassage(db.Entity):
    massage_time = Required(date)
    massage_body = Required(str)
    massage_sent_by = Required(str)
    massage_sent_to = Optional(str)

db.bind(provider='sqlite', filename='massage_base.sql', create_db=True)
db.generate_mapping(create_tables=True)

def add_to_base(massage_time, massage_body, massage_sent_by):
    with db_session():
         current_massage = ClientMassage(massage_time=massage_time, massage_body=massage_body, massage_sent_by=massage_sent_by)

def read_by_name(name):
    with db_session():
        return select(p for p in ClientMassage if p.massage_sent_by == name)








