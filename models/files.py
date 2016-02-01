# -*- coding: utf-8 -*-

from .base import BaseModel
from peewee import BooleanField
from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import TextField


class CommonFile(BaseModel):
    name = CharField()
    ext = CharField()
    size = IntegerField()
    cre_date = DateTimeField()
    mod_date = DateTimeField()

    def __unicode__(self):
        return self.name + self.ext


class CommonFolder(BaseModel):
    path = CharField()
    depth = IntegerField()
    dirs = TextField()
    files = TextField()


class ID3Tag(BaseModel):
    pass


class MusicFile(CommonFile):
    listened = BooleanField(default=False)
    favorite = IntegerField(default=0)
    # id3tag = ForeignKeyField(ID3Tag, related_name='id3tag')


class VideoFile(CommonFile):
    seen = BooleanField(default=False)
    favorite = IntegerField(default=0)


class ImageFile(CommonFile):
    pass


class DocumentFile(CommonFile):
    pass
