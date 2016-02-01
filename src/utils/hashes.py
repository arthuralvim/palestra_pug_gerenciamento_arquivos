# -*- coding: utf-8 -*-

from decouple import config
from .folder import makedir
import os
import subprocess
import hashlib


class BaseMD5(object):

    md5_extra_path = config('MD5_EXTRA_PATH', default='.md5')
    md5_cmd = 'md5'

    def __init__(self, _file):
        self._file = _file

    @property
    def file_path(self):
        return self._file.dirname

    @property
    def file_name(self):
        return self._file.basename

    @property
    def file_full_path(self):
        return self._file.strpath

    @property
    def md5_path(self):
        return os.path.join(self.file_path, self.md5_extra_path)

    @property
    def md5_full_path(self):
        return os.path.join(self.md5_path, self.file_name)


class UnixMD5(BaseMD5):

    def get_command_args(self):
        return [self.md5_cmd, self.file_full_path]

    def run_command(self):
        return subprocess.check_output(self.get_command_args(),
                                       cwd=self.file_path)

    def get_md5(self, md5_output):
        return md5_output.strip().split(' ')[-1]

    def run(self, save=False):
        run_cmd = self.run_command()
        md5 = self.get_md5(run_cmd)

        if save:
            makedir(self.md5_path)
            with open(self.md5_full_path, 'w') as f:
                f.write(md5.encode('utf-8'))


class HashMD5(BaseMD5):

    def run_command(self):
        md5 = hashlib.md5()
        with open(self.file_full_path, "rb") as fi:
            for chunk in iter(lambda: fi.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()

    def run(self, save=False):
        md5 = self.run_command()

        if save:
            makedir(self.md5_path)
            with open(self.md5_full_path, 'w') as f:
                f.write(md5.encode('utf-8'))
