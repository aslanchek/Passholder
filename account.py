import json
import gnupg
from datetime import datetime

class OverwriteError(Exception):
    pass

class AccountNotExists(Exception):
    pass

class BadPassphrase(Exception):
    pass

class DB:
    def __init__(self, filename):
        self.filename = filename
        self.gpg = gnupg.GPG()
        self.gpg.encoding = "utf-8"
        self.db = {}

    def load(self, passphrase):
        try:
            with open(self.filename, "r") as f: 
                encrypted_data = f.read()
                data = self.gpg.decrypt(encrypted_data, passphrase=passphrase)
                if data.ok:
                    if data:
                        self.db = json.loads(data)
                    else:
                        self.db = {}
                else:
                    raise BadPassphrase("The passphrase didn't fit")
        except FileNotFoundError:
            self.db = {}
    
    def dump(self, passphrase):
        with open(self.filename, "w") as f:
            data = str(json.dumps(self.db, indent=2))
            encrypted_data = str(self.gpg.encrypt(data, [], symmetric=True, passphrase=passphrase))
            f.write(encrypted_data)

    def insert(self, site, login, password):
        if site in self.db:
            raise OverwriteError(f"Account on {site} exists. Last modified {self.db[site]['date']}")
        else:
            self.db[site] = { "login": login, "password": password, "date": datetime.now().strftime("%d/%m/%Y %H:%M") }

    def update(self, site, login, password):
        self.db[site] = { "login": login, "password": password, "date": datetime.now().strftime("%d/%m/%Y %H:%M") }
    
    def delete(self, site):
        if site in self.db:
            del self.db[site]
        else:
            raise AccountNotExists("Account does not exists")

    def __getitem__(self, site): # Usage: db['vk.com']
        if site in self.db:
            return self.db[site]
        else:
            raise AccountNotExists("Account does not exists")

    def __setitem__(self, site, value): # Usage: db['vk.com'] = { 'login': 'login', 'password': 'password' }
       self.insert(site, value['login'], value['password'])

    def __delitem__(self, site): # Usage: del db['vk.com']
        self.delete(site) 

def main():
    db = DB('storage')

    db.load(input("enter passphrase >> "))
    
    print(db["vk.com"])

    db.dump(input("enter passphrase >> "))

main()

#
#if site in self.db:
#            print(f"Account on {site} exists. Last modified {self.db[site]['date']}")
#            if input("Do you want to overwrite? [Y/n] ").lower() == "y":
#                self.db[site] = { "login": login, "password": password, "date": datetime.now().strftime("%d/%m/%Y %H:%M") }
#        else:
#            self.db[site] = { "login": login, "password": password, "date": datetime.now().strftime("%d/%m/%Y %H:%M") }
#            print(self.db)
#
