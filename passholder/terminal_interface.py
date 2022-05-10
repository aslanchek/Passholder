from typing import List
from getpass_asterisk.getpass_asterisk import getpass_asterisk

class Terminal:
    def __init__(self, prompt = ">> "):
        self.prompt = prompt

    def request(self, issue):
        return input(issue + self.prompt)

    def request_password(self, issue):
        return getpass_asterisk(issue + self.prompt)

    def choice(self, issue):
        while True:
            check = input(issue + "[y/n] ")
            if check.lower() == "y":
                return True
            elif check.lower() == "n":
                return False

            print("Please enter one letter ('y' or 'n')")            

    def select(self, options: List[str], issue = ""):
        if issue:
            print("C: " + issue)

        for i in range(0, len(options)):
            print("{number}: {option}".format(number=i + 1, option = options[i]))

        while True:
            try:
                selection = int(input(self.prompt))
            except ValueError:
                print("Please, enter a number")                
            else:
                if 1 <= selection <= len(options):
                    return selection
                
                print("Enter a number, from list above")
        
    def alert(self, issue):
        print("A: " + issue)

    def error(self, issue):
        print("E: " + issue)

    def account_format(self, account):
        return "{login}: {password}".format(*account)


