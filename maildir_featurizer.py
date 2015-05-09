import os, argparse, sys

p = argparse.ArgumentParser(description = 'Get simple email features very quickly.')
p.add_argument('maildir', nargs = '+', help = 'Maildir(s) to look at')

def messages(_):
    return [_]

def cli():
    for maildir in p.parse_args().maildir:
        for message in messages(maildir):
            print(message)

cli()
