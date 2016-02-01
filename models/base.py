# -*- coding: utf-8 -*-

from peewee import Model
from peewee import SqliteDatabase
from peewee import create_model_tables
from peewee import drop_model_tables
from decouple import config

database_name = config('DB_NAME', default='models.db')
database = SqliteDatabase(database_name)


class BaseModel(Model):

    class Meta:
        database = database


class DatabaseOperations(object):

    models = []

    def create_tables(self):
        create_model_tables(*self.models)

    def drop_tables(self):
        drop_model_tables(*self.models)

    def export_data(self):
        pass
