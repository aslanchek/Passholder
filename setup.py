from setuptools import setup, find_packages
from os.path import join, dirname

with open('requirements.txt') as fp:
    reqs = fp.read()

setup(
    name='passholder',
    version='0.0.1',
    license='GPL-3.0',
    description = 'This software is needed for storage passwords \
                    in encrypted file.',
    url = 'https://github.com/aslanchek/Passholder',
    download_url = 'https://github.com/aslanchek/Passholder/archive/refs/tags/v0.0.1-alpha.tar.gz',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    install_requires=reqs,
    entry_points={
        'console_scripts':
        ['passholder = passholder.controller:main']
    },
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Database',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.8',
    ]
)
