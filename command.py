#!/usr/bin/python3

"""Super program.

Usage:
  command.py db create
  command.py db drop
  command.py db export
  command.py dir list <path>
  command.py dir save <path>
  command.py ex boot
  command.py (-h | --help)
  command.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.


"""
from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version='Gerenciador de Arquivos - 0.1')

    if args['db']:
        if args['create']:
            from models import create_tables
            create_tables()

        if args['drop']:
            from models import drop_tables
            drop_tables()

        if args['export']:
            from models import export_data
            export_data()


    elif args['dir']:
        if args['list']:
            from dirs import dir_ls_tree
            dir_ls_tree(args['<path>'])


    elif args['ex']:
        if args['boot']:
            from init import boot
            boot()

    else:
        pass
