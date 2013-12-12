import os
from collections import Counter


def action_startswith(filter, file=None):
    file = os.path.basename(file)
    if file.startswith(filter):
        return True


def action_endswith(filter, file=None):
    file = os.path.basename(file)
    if file.endswith(filter):
        return True


def action_check_file(file=None, **kwargs):
    if os.path.isfile(file):
        return True


def action_check_link(file=None, **kwargs):
    if os.path.islink(file):
        return True


def list_files(startpath, action, filter=None, reverse=False, limit=None):
    fs = []
    for root, dirs, files in os.walk(startpath):

        for f in files:
            fileabspath = os.path.join(os.path.abspath(root), f)
            if action(filter=filter, file=fileabspath):
                fs.append(fileabspath)
                # print(fileabspath)

    if reverse:
        fls = sorted(fs, reverse=True)
    else:
        fls = sorted(fs, reverse=False)

    if limit:
        for f in fls[:limit]:
            print('{}'.format(f))
    else:
        for f in fls:
            print('{}'.format(f))


def dir_ls_tree(startpath, indent_char=' ', subindent_char=' '):
    for root, dirs, files in os.walk(startpath):
        # indentacao
        level = root.replace(startpath, '').count(os.sep)
        indent = indent_char * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        # subindentacao
        subindent = subindent_char * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))


def dir_list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        for f in files:
            print(os.path.join(os.path.abspath(root), f))


def dir_list_folders(startpath):
    for root, dirs, files in os.walk(startpath):
        print(os.path.abspath(root))


def dir_list_folders_empty(startpath):
    for root, dirs, files in os.walk(startpath):
        if not os.listdir(root):
            print(os.path.abspath(root))


def dir_filter_files(startpath, filter):
    for root, dirs, files in os.walk(startpath):
        files
        print(os.path.abspath(root))


def dir_list_extensions(path, reverse=False, limit=None):

    fexts = []
    for root, dirs, files in os.walk(path):
        exts = [os.path.splitext(f)[1] for f in files]
        fexts.extend(exts)

    exts = Counter(fexts)

    if reverse:
        exts = sorted(exts.items(), key=lambda x: (-x[1], x[0]), reverse=True)
    else:
        exts = sorted(exts.items(), key=lambda x: (-x[1], x[0]), reverse=False)

    if limit:
        for ext, count in exts[:limit]:
            print('{}:{}'.format(ext, str(count)))
    else:
        for ext, count in exts:
            print('{}:{}'.format(ext, str(count)))





#node class
# class node:
#   path = ""
#   depth = ""
#   dirs = []
#   files = []

#   def __init__(self,path,depth,dirs,files):
#     self.path = path
#     self.depth = depth
#     self.dirs = dirs
#     self.files = files


# #returns array of node objects for a given path
# def parse(path):

#   dir_list = []
#   startinglevel = path.count(os.sep)

#   for path, dirs, files in os.walk(path):
#     depth = path.count(os.sep) - startinglevel
#     Node = node(path,depth,dirs,files)
#     dir_list.append(Node)

#   return dir_list
# #-----------------------------------Main---------------------------------------
# if __name__ == "__main__":
#   nodes = parse(top)

#   i = 0
#   for node in nodes:
#     print "path:", node.path
#     print "depth:",node.depth
#     print "dirs:",node.dirs
#     print "files:",node.files
#     i += 1
#     if(i >= 4):
#       break
