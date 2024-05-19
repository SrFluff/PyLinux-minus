import os

from colorama import Back, Fore

def cls():

    os.system('cls' if os.name == 'nt' else 'clear')

disset = 1

cls()

pwd = "/"

setup = 1

packages = [""]

arch = 1

root = ["user-files" , "pac" , "config" , "info"]

userfiles = ["Arch.txt" , "installs.txt"]

pac = ["system" , "user"]

pacsystem = ["pwd" , "ls" , "cd" , "pacman" , "help" , "clear" , "exit"]

pacuser = ["cat" , "whoami" , "PyFetch" , "echo" , "man" , "chname" , "chhost" , "license" , "credits" , "map"]

config = ["Arch.config"]

info = ["credits.txt" , "license.txt" , "version.txt"]

pacls = ["cat - reads a specified file" , "whoami - prints user information" , "PyFetch - a fetch script for PyLinux" , "echo - prints user input or file location" , "man - shows the PyLinux documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyLinux license" , "credits - prints the PyLinux credits" , "map - prints the filesystem map"]

custom = 0

cusset = 1

uset = 1

name = ""

host = ""

ls = root

usernamecustom = 0

hostnamecustom = 0

packagescustom = 0

pacpref = 0

pacprefselect = 0

init = 1

while init:

    while setup:

        cls()

        if disset == 1:
    
            print(Back.RESET + Fore.WHITE + "Please select an installation template\n" + Fore.RESET)

            print(Back.WHITE + Fore.BLACK + "[1] Full install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] Lite install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] Custom install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[4] Cancel install\n" + Back.RESET + Fore.RESET)

        if disset == 2:

            cls()

            print(Back.RESET + Fore.WHITE + "Please select an installation template\n" + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] Full install" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[2] Lite install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] Custom install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[4] Cancel install\n" + Back.RESET + Fore.RESET)

        if disset == 3:

            print(Back.RESET + Fore.WHITE + "Please select an installation template\n" + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] Full install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] Lite install" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[3] Custom install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[4] Cancel install\n" + Back.RESET + Fore.RESET)

        if disset == 4:

            print(Back.RESET + Fore.WHITE + "Please select an installation template\n" + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] Full install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] Lite install" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] Custom install" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[4] Cancel install\n" + Back.RESET + Fore.RESET)

        a = input("> ")

        if a == "1":

            disset = 1

        if a == "2":

            disset = 2

        if a == "3":

            disset = 3

        if a == "4":

            disset = 4

        if a == "":

            if disset == 1:

                cls()

                packages = ["pwd" , "ls" , "cd" , "cat" , "pacman" , "help" , "whoami" , "rm" , "rs" , "PyFetch" , "echo" , "man" , "chname" , "chhost" , "clear" , "license" , "credits" , "license" , "map" , "exit"]

                pacls = ["cat - reads a specified file" , "whoami - prints user information" , "PyFetch - a fetch script for PyLinux" , "echo - prints user input or file location" , "man - shows the PyLinux documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyLinux license" , "credits - prints the PyLinux credits" , "map - prints the filesystem map"]

                catinstalled = 1

                whoamiinstalled = 1

                pyfetchinstalled = 1

                echoinstalled = 1

                maninstalled = 1

                chnameinstalled = 1

                chhostinstalled = 1

                licenseinstalled = 1

                creditsinstalled = 1

                mapinstalled = 1
                
                name = "root"

                host = "PyArch"

                setup = 0

                init = 0

                custom = 0

                pacprefselect = 0

                usernamecustom = 0

                hostnamecustom = 0

                packagescustom = 0

                print("Type 'help' for a list of commands")

                arch = 1

            if disset == 2:

                packages = pacsystem

                pacls = ["cat - reads a specified file" , "whoami - prints user information" , "PyFetch - a fetch script for PyLinux" , "echo - prints user input or file location" , "man - shows the PyLinux documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyLinux license" , "credits - prints the PyLinux credits" , "map - prints the filesystem map"]

                setup = 0

                init = 0

                catinstalled = 0

                whoamiinstalled = 0

                pyfetchinstalled = 0

                echoinstalled = 0

                maninstalled = 0

                chnameinstalled = 0

                chhostinstalled = 0

                licenseinstalled = 0

                creditsinstalled = 0

                mapinstalled = 0

                cls()

                name = "root"

                host = "PyLinux"

                print("Type 'help' for a list of commands")

                arch = 1

            if disset == 3:

                cusset = 1
                
                packages = pacsystem

                pacls = ["cat - reads a specified file" , "whoami - prints user information" , "PyFetch - a fetch script for PyLinux" , "echo - prints user input or file location" , "man - shows the PyLinux documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyLinux license" , "credits - prints the PyLinux credits" , "map - prints the filesystem map"]

                setup = 0

                custom = 1
        
            if disset == 4:

                cls()

                quit()

    while custom:

        cls()

        if cusset == 1:

            print(Back.RESET + Fore.WHITE + "Please select a customization option\n" + Fore.RESET)

            print(Back.WHITE + Fore.BLACK + "[1] username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] packages" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[4] boot" + Fore.RESET + Back.RESET)
            print(Back.RESET + Fore.WHITE + "[5] go back\n" + Back.RESET + Fore.RESET)

        if cusset == 2:

            print(Back.RESET + Fore.WHITE + "Please select a customization option\n" + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] username" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[2] hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] packages" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[4] boot" + Fore.RESET + Back.RESET)
            print(Back.RESET + Fore.WHITE + "[5] go back\n" + Back.RESET + Fore.RESET)

        if cusset == 3:

            print(Back.RESET + Fore.WHITE + "Please select a customization option\n" + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] hostname" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[3] packages" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[4] boot" + Fore.RESET + Back.RESET)
            print(Back.RESET + Fore.WHITE + "[5] go back\n" + Back.RESET + Fore.RESET)

        if cusset == 4:

            print(Back.RESET + Fore.WHITE + "Please select a customization option\n" + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] packages" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[4] boot" + Fore.RESET + Back.RESET)
            print(Back.RESET + Fore.WHITE + "[5] go back\n" + Back.RESET + Fore.RESET)

        if cusset == 5:

            print(Back.RESET + Fore.WHITE + "Please select a customization option\n" + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] packages" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[4] boot" + Fore.RESET + Back.RESET)
            print(Back.WHITE + Fore.BLACK + "[5] go back\n" + Back.RESET + Fore.RESET)

        a = input("> ")

        if a == "1":

            cusset = 1

        if a == "2":

            cusset = 2

        if a == "3":

            cusset = 3

        if a == "4":

            cusset = 4

        if a == "5":

            cusset = 5

        if a == "":

            if cusset == 1:

                cusset = 1

                uset = 1

                custom = 0

                usernamecustom = 1

            if cusset == 2:

                cusset = 1

                uset = 1

                custom = 0

                hostnamecustom = 1

            if cusset == 3:

                custom = 0

                uset = 1

                uset = 1

                packagescustom = 1

            if cusset == 4:

                cls()

                if name == "" and host == "" and pacpref == 0:

                    print(Back.RESET + Fore.WHITE + "You have not set a username, hostname, or package preference. Press enter to go back.\n" + Back.RESET + Fore.RESET )

                    a = input("> ")

                    cls()

                    custom = 1

                if not name == "" and host == "" and pacpref == 0:

                    print(Back.RESET + Fore.WHITE + "You have not set a hostname, or package preference. Press enter to go back.\n" + Back.RESET + Fore.RESET )

                    a = input("> ")

                    cls()

                    custom = 1

                if not name == "" and not host == "" and pacpref == 0:

                    print(Back.RESET + Fore.WHITE + "You have not set a package preference. Press enter to go back.\n" + Back.RESET + Fore.RESET )

                    a = input("> ")

                    cls()

                    custom = 1

                if not name == "" and host == "" and not pacpref == 0:

                    print(Back.RESET + Fore.WHITE + "You have not set a hostname. Press enter to go back.\n" + Back.RESET + Fore.RESET )

                    a = input("> ")

                    cls()

                    custom = 1

                if name == "" and not host == "" and pacpref == 0:

                    print(Back.RESET + Fore.WHITE + "You have not set a username, or package preference. Press enter to go back.\n" + Back.RESET + Fore.RESET )

                    a = input("> ")

                    cls()

                    custom = 1

                if name == "" and not host == "" and not pacpref == 0:

                    print(Back.RESET + Fore.WHITE + "You have not set a username. Press enter to go back.\n" + Back.RESET + Fore.RESET )

                    a = input("> ")

                    cls()

                    custom = 1

                if name == "" and host == "" and not pacpref == 0:

                    print(Back.RESET + Fore.WHITE + "You have not set a username, or hostname. Press enter to go back.\n" + Back.RESET + Fore.RESET )

                    a = input("> ")

                    cls()

                    custom = 1

                if not name == "" and not host == "" and not pacpref == 0:

                    cls()

                    custom = 0

                    init = 0

                    arch = 1

                    print(Back.RESET + Fore.WHITE + "Type 'help' for a list of commands")

            if cusset == 5:

                custom = 0

                disset = 1

                setup = 1

                arch = 0

    while usernamecustom:

        cls()

        if uset == 1:

            print(Back.RESET + Fore.WHITE + "Username customization\n" + Back.RESET + Fore.RESET)

            print(Back.WHITE + Fore.BLACK + "[1] set a new username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] show username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] go back\n" + Back.RESET + Fore.RESET)

        if uset == 2:

            print(Back.RESET + Fore.WHITE + "Username customization\n" + Back.RESET + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] set a new username" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[2] show username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] go back\n" + Back.RESET + Fore.RESET)

        if uset == 3:

            print(Back.RESET + Fore.WHITE + "Username customization\n" + Back.RESET + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] set a new username" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] show username" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[3] go back\n" + Back.RESET + Fore.RESET)

        a = input("> ")

        if a == "1":

            uset = 1
                
        if a == "2":

            uset = 2

        if a == "3":

            uset = 3

        if a == "":

            if uset == 1:

                uset = 1
                
                cls()

                print(Back.RESET + Fore.WHITE + "Username customization\n" + Back.RESET + Fore.RESET)

                print(Back.RESET+ Fore.WHITE + "Type a username\n" + Back.RESET + Fore.RESET)

                name = input("Username: ")

                cls()

                usernamecustom = 1

            if uset == 2:

                uset = 1

                cls()

                if not name == "":

                    cls()

                    print(Back.RESET + Fore.WHITE + "Username customization\n" + Back.RESET + Fore.RESET)

                    print(Back.RESET+ Fore.WHITE + "Your username is set to '" + name + "'. Press enter to go back.\n" + Back.RESET + Fore.RESET)

                    a = input("> ")

                    cls()
                    
                    usernamecustom = 1

                else:

                    cls()
                    
                    print(Back.RESET + Fore.WHITE + "Username customization\n" + Back.RESET + Fore.RESET)

                    print(Back.RESET+ Fore.WHITE + "You have not set a username. Press enter to go back.\n" + Back.RESET + Fore.RESET)

                    a = input("> ")

                    cls()

                    usernamecustom = 1
            
            if uset == 3:

                uset = 1
                
                usernamecustom = 0

                custom = 1

                arch = 0

    while hostnamecustom:

        cls()

        if uset == 1:

            print(Back.RESET + Fore.WHITE + "Hostname customization\n" + Back.RESET + Fore.RESET)

            print(Back.WHITE + Fore.BLACK + "[1] set a new hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] show hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] go back\n" + Back.RESET + Fore.RESET)

        if uset == 2:

            print(Back.RESET + Fore.WHITE + "Hostname customization\n" + Back.RESET + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] set a new hostname" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[2] show hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] go back\n" + Back.RESET + Fore.RESET)

        if uset == 3:

            print(Back.RESET + Fore.WHITE + "Hostname customization\n" + Back.RESET + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] set a new hostname" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] show hostname" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[3] go back\n" + Back.RESET + Fore.RESET)
        
        a = input("> ")

        if a == "1":

            uset = 1

        if a == "2":

            uset = 2

        if a == "3":

            uset = 3

        if a == "":

            if uset == 1:

                cls()

                print(Back.RESET + Fore.WHITE + "Hostname customization\n" + Back.RESET + Fore.RESET)

                print(Back.RESET + Fore.WHITE + "Please type a new hostname\n" + Back.RESET + Fore.RESET)

                host = input("Hostname: ")

                cls()

                hostnamecustom = 1

            if uset == 2:

                cls()

                if not host == "":

                    cls()

                    print(Back.RESET + Fore.WHITE + "Hostname customization\n" + Back.RESET + Fore.RESET)

                    print(Back.RESET + Fore.WHITE + "Your hostname is currently set to '" + host + "'. Press enter to go back.\n" + Back.RESET + Fore.RESET)
                
                    a = input("> ")

                    cls()

                    hostnamecustom = 1

                else:

                    cls()

                    print(Back.RESET + Fore.WHITE + "Hostname customization\n" + Back.RESET + Fore.RESET)

                    print(Back.RESET + Fore.WHITE + "You have not set a hostname. Press enter to go back.\n" + Back.RESET + Fore.RESET)

                    a = input("> ")

                    cls()

                    hostnamecustom = 1

            if uset == 3:

                cls()

                hostnamecustom = 0

                custom = 1

    while packagescustom:

        cls()

        if uset == 1:

            print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

            print(Back.WHITE + Fore.BLACK + "[1] choose a pac preference" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] show pac preference" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] go back\n" + Back.RESET + Fore.RESET)

        if uset == 2:

            print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] choose a pac preference" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[2] show pac preference" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[3] go back\n" + Back.RESET + Fore.RESET)

        if uset == 3:

            print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] choose a pac preference" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] show pac preference" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[3] go back\n" + Back.RESET + Fore.RESET)
        
        a = input("> ")

        if a == "1":

            uset = 1

        if a == "2":

            uset = 2

        if a == "3":

            uset = 3

        if a == "":

            if uset == 1:

                uset = 1

                packagescustom = 0

                pacprefselect = 1

            if uset == 2:

                uset == 1

                cls()
            
                if pacpref == 0:
                    
                    print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

                    print(Back.RESET + Fore.WHITE + "You have not set any package preferences. Press enter to go back.\n" + Back.RESET + Fore.RESET)

                    a = input("> ")

                    cls()

                    packagescustom = 1

                if pacpref == 1:
                    
                    print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

                    print(Back.RESET + Fore.WHITE + "You have selected system packages only. Press enter to go back.\n" + Back.RESET + Fore.RESET)

                    a = input("> ")

                    cls()

                    packagescustom = 1

                if pacpref == 2:
                    
                    print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

                    print(Back.RESET + Fore.WHITE + "You have sellected a full package install. Press enter to go back.\n" + Back.RESET + Fore.RESET)

                    a = input("> ")

                    cls()

                    packagescustom = 1

            if uset == 3:

                uset = 1
                
                cls()

                packagescustom = 0

                custom = 1

    while pacprefselect:

        cls()

        if uset == 1:
                
            print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

            print(Back.WHITE + Fore.BLACK + "[1] system packages only" + Back.RESET + Fore.RESET)
            print(Back.RESET + Fore.WHITE + "[2] all available packages\n" + Back.RESET + Fore.RESET)

        if uset == 2:
                
            print(Back.RESET + Fore.WHITE + "Package customization\n" + Back.RESET + Fore.RESET)

            print(Back.RESET + Fore.WHITE + "[1] system packages only" + Back.RESET + Fore.RESET)
            print(Back.WHITE + Fore.BLACK + "[2] all available packages\n" + Back.RESET + Fore.RESET)

        a = input("> ")

        if a == "1":

            uset = 1

        if a == "2":

            uset = 2

        if a == "":

            if uset == 1:

                cls()

                packages = pacsystem

                pacls = ["cat" , "whoami" , "rm" , "rs" , "PyFetch" , "echo" , "man" , "chname" , "chhost" , "license" , "credits" , "map" , "pacls"]
                
                pacuser = []

                pacprefselect = 0

                packagescustom = 1

                catinstalled = 1

                whoamiinstalled = 1

                pyfetchinstalled = 1

                echoinstalled = 1

                maninstalled = 1

                chnameinstalled = 1

                chhostinstalled = 1

                licenseinstalled = 1

                creditsinstalled = 1

                mapinstalled = 1
                
                pacpref = 1

            if uset == 2:

                pacls = []
                
                packages = ["pwd" , "ls" , "cd" , "pacman" , "help" , "clear" , "exit" , "cat" , "whoami" , "rm" , "rs" , "PyFetch" , "echo" , "man" , "chname" , "chhost" , "license" , "credits" , "map" , "pacls"]

                pacsystem = ["pwd" , "ls" , "cd" , "pacman" , "help" , "clear" , "exit"]

                pacuser = ["cat" , "whoami" , "rm" , "rs" , "PyFetch" , "echo" , "man" , "chname" , "chhost" , "license" , "credits" , "map" , "pacls"]

                pacprefselect = 0

                packagescustom = 1

                uset = 1

                catinstalled = 0

                whoamiinstalled = 0

                pyfetchinstalled = 0

                echoinstalled = 0

                maninstalled = 0

                chnameinstalled = 0

                chhostinstalled = 0

                licenseinstalled = 0

                creditsinstalled = 0

                mapinstalled = 0
                
                pacpref = 2

    while arch:

        a = input(Back.RESET + Fore.GREEN + name + "@" + host + Fore.WHITE + ":" + Fore.RESET   + Fore.BLUE + pwd + Fore.RESET + "$ " + Back.RESET + Fore.RESET)

        if a == "pwd":

            print(Back.RESET + Fore.WHITE + pwd + Back.RESET + Fore.RESET)

        if a == "help":

            print(Back.RESET + Fore.WHITE + "help - prints this help message" + Back.RESET + Fore.WHITE)
            print(Back.RESET + Fore.WHITE + "pwd - prints the current working directory" + Back.RESET + Fore.WHITE)
            print(Back.RESET + Fore.WHITE + "ls - lists the contents of the current directory" + Back.RESET + Fore.WHITE)
            print(Back.RESET + Fore.WHITE + "cd - change the directory to a specified one" + Back.RESET + Fore.WHITE)
            print(Back.RESET + Fore.WHITE + "pacman - install a specified package" + Back.RESET + Fore.WHITE)
            print(Back.RESET + Fore.WHITE + "pacls - prints a list to packages" + Back.RESET + Fore.WHITE)
            print(Back.RESET + Fore.WHITE + "clear - clears the screen" + Back.RESET + Fore.WHITE)
            print(Back.RESET + Fore.WHITE + "exit - exit PyLinux" + Back.RESET + Fore.WHITE)

        if a == "pacls":

            print(Back.RESET + Fore.WHITE + '\n'.join(pacls) + Back.RESET + Fore.RESET)

        if a == "ls":

            print(Back.RESET + Fore.WHITE + '   '.join(ls) + Back.RESET + Fore.RESET)

        if a == "exit":

            cls()

            quit()

        if a == "clear":

            cls()