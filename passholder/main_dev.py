import controller_dev as controller
import terminal_interface

interface = terminal_interface.Terminal()
controller = controller.Сontroller(interface)

DEFAULT_FILENAME = "storage"

def main():
    if controller.storage_exists(filename = DEFAULT_FILENAME):
        interface.alert("default storage filename exists")
        if interface.choice("do you want to use this storage?"):
            controller.open_storage(DEFAULT_FILENAME, interface.request("enter storage password"))
        else:
            controller.create_storage(filename = interface.request("enter storage filename"))

    else:
        interface.alert("storage file not found")
        check = interface.select("select the option:", ["enter another filename", "create new storage"])
        if check == "1":
            filename_tmp = interface.request("enter another storage filename")
            if controller.storage_exists(filename=filename_tmp):
                passphrase_tmp = interface.request("enter storage password") 
                controller.open_storage(filename_tmp, passphrase_tmp)
        ######################################
        elif check == "2":
            controller.create_storage(interface.request("enter new storage filename"))
        elif check == "3":
            interface.alert("closing...")
            exit()


    

if __name__ == "__main__":
    main()
