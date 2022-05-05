#!/bin/python3
import json
import gnupg
from getpass import getpass
from os import system

#START_MESSAGE = "Passholder is a programm that allows you to write your passwords into encrypted file where you can securely store it."
#CHOICE_MESSAGE = "Select option(default = 1):\n1)Show passwords\n2)Add password\n"

#def show_passwords():
#    try:
#        with open("storage", "r") as f:
#            passwords = json.load(f)
#        for j in passwords:
#            print(f"{j} {passwords[j]['login']}: {passwords[j]['password']}")
#    except FileNotFoundError:
#        print("E: no passwords storage file detected.")

def search_account(site):
    try:
        with open("storage", "r") as f: # LOADING JSON FILE
            accounts = json.load(f)     # WITH ACCOUNTS
            accounts_found = []
            for i in accounts:
                if site in i:
                    accounts_found.append(i)
            if accounts_found:
                result = ""
                for j in accounts_found:
                    result += f"{j} {accounts[j]['login']}: {accounts[j]['password']}\n"
                return "Found accounts:\n" + result
            else:
                return "E: no such account was found"
    except FileNotFoundError:
        return "E: no passwords storage file detected."
        
def append_account(site, login, password):
    try:
        with open("storage", "r") as f:
            accounts = json.load(f) 
        accounts[site] = {"login": login, "password": password}
        with open("storage", "w") as f:
            json.dump(accounts, f, indent=2)
        print("account successifully added")
    except:
        with open("storage", "w") as f:
            accounts = {}
            accounts[site] = {"login": login, "password": password}
            json.dump(accounts, f, indent=2)
        print("account successifully added")
    
def delete_account(site):
    with open("storage", "r") as f: # LOADING JSON FILE
        accounts = json.load(f)     # WITH ACCOUNTS

    accounts_found = []
    for i in accounts:
        if site in i:
            accounts_found.append(i)

    if accounts_found:
        result = ""
        for j in accounts_found:
            result += f"{j} {accounts[j]['login']}\n"
        print("Found accounts:\n" + result)
        
        if len(accounts_found) > 1:
            print("\nselect account to delete")
            n = 1
            for account in accounts_found:
                print(f"{n}) {account}")
                n += 1
            del accounts[accounts_found[int(input("delete >>"))-1]]
            print("\nselected account successifully deleted")
        else:
            del accounts[accounts_found[0]]
            print("selected account successifully deleted")
            
        with open("storage", "w") as f:
            json.dump(accounts, f, indent=2)
    else:
        return "E: no such account was found"

 
    

def main():
    running = True
    while running:
        print("\nselect option:")
        print("\n1)search account\n2)append account\n3)delete account\n4)exit\n") 
        i = input(">>")
        try:
            if i == "1":
                print(search_account(input("site >>")))
            elif i == "2":
                try:
                    append_account(input("site >>"), input("login >>"), getpass(prompt="password >>", stream=None)
    )
                except KeyboardInterrupt:
                    print("\n\naborted")
            elif i == "3":
                delete_account(input("site >>"))
            elif i == "4":
                running = False
                system("clear")
            else:
                print("E: select the determined option only")
        except json.decoder.JSONDecodeError:
            print("E: passwords storage file is empty")
        except FileNotFoundError:
            print("E: no passwords storage file detected.")
     

if __name__ == "__main__":
    main()
