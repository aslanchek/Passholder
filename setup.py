from setuptools import setup, find_packages

reqs = [
    'caugetch==0.0.1',
    'clipboard==0.0.4',
    'colorama==0.4.4',
    'getpass4==0.0.14.1',
    'pyperclip==1.8.2',
    'python-gnupg==0.4.8',
]

setup(
    name='passholder',
    version='0.0.3',
    license='GPL-3.0',
    description = 'Password manager',
    url = 'https://github.com/aslanchek/Passholder',
    download_url = 'https://github.com/aslanchek/Passholder/archive/refs/tags/v0.0.3-alpha.tar.gz',
    packages=find_packages(),
    long_description='See github for long description.',
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
