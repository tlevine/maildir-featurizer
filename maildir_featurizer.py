import os, argparse, sys

p = argparse.ArgumentParser(description = 'Get simple email features very quickly.')
p.add_argument('maildir', nargs = '+', help = 'Maildir(s) to look at')

def cli():
    print(p.parse_args().maildir)

cli()
