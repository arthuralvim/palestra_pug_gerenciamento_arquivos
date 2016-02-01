# -*- coding: utf-8 -*-

import os


def makedir(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
