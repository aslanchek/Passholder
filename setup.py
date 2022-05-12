from setuptools import setup, find_packages

reqs = [
    'getpass-asterisk==1.0.0',
    'python-gnupg==0.4.8',
]

setup(
    name='passholder',
    version='0.1.4',
    license='GPL-3.0',
    description = 'Password manager',
    url = 'https://github.com/aslanchek/Passholder',
    download_url = 'https://github.com/aslanchek/Passholder/archive/refs/tags/v0.1.4-alpha.tar.gz',
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
