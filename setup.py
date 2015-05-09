from setuptools import setup, find_packages

setup(
    name = 'maildir-featurizer',
    version = '0.1',
    description = 'Quickly featurize a maildir',
    author = 'Thomas Levine',
    author_email = '_@thomaslevine.com',
    url = 'https://thomaslevine.com',
    entry_points = {'console_scripts': ['maildir-featurier = maildir_featurizer:cli']},
    license = 'AGPL',
    packages = ['maildir_featurizer'],
    classifiers=[
        'Programming Language :: Python :: 3.4',
    ],
)
