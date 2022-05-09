import db
import json
import terminal_interface
import errors
from os.path import exists

DEFAULT_FILENAME = "storage"

class Сontroller:
    def __init__(self, interface):
        self.interface = interface
        self.storage = db.DB()

    def storage_exists(self, filename):
        return exists(filename)
        
        
    def create_storage(self, filename, passphrase):  
        self.storage.newdb(filename, passphrase) if filename else self.storage.newdb(passphrase)
        self.interface.alert("new storage created")

    def open_storage(self, filename, passphrase):
        while not self.storage.opened:
            try:
                self.storage.load(filename, passphrase)
            except errors.DecryptionFailed:
                self.interface.error("decryption failed")
                if self.interface.choice("want to try again?"):
                    continue
                else:
                    break
            except FileNotFoundError:
                self.interface.error("no data was provided")
                if self.interface.choice("want to create new storage?"):
                    filename_new = self.interface.request("enter the new storage filename")
                    passphrase_new = self.interface.request("enter the new storage passphrase")
                    self.create_storage(filename_new, passphrase_new)
                    self.open_storage(filename_new, passphrase_new)
                else:
                    break
            except json.decoder.JSONDecodeError:
                self.interface.error("json parsing error")
                if self.interface.choice("want to create new storage?"):
                    filename_new = self.interface.request("enter the new storage filename")
                    passphrase_new = self.interface.request("enter the new storage passphrase")
                    self.create_storage(filename_new, passphrase_new)
                    self.open_storage(filename_new, passphrase_new)
                else:
                    break

        if self.storage.opened:
            self.interface.alert("storage opened!")
        else:
            self.interface.alert("abort")
            
    def save_in_storage():
        pass

    def close_storage():
        try:
            pass
        except:
            pass

