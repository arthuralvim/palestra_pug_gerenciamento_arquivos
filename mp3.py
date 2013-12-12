import os
from mutagenx.easyid3 import EasyID3
from mutagenx.mp3 import MP3


def action_mp3(filter='.mp3', file=None):
    file = os.path.basename(file)
    if file.endswith(filter):
        return True


def list_mp3(startpath, action, reverse=False, limit=None):
    fs = []
    for root, dirs, files in os.walk(startpath):

        for f in files:
            fileabspath = os.path.join(os.path.abspath(root), f)
            if action(file=fileabspath):
                fs.append(fileabspath)
                import ipdb; ipdb.set_trace()
                mp3info = EasyID3(fileabspath)
                audio = MP3(fileabspath)
                print(fileabspath)
                print(mp3info.items())
                print('*'*40)


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
