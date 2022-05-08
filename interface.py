
class Terminal:
    def __init__(self):
        pass

    def request(self, issue):
        return input(issue + ">> ")

    def choice(self, issue):
        check = input(issue + "[Y/n] ")
        if check.lower() = "y":
            return True
        else:
            return False

    def checkbox(self, issue, options, count):
        '''
        issue - str object
        options - array of str
        count - int
        '''
        for i in range(0, count):
            print(issue)
            print(f"{i+1}) {options[i]}")
        return input(">> ")

    def alert(self, issue):
        print("A:" + issue) 

    def error(self, issue):
        print("E:" + issue)
