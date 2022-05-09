from model.db import DB
from terminal_interface import Terminal
from os.path import exists

import errors
import json

def init_db():
    db = None

    if exists("storage"):
        tui.alert("Default storage exists")
        if tui.choice("Do you want to use this storage? "):
            resume = True
            while resume and not db:
                try:
                    db = DB.load(passphrase = tui.request("Enter password "))
                except errors.DecryptionFailed:
                    tui.error("Decryption failed")
                    if not tui.choice("Want to try again? "):
                        resume = False

            if db:
                return db

    else:
        tui.alert("Default storage not found")
        
    while not db:
        select = tui.select(["Create new storage", "Enter different filename", "Quit"])
        if select == 1:
            db = DB.create()
        elif select == 2:
            filename = tui.request("Enter filename ")
            
            if exists(filename):
                resume = True
                while resume and not db:
                    try:
                        db = DB.load(filename, tui.request("Enter password "))
                    except errors.DecryptionFailed:
                        tui.error("Decryptuon failed")
                        if not tui.choice("Want to try again? "):
                            resume = False
            else:
                tui.alert("Storage not found")

        else:
            exit(0)
    return db
        
        

tui = Terminal()

db = init_db()
    

