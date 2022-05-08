import db
import interface
from errors import *

def main():
    term = interface.Terminal()
    storage = db.DB(term.request("enter the storage filename(default=storage)"))    
    
    while not storage.opened:
        try:
            storage.load(term.request("enter the passphrase")) 
        except DecryptionFailed:
            term.error("decryption failed")
            if term.choice("want to create new storage?"):
                new_filename = term.request("enter another filename to prevent overwrite(keep empty to overwrite)")
                if new_filename:
                    storage.filename = new_filename
                    storage.newdb(term.request("enter the passphrase for new storage"))
                else:
                    storage.newdb(term.request("enter the passphrase for new storage"))
                    
        except FileNotFoundError:
            term.error("no encrypted data was provided")
            if term.choice("want to create new storage?"):
                storage.newdb(term.request("enter the passphrase for new storage"))
                term.alert("new storage created!")
                storage.opened = True
    
        except JSONDecodeError:
            term.error("json parsing error")
            if term.choice("want to create new storage?"):
                new_filename = term.request("enter another filename to prevent overwrite(keep empty to overwrite)")
                if new_filename:
                    storage.filename = new_filename
                    storage.newdb(term.request("enter the passphrase for new storage"))
                    storage.opened = True
                else:
                    storage.newdb(term.request("enter the passphrase for new storage"))     
                    storage.opened = True

    term.alert("storage opened!")
    running = True

    while running:
        check = term.checkbox("select the option", ["search account", "add account", "delete account", "exit"])
        if check == "1":
            term.alert(term.account_format(storage[term.request("enter account website")]))
        elif check == "4":
            i_check = term.checkbox("exit", ["exit and save", "exit without saving", "cancel"])
            if i_check == "1":
                storage.dump(term.request("enter the closing passphrase for the storage"))
                running = False
                break
            elif i_check == "2":
                term.alert("closing without saving")
                running = False
                break
            elif i_check == "3":
                term.alert("cancel")

            
            
            
main()

