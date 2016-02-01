# -*- coding: utf-8 -*-

from .base import BaseModel
from peewee import BooleanField
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import TextField


class FolderModel(BaseModel):
    path = CharField()
    files = TextField()
    size = IntegerField()
    cre_date = DateTimeField()
    mod_date = DateTimeField()

    def __unicode__(self):
        return self.path
