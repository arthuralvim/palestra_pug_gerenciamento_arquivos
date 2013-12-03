import os
import random
import string


def gen_rnd_str(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in list(range(size)))


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(name='example', ext=''):
    with open('{}.{}'.format(name, ext), 'w', encoding='utf-8') as fle:
        fle.write(gen_rnd_str(300))


def create_hidden(name='example', ext=''):
    with open('.{}.{}'.format(name, ext), 'w', encoding='utf-8') as fle:
        fle.write(gen_rnd_str(300))


def create_symlink(source, destination):
    os.symlink(source, destination)



def boot(name_root='FOLDER_EXAMPLE', nfolder=20, nfiles=100, nlinks=10,
    nhidden=10, depth=10, seed=10):

    random.seed(seed)

    if not os.path.exists(name_root):

        create_dir(name_root)
        main_root = os.path.abspath(name_root)
        os.chdir(name_root)

        for d in list(range(nfolder)):
            create_dir(gen_rnd_str())

        dir_name = os.path.join(main_root, *[gen_rnd_str() for d in list(range(depth))])
        create_dir(dir_name)

        os.chdir(main_root)

        cntfil = 0
        cntlin = 0
        cnthid = 0

        while cntfil != nfiles or cntlin != nlinks or cnthid != nhidden:

            for root, dirs, files in os.walk('.'):

                threshold = random.random()
                os.chdir(root)
                print(root)
                if random.random() > threshold and cntfil != nfiles:
                    create_file(gen_rnd_str(), gen_rnd_str(size=3))
                    cntfil += 1
                    print('file: {}'.format(str(cntfil)))

                if random.random() > threshold and cnthid != nhidden:
                    create_hidden(gen_rnd_str(), gen_rnd_str(size=3))
                    cnthid += 1
                    print('hidden: {}'.format(str(cnthid)))

                if files:
                    if random.random() > threshold and cntlin != nlinks:

                        chosen = files[random.randint(1, len(files))-1]
                        if not os.path.islink(chosen):
                            create_symlink(chosen, gen_rnd_str(size=15))
                            cntlin += 1
                        print('link: {}'.format(str(cntlin)))

                os.chdir(main_root)

            create_dir('DELETE')
            create_dir('RESULTS')

        print('Exemplo criado.')

    else:

        print('Exemplo já criado.')

