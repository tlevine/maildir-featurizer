import pathlib, argparse, sys

p = argparse.ArgumentParser(description = 'Get simple email features very quickly.')
p.add_argument('maildir', nargs = '+', help = 'Maildir(s) to look at')

def features(p):
    '''
    :param pathlib.Path p: An email file
    '''
    return {
        'date': datetime.datetime.fromtimestamp(int(p.name.split('_')[0])),
    }

def messages(maildir):
    parent = pathlib.Path(maildir)
    for child in parent.iterdir():
        if child.is_file():
            pass
        elif child.name in {'new', 'cur', 'tmp'}:
            for grandchild in child.iterdir():
                if grandchild.is_file():
                    yield features(grandchild)
        else:
            yield from messages(child)

def cli():
    for maildir in p.parse_args().maildir:
        for message in messages(maildir):
            print(message)

cli()
