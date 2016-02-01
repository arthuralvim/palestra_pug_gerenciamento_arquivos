# Makefile palestra_pug_arquivos

PIP=$(VIRTUAL_ENV)/bin/pip
PY=$(VIRTUAL_ENV)/bin/python

.PHONY: all help clean requirements test

all: help

help:
	@echo 'Makefile *** palestra_pug_arquivos *** Makefile'

# UTIL

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

requirements:
	@$(PIP) install -r requirements.txt

requirements.test:
	@$(PIP) install -r requirements/test.txt

# ---

# DATABASE

# db:

# db.delete:
#     @rm models.db

# db.reboot: db.delete db

# ---

# TESTS

test:
	@py.test

# ---
