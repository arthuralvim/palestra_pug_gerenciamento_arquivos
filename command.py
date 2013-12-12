#!/usr/bin/python3

"""Super program.

Usage:
  command.py db (create|drop|export)
  command.py dir (tree|list|listf|liste|save) <PATH>
  command.py dir ext <PATH> [--reverse] [--limit=LIMIT]
  command.py filter (file|link) <PATH> [--reverse] [--limit=LIMIT]
  command.py filter (start|end|file|link) <PATH> <FILTER>
  command.py mp3 (tags|export) <PATH> [--reverse] [--limit=LIMIT]
  command.py boot
  command.py (-h | --help)
  command.py (-v | --version)

Options:
    -r, --reverse                   Show dir options in reverse.
    -l LIMIT --limit=LIMIT         Limit the numbers of elements displayed.
    -o FILE --output=FILE      Output file [default: result.txt]
    -h, --help                      Show this screen.
    -v, --version                   Show version


"""
from docopt import docopt
from os.path import exists
from schema import And
from schema import Or
from schema import Schema
from schema import SchemaError
from schema import Use

check = lambda check: check in ['true', 'True', '1', 'y', 'yes',]

if __name__ == '__main__':
    args = docopt(__doc__, version='Gerenciador de Arquivos - 0.1')

    schema = Schema({
                # Optional('FILE'): Use(open,
                #     error='FILE should be readable'),
                '<PATH>': Or(None, And(exists), error='PATH should exist'),
                '<FILTER>': And(Use(str), error='PATH should exist'),
                '--limit': Or(None, And(Use(int), lambda n: n > 0), error='--limit=LIMIT should be integer N > 0 > total number files'),

                # options
                '--help': bool,
                '--reverse': bool,
                '--version': bool,
                'boot': bool,
                'create': bool,
                'db': bool,
                'dir': bool,
                'drop': bool,
                'end': bool,
                'export': bool,
                'ext': bool,
                'file': bool,
                'filter': bool,
                'link': bool,
                'list': bool,
                'liste': bool,
                'listf': bool,
                'mp3': bool,
                'save': bool,
                'start': bool,
                'tags': bool,
                'tree': bool,
                })
    try:
        args = schema.validate(args)
    except SchemaError as e:
        exit(e)

    # functions
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
        if args['tree']:
            from dirs import dir_ls_tree
            dir_ls_tree(args['<PATH>'])

        if args['list']:
            from dirs import dir_list_files
            dir_list_files(args['<PATH>'])

        if args['listf']:
            from dirs import dir_list_folders
            dir_list_folders(args['<PATH>'])

        if args['liste']:
            from dirs import dir_list_folders_empty
            dir_list_folders_empty(args['<PATH>'])

        if args['ext']:
            from dirs import dir_list_extensions

            if args['--limit']:
                dir_list_extensions(args['<PATH>'], args['--reverse'], args['--limit'])
            else:
                dir_list_extensions(args['<PATH>'], args['--reverse'])

    elif args['filter']:
        if args['start']:
            from dirs import list_files
            from dirs import action_startswith

            if args['--limit']:
                list_files(args['<PATH>'], action_startswith, args['<FILTER>'], args['--reverse'], args['--limit'])
            else:
                list_files(args['<PATH>'], action_startswith, args['<FILTER>'], args['--reverse'])

        if args['end']:
            from dirs import list_files
            from dirs import action_endswith

            if args['--limit']:
                list_files(args['<PATH>'], action_endswith, args['<FILTER>'], args['--reverse'], args['--limit'])
            else:
                list_files(args['<PATH>'], action_endswith, args['<FILTER>'], args['--reverse'])

        if args['link']:
            from dirs import list_files
            from dirs import action_check_link


            if args['--limit']:
                list_files(args['<PATH>'], action_check_link, reverse=args['--reverse'], limit=args['--limit'])
            else:
                list_files(args['<PATH>'], action_check_link, reverse=args['--reverse'])

        if args['file']:
            from dirs import list_files
            from dirs import action_check_file

            if args['--limit']:
                list_files(args['<PATH>'], action_check_file, reverse=args['--reverse'], limit=args['--limit'])
            else:
                list_files(args['<PATH>'], action_check_file, reverse=args['--reverse'])


    elif args['mp3']:
        if args['tags']:
            from mp3 import list_mp3
            from mp3 import action_mp3

            if args['--limit']:
                list_mp3(args['<PATH>'], action_mp3, args['--reverse'], args['--limit'])
            else:
                list_mp3(args['<PATH>'], action_mp3, args['--reverse'])


    elif args['boot']:
        from init import boot
        boot()
