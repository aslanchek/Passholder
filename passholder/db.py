import json
import gnupg
import os
from datetime import datetime
from passholder.errors import *

class DB:
    def __init__(self, filename="storage", new=False):
        if not(new or os.path.isfile(filename)):
            raise FileNotFoundError("Mentioned file does not exist.")
        self.filename = filename
        self.__gpg = gnupg.GPG()
        self.__gpg.encoding = "utf-8"
        self.__db = {}
        self.opened = False

    def newdb(self, passphrase):
        with open(self.filename, "w") as f:
            encrypted_data = str(self.__gpg.encrypt("{}", [], symmetric=True,
                                                    passphrase=passphrase))
            f.write(encrypted_data)

    def load(self, passphrase=None):
        with open(self.filename, "r") as f:
            if self.__gpg.is_valid_file(f):
                encrypted_data = f.read()
                data = self.__gpg.decrypt(encrypted_data,
                                          passphrase=passphrase)
                if data.status == "decryption ok":
                    if str(data):
                        self.__db = json.loads(str(data))
                    else:
                        self.__db = {}
                    self.opened = True
                elif data.status == "decryption failed":
                    raise DecryptionFailed("Something wrong with storage file")
                    #raise BadPassphrase("The passphrase didn't fit")
                elif data.status == "no data was provided":
                    raise FileNotFoundError("No encrypted data was provided")

    def dump(self, passphrase):
        with open(self.filename, "w") as f:
            data = str(json.dumps(self.__db, indent=2))
            encrypted_data = str(self.__gpg.encrypt(data, [], symmetric=True,
                                                    passphrase=passphrase))
            f.write(encrypted_data)

    def insert(self, site, login, password):
        if site in self.__db:
            raise OverwriteError(f"Account on {site} exists. Last modified \
                                 {self.__db[site]['date']}")
        else:
            self.__db[site] = { "login": login, "password": password,
                               "date": datetime.now().strftime("%d/%m/%Y %H:%M") }

    def update(self, site, login, password):
        if site in self.__db:
            self.__db[site] = { "login": login, "password": password,
                               "date": datetime.now().strftime("%d/%m/%Y %H:%M") }
        else:
            raise AccountNotExists("Account to update does not exists")

    def search(self, pattern):
        pass

    def delete(self, site):
        if site in self.__db:
            del self.__db[site]
        else:
            raise AccountNotExists("Account to delete does not exists")

    def __getitem__(self, site): # Usage: __db['vk.com']
        if site in self.__db:
            return self.__db[site]
        else:
            raise AccountNotExists("Account to get does not exists")

    def __setitem__(self, site, value): # Usage: __db['vk.com'] = { 'login': 'login', 'password': 'password' }
       self.insert(site, value['login'], value['password'])

    def __delitem__(self, site): # Usage: del __db['vk.com']
        self.delete(site)

