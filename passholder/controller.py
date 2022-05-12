import json
from os.path import exists

from passholder import *

filename = "storage"


def init_db():
    db = None
    global filename

    if exists(filename):
        tui.alert("default storage exists")
        if tui.choice("do you want to use this storage?"):
            resume = True
            while resume and not db:
                try:
                    db = DB.load(passphrase=tui.request_password("enter passphrase"))
                except errors.DecryptionFailed:
                    tui.error("decryption failed")
                    if not tui.choice("want to try again?"):
                        resume = False
                except FileNotFoundError:
                    tui.error("no encrypted data was provided")
                    resume = False
                except json.decoder.JSONDecodeError:
                    tui.error("json parsing error")
                except IsADirectoryError:
                    tui.error("it is a directory, must be a gpg file")
                    resume = False
            if db:
                tui.alert("storage loaded")
                return db, filename

    else:
        tui.alert("default storage not found")

    while not db:
        select = tui.select(["create new storage", "enter another filename", "quit"])
        if select == 1:
            if not exists(filename):
                db = DB.create()
                tui.alert("new storage created")
            else:
                tui.alert(f'storage "{filename}" exists')
                if tui.choice("do you want to overwrite?"):
                    db = DB.create()
                    tui.alert("new storage created")
        elif select == 2:
            filename = tui.request("enter filename")
            if exists(filename):
                resume = True
                while resume and not db:
                    try:
                        db = DB.load(filename, tui.request_password("enter password"))
                    except errors.DecryptionFailed:
                        tui.error("decryptuon failed")
                        if not tui.choice("want to try again? "):
                            resume = False
            else:
                tui.alert("storage not found")

        else:
            exit(0)

    tui.alert("storage loaded")
    return db, filename


def add():
    try:
        db.insert(tui.request("site"), tui.request("login"), tui.request("password"))
        tui.alert("account added")
    except errors.OverwriteError:
        tui.error("such account exists")


def search():
    try:
        site = tui.request("site")
        tui.alert(f"account found\nlogin: {db[site]['login']} password: {db[site]['password']}")
    except errors.AccountDoesNotExist:
        tui.error(f"account for {site} not found")


def delete():
    try:
        db.delete(tui.request("site"))
        tui.alert("account deleted")
    except errors.AccountDoesNotExist:
        tui.error("such account does not exist")


def save():
    db.dump(filename, tui.request_password("enter passphrase", repeat=True))
    tui.alert("changes saved")

def main():
    pass

running = True
tui = Terminal()
try:
    db, filename = init_db()
    while running:
       select = tui.select(["add new", "delete", "search", "save", "exit"])
       if select == 1:
           add()
       elif select == 2:
           delete()
       elif select == 3:
           search()
       elif select == 4:
           save()
       elif select == 5:
           running = False
           tui.alert("closing")
except KeyboardInterrupt:
    tui.alert("\n<C-c>: abort")
except EOFError:
    tui.alert("\n<C-d>: abort")
   
