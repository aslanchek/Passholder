from typing import List

class Terminal:
    def __init__(self, prompt = ">> "):
        self.prompt = prompt

    def request(self, issue):
        return input(issue + self.prompt)

    def choice(self, issue):
        while True:
            check = input(issue + "[y/n] ")
            if check.lower() == "y":
                return True
            elif check.lower() == "n":
                return False

            print("Please enter one letter ('y' or 'n')")            

    def select(self, issue: str, options: List[str]):
        '''issue - str object, options - array of str'''
        if issue:
            print("C:" + issue)
        for i in range(0, len(options)):
            print(f"{i+1}) {options[i]}")
        return input(self.prompt)

    def alert(self, issue):
        print("A:" + issue)

    def error(self, issue):
        print("E:" + issue)

    def account_format(self, account):
        return f"{account['login']} : {account['password']}"
