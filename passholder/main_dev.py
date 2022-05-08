import controller_dev as controller
import terminal_interface

term = terminal_interface.Terminal()
controller = controller.Controller()

def main():
    if controller.storage_exists(filename = DEFAULT_FILENAME):
        term.alert("file storage exists")
        if term.choice("do you want to use this storage?"):
            controller.open_storage(filename = DEFAULT_FILENAME):
        else:
            controller.create_storage(filename = DEFAULT_FILENAME)
    else:
        term.alert("storage file not found")
        check = term.select("select the option:", ["enter another filename", "create new storage"])
        if check = "1":
            controller.open_storage(filename = term.request("enter storage filename"))
        elif check == "2":
            controller.create_storage(filename = term.request("enter new storage filename"))
        elif check == "3":
            term.alert("closing...")
            exit()


    

if __name__ == "__main__":
    main()
