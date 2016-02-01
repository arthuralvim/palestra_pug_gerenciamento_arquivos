# -*- coding: utf-8 -*-

from src.utils import UnixMD5
from src.utils import HashMD5
import pytest


class TestCheckFileMD5(object):
    md5 = '0cc175b9c0f1b6a831c399e269772661'
    md5_output = 'MD5 (/some/path/to/md5_test.txt) = 0cc175b9c0f1b6a831c399e269772661'  # noqa

    def test_unix_md5(self, tmpdir):
        filename = 'md5_test.txt'
        file_path = tmpdir.join(filename)
        file_path.write("a")
        assert file_path.read() == "a"

        md5 = UnixMD5(file_path)
        md5.run()

        md5_path = tmpdir.join(".md5").join(filename)
        assert not md5_path.exists()

        md5.run(save=True)
        assert md5_path.exists()

        assert md5_path.read() == self.md5

        md5_output = md5.get_md5(self.md5_output)
        assert md5_output == self.md5

    def test_hash_md5(self, tmpdir):
        filename = 'md5_test.txt'
        file_path = tmpdir.join(filename)
        file_path.write("a")
        assert file_path.read() == "a"

        md5 = HashMD5(file_path)
        md5.run()

        md5_path = tmpdir.join(".md5").join(filename)
        assert not md5_path.exists()

        md5.run(save=True)
        assert md5_path.exists()

        assert md5_path.read() == self.md5
