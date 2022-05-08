from setuptools import setup, find_packages
from os.path import join, dirname

with open('requirements.txt') as fp:
    reqs = fp.read()

setup(
    name='passholder',
    version='0.0.1',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=reqs,
    entry_points={
        'console_scripts':
        ['passholder = passholder.controller:main']
    }
)
