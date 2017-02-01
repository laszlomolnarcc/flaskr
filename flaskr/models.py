from connectdatabase import ConnectDatabase
from peewee import *


class Entries(Model):
    title = CharField()
    text = CharField()

    class Meta:
        database = ConnectDatabase.db
