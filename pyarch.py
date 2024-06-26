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

pacls = ["cat - reads a specified file" , "whoami - prints user name" , "PyFetch - a fetch script for PyArch" , "echo - prints user input or file location" , "man - shows the PyArch documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyArch license" , "credits - prints the PyArch credits" , "map - prints the filesystem map"]

custom = 0

cusset = 1

uset = 1

name = ""

host = ""

ls = root

instp = "0"

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

                pacls = ["cat - reads a specified file" , "whoami - prints user name" , "PyFetch - a fetch script for PyArch" , "echo - prints user input or file location" , "man - shows the PyArch documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyArch license" , "credits - prints the PyArch credits" , "map - prints the filesystem map"]

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

                pacuser = ["cat" , "whoami" , "PyFetch" , "echo" , "man" , "chname", "chhost" , "license" , "credits" , "map"]
                
                name = "root"

                host = "PyArch"

                setup = 0

                init = 0

                custom = 0

                pacprefselect = 0

                usernamecustom = 0

                hostnamecustom = 0

                packagescustom = 0

                instp = "10"

                print("Type 'help' for a list of commands")

                arch = 1

            if disset == 2:

                packages = pacsystem

                pacls = ["cat - reads a specified file" , "whoami - prints user name" , "PyFetch - a fetch script for PyArch" , "echo - prints user input or file location" , "man - shows the PyArch documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyArch license" , "credits - prints the PyArch credits" , "map - prints the filesystem map"]

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

                pacuser = []

                cls()

                instp = "0"

                name = "root"

                host = "PyArch"

                print("Type 'help' for a list of commands")

                arch = 1

            if disset == 3:

                cusset = 1
                
                packages = pacsystem

                pacls = ["cat - reads a specified file" , "whoami - prints user name" , "PyFetch - a fetch script for PyArch" , "echo - prints user input or file location" , "man - shows the PyArch documentation" , "chname - changes the username" , "chhost - changes the host name" , "license - prints the PyArch license" , "credits - prints the PyArch credits" , "map - prints the filesystem map"]

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

                    uset = 1

                    arch = 0

                    packagescustom = 1

            if uset == 3:

                uset = 1
                
                cls()

                packagescustom = 0

                custom = 1

                cusset = 1

                arch = 0

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

                instp = "10"

            if uset == 2:

                pacls = []
                
                packages = ["pwd" , "ls" , "cd" , "pacman" , "help" , "clear" , "exit" , "cat" , "whoami" , "rm" , "rs" , "PyFetch" , "echo" , "man" , "chname" , "chhost" , "license" , "credits" , "map" , "pacls"]

                pacsystem = ["pwd" , "ls" , "cd" , "pacman" , "help" , "clear" , "exit"]

                pacuser = ["cat" , "whoami" , "rm" , "rs" , "PyFetch" , "echo" , "man" , "chname" , "chhost" , "license" , "credits" , "map" , "pacls"]

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

                init = 1
                
                arch = 0

                cusset = 1

                disset = 1

                pacprefselect = 1

                instp = "0"
    
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
            print(Back.RESET + Fore.WHITE + "exit - exit PyArch" + Back.RESET + Fore.WHITE)

        if a == "pacls":

            print(Back.RESET + Fore.WHITE + '\n'.join(pacls) + Back.RESET + Fore.RESET)

        if a == "ls":

            print(Back.RESET + Fore.WHITE + '   '.join(ls) + Back.RESET + Fore.RESET)

        if a == "exit":

            cls()

            quit()

        if a == "clear":

            cls()

        if a == "cd user-files":

            if ls == root:
            
                ls = userfiles

                pwd = "/user-files"

        if a == "cd /user-files":

            ls = userfiles

            pwd = "/userfiles"

        if a == "cd pac":

            if ls == root:

                ls =  pac
            
                pwd = "/pac"

        if a == "cd /pac":

            ls = pac

            pwd = "/pac"

        if a == "cd config":

            if ls == root:

                ls = config

                pwd = "/config"

        if a == "cd /config":

            ls = config

            pwd = "/config"

        if a == "cd info":

            if ls == root:

                ls = info
                
                pwd = "/info"

        if a == "cd /info":

            ls = info

            pwd = "/info"

        if a == "cd system":

            if ls == pac:

                ls = pacsystem

                pwd = "/pac/system"

        if a == "cd /pac/system":

            ls = pacsystem

            pwd = "/pac/system"

        if a == "cd user":

            if ls == pac:

                ls = pacuser
                
                pwd = "/pac/users"

        if a == "cd /pac/user":

            ls = pacuser

            pwd = "/pac/user"

        if a == "cd /":

            ls = root

            pwd = "/"

        if a == "cd ..":

            if ls == userfiles:

                ls = root

                pwd = "/"

            if ls == pac:

                ls = root

                pwd = "/"

            if ls == config:

                ls = root

                pwd = "/"

            if ls == pac:

                ls = info

                pwd = "/"

            if ls == pacsystem:

                ls = pac
                
                pwd = "/pac"

            if ls == pacuser:

                ls = pac

                pwd = "/pac"

            if ls == info:

                ls = root

                pwd = "/"

        if a == "pacman cat":

            if catinstalled == 0:

                print(Back.RESET + Fore.WHITE + "cat has been installed, for a guide on how to use it, type 'pacls', or look it up with 'man'" + Back.RESET + Fore.RESET)

                pacuser.append('cat')

                catinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "cat is already installed, look it up with 'pacls' or 'man'" + Back.RESET + Fore.RESET)

        if a == "pacman whoami":

            if whoamiinstalled == 0:

                print(Back.RESET + Fore.WHITE + "whoami has been installed, type 'whoami' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('whoami')

                whoamiinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "whoami is already installed, run it by typing 'whoami'" + Back.RESET + Fore.RESET)

        if a == "pacman PyFetch":

            if pyfetchinstalled == 0:

                print(Back.RESET + Fore.WHITE + "PyFetch has been sucessfully install, type 'pyfetch' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('PyFetch')

                pyfetchinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "PyFetch is already installed, run it by typing 'pyfetch'" + Back.RESET + Fore.RESET)

        if a == "pacman echo":

            if  echoinstalled == 0:

                print(Back.RESET + Fore.WHITE + "echo has been installed, look it up with 'pacls' or 'man'" + Back.RESET + Fore.RESET)

                pacuser.append('echo')

                echoinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "echo is already installed, look it up with 'pacls' or 'man'" + Back.RESET + Fore.RESET)

        if a == "pacman man":

            if maninstalled == 0:

                print(Back.RESET + Fore.WHITE + "man has been installed, type 'man' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('man')

                maninstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "man is already installed, run it by typing 'man'" + Back.RESET + Fore.RESET)

        if a == "pacman chname":

            if chnameinstalled == 0:

                print(Back.RESET + Fore.WHITE + "chname has been installed, type 'chname' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('chname')

                chnameinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "chname is already installed, run it by typing 'chname'" + Back.RESET + Fore.RESET)

        if a == "pacman chhost":

            if chhostinstalled == 0:

                print(Back.RESET + Fore.WHITE + "chhost has been installed, type 'chhost' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('chhost')

                chhostinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "chhost is already installed, run it by typing 'chhost'" + Back.RESET + Fore.RESET)

        if a == "pacman license":

            if licenseinstalled == 0:

                print(Back.RESET + Fore.WHITE + "license has been installed, type 'license' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('license')

                licenseinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "license is already installed, run it by typing 'license'" + Back.RESET + Fore.RESET)

        if a == "pacman credits":

            if creditsinstalled == 0:

                print(Back.RESET + Fore.WHITE + "credits has been installed, type 'credits' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('credits')

                creditsinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "credits is already installed, run it by typing 'credits'" + Back.RESET + Fore.RESET) 

        if a == "pacman map":

            if mapinstalled == 0:

                print(Back.RESET + Fore.WHITE + "map has been installed, type 'map' to try it out" + Back.RESET + Fore.RESET)

                pacuser.append('map')

                mapinstalled = 1

            else:

                print(Back.RESET + Fore.WHITE + "map is already installed, run it by typing 'map'" + Back.RESET + Fore.RESET)

        if a == "cat Arch.txt":

            if ls == userfiles:

                if catinstalled == 1:

                    print(Back.RESET + Fore.WHITE + "PyArch is very much inspired by Arch Linux, it's more customizeable from the boot screen." + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "PyArch minus also has a slightly more closed syntax when it comes to two-worded directory names" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "but it's not that noticeable. The doc command has been replaced with man, and I've added a package" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "manager in the form of 'pacman' and 'pacls'. It also has highlighting through colorama which makes" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "it look a lot nicer. Other than that, you still can't add files without editing the source code, " + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "make directories or really edit the filesystem. The only plans I have for PyArch down the line is" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "to add a few more packages." + Back.RESET + Fore.RESET)

        if a == "cat installs.txt":

            if ls == userfiles:

                if catinstalled == 1:

                    print(Back.RESET + Fore.WHITE + "Out of the box, PyArch comes with 3 options for 'installing' it, full install, which means you get" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "all possible packages preinstalled, and nothing much else. Then there's lite mode, which just comes" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "with system-only packages. And the best option, is the custom boot, this allows you to set a custom" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "username and hostname, and select your package preference. The real benefit is that you can edit your " + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "name without having to install 'chname' and it feels more personal. Later down the line I might add" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "the option to rename directories and base files. :3" + Back.RESET + Fore.RESET)

        
        if a == "cat Arch.config":

            if ls == config:

                if catinstalled == 1:

                    print(Back.RESET + Fore.WHITE + "root user: " + name + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "host machine: " + host + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "packages preference: " + pacpref + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "installed packages on boot: " + instp + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "PyArch repository version: 1.0.0" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "Filesystem access: read-only" + Back.RESET + Fore.RESET)

        if a == "cat credits.txt":

            if ls == info:

                if catinstalled == 1:

                    print(Back.RESET + Fore.WHITE + "Made by Franco M. (SrFluff - GitHub) with Python by Guido van Rossum in Visual Studio Code" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "by Microsoft, hosted on GitHub by Microsoft, inspired by Linux by Linus Torvals" + Back.RESET + Fore.RESET)
                    print(Back.RESET + Fore.WHITE + "and Arch by Judd Vinet, Colorama by Jonathan Hartley. All code written by me (Franco M.)" + Back.RESET + Fore.RESET)

        if a == "cat license.txt":

            if ls == info:

                if catinstalled == 1:

                    print(Back.RESET + Fore.WHITE + "Licensed under the GNU public license v3.0" + Back.RESET + Fore.RESET)  

        if a == "credits":

            if creditsinstalled == 1:

                print(Back.RESET + Fore.WHITE + "Made by Franco M. (SrFluff - GitHub) with Python by Guido van Rossum in Visual Studio Code" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "by Microsoft, hosted on GitHub by Microsoft, inspired by Linux by Linus Torvals" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "and Arch by Judd Vinet, Colorama by Jonathan Hartley. All code written by me (Franco M.)" + Back.RESET + Fore.RESET)

        if a == "license":

            if licenseinstalled == 1:

                print(Back.RESET + Fore.WHITE + "Licensed under the GNU public license v3.0" + Back.RESET + Fore.RESET)

        if a == "cat version.txt":

            if catinstalled == 1:

                print(Back.RESET + Fore.WHITE + "PyArch v1.0.0 'Apricot'" + name + Back.RESET + Fore.RESET)

        if a == "whoami":

            if whoamiinstalled == 1:
            
                print(Back.RESET + Fore.WHITE + name + Back.RESET + Fore.RESET)

        if a == "pyfetch":

            if pyfetchinstalled == 1:

                print(Back.RESET + Fore.WHITE + "OS: PyArch v1.0.0 'Apricot'" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "Name: " + name + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "Host: " + host + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "Kernel: PyLinux kernel v1.0.0" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "Shell: N/A" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "Package manager: pacman" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "Main repository: PyArch repo 1" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "Installer: PyArch basic installer" + Back.RESET + Fore.RESET)

        if a == "chname":

            if chnameinstalled == 1:

                cls()

                print(Back.RESET + Fore.WHITE + "Type your new username (Leave blank to cancel)\n" + Back.RESET + Fore.RESET)

                a = input(Back.RESET + Fore.WHITE + "> " + Back.RESET + Fore.RESET)

                if not a == "":

                    name = a

                print(Back.RESET + Fore.WHITE + "Type 'help' for a list of commands" + Back.RESET + Fore.RESET)

        if a == "chhost":

            if chhostinstalled == 1:

                cls()

                print(Back.RESET + Fore.WHITE + "Type your new hostname (Leave blank to cancel)\n" + Back.RESET + Fore.RESET)

                a = input(Back.RESET + Fore.WHITE + "> " + Back.RESET + Fore.RESET)

                if not a == "": 

                    host = a

                print(Back.RESET + Fore.WHITE + "Type 'help' for a list of commands" + Back.RESET + Fore.RESET)

        if a == "echo":

            if echoinstalled == 1:
            
                a = input("> ")

                if a == "Arch.txt":

                    print(Back.RESET + Fore.WHITE + "/user-files" + Back.RESET + Fore.RESET)

                if a == "installs .txt":

                    print(Back.RESET + Fore.WHITE + "/user-files" + Back.RESET + Fore.RESET)

                if a == "Arch.config":

                    print(Back.RESET + Fore.WHITE + "/config" + Back.RESET + Fore.RESET)

                if a == "credits.txt":

                    print(Back.RESET + Fore.WHITE + "/info" + Back.RESET + Fore.RESET)

                if a == "license.txt":

                    print(Back.RESET + Fore.WHITE + "/info" + Back.RESET + Fore.RESET)

                if a == "version.txt":

                    print(Back.RESET + Fore.WHITE + "/info" + Back.RESET + Fore.RESET)

                else:

                   print(Back.RESET + Fore.WHITE + a + Back.RESET + Fore.RESET)

        if a == "map":

            if mapinstalled == 1:

                print(Back.RESET + Fore.WHITE + "/" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "-> /user-files /pac /config /info" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "/user-files" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "-> Arch.txt installs.txt" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "/pac" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "-> /system /user" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "/system" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "-> pwd ls cd pacman help clear exit" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "/user" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "-> !^$#$**&@$*&$&*#*&$@&)" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "/config" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "-> Arch.config" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "/info" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "-> credits.txt license.txt version.txt" + Back.RESET + Fore.RESET)

        if a == "man":

            if maninstalled:

                print(Back.RESET + Fore.WHITE + "PyArch Manual" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "By Franco M.\n" + Back.RESET + Fore.RESET)
                
                print(Back.RESET + Fore.WHITE + "Navigating the filesystem\n" + Back.RESET + Fore.RESET)

                print(Back.RESET + Fore.WHITE + "pwd\n" + Back.RESET + Fore.RESET)
                
                print(Back.RESET + Fore.WHITE + "To print the current working directory use the 'pwd' the current directory is also displayed" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "after the hostname and before the '$', here's an example: 'user:@host/$' where '/' is the working" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "directory\n" + Back.RESET + Fore.RESET)

                print(Back.RESET + Fore.WHITE + "ls\n" + Back.RESET + Fore.RESET)

                print(Back.RESET + Fore.WHITE + "To list the contents of the current directory type 'ls' and all the contents will be printed three" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "spaces appart from eachother. Anything that isn't followed by .txt, or anything that isn't in the" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "/pac/system or /pac/user directory is a directory, or sub-directory.\n" + Back.RESET + Fore.RESET)

                print(Back.RESET + Fore.WHITE + "cd\n" + Back.RESET + Fore.RESET)

                print(Back.RESET + Fore.WHITE + "To change the current directory type 'cd' followed by the name or path of a directory, if you only" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "specify the name then you must be in a directory directly below that directory, for example: /pac is" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "bellow /pac/system. If you use the full filepath, like going from /pac/user to / you don't need to" + Back.RESET + Fore.RESET)
                print(Back.RESET + Fore.WHITE + "worry about " + Back.RESET + Fore.RESET)
