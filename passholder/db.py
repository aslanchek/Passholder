import json
import gnupg
from datetime import datetime
from passholder.errors import *


class DB:
    def __init__(self, db, gpg):
        self.__gpg = gpg
        self.__db = db


    def dump(self, filename, passphrase):
        with open(filename, "w") as f:
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
            raise AccountDoesNotExist("Account to update does not exists")

    def search(self, pattern):
        pass

    def delete(self, site):
        if site in self.__db:
            del self.__db[site]
        else:
            raise AccountDoesNotExist("Account to delete does not exists")

    def __getitem__(self, site): # Usage: __db['vk.com']
        if site in self.__db:
            return self.__db[site]
        else:
            raise AccountDoesNotExist("Account to get does not exists")

    def __setitem__(self, site, value): # Usage: __db['vk.com'] = { 'login': 'login', 'password': 'password' }
       self.insert(site, value['login'], value['password'])

    def __delitem__(self, site): # Usage: del __db['vk.com']
        self.delete(site)


    @classmethod
    def create(cls):
        gpg = gnupg.GPG()
        gpg.encoding = "utf-8"

        db = {}

        return cls(db, gpg)

    @classmethod
    def load(cls, filename = "storage", passphrase = None):
        gpg = gnupg.GPG()
        gpg.encoding = "utf-8"
        db = {}
        with open(filename, "r") as f:
            encrypted_data = f.read()
            data = gpg.decrypt(encrypted_data,
                               passphrase=passphrase)

            if data.status == "decryption ok":
                if str(data):
                    db = json.loads(str(data))

            elif data.status == "decryption failed":
                raise DecryptionFailed("Something wrong with storage file")
            elif data.status == "no data was provided":
                raise FileNotFoundError("No encrypted data was provided")

        return cls(db, gpg)
