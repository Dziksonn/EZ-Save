import os
import time
from datetime import datetime
import shutil

class ZaladowanieZmiennych:

    def dirconv(rawdir):
        if rawdir.find("[User]") != -1:
            return(rawdir.replace("[User]", os.path.expanduser('~')))
        else:
            return(rawdir)

    def __init__(self, nazwa):
        file = open("config.txt", 'r')
        linijki = file.readlines()
        x = 0
        for linijki[x] in linijki:
            self.Id = linijki[x].split(";")[0]
            self.Nazwa = linijki[x].split(";")[1]
            rawdir = linijki[x].split(";")[2]
            self.Dir = ZaladowanieZmiennych.dirconv(rawdir)[:-1]
            self.Err = 0
            if self.Nazwa == nazwa:
                break
            elif self.Id == nazwa:
                break
            elif self.Nazwa == "0000" or self.Id == "0" or self.Dir == "0000":
                self.Err = 1



class Menu:
    def __init__(self):
        Menu.glowne()

    def glowne():
        os.system('cls')
        print("Menu głowne:")
        print("    1. Wybierz gre")
        print("    2. Lista gier\n")
        wybor = input()
        if wybor == "1":
            Menu.game_select()
        elif wybor =="2":
            Menu.all_games()
        else:
            print("Wpisana zla cyfre. Powracam do menu")
            time.sleep(5)

    def game_select():
        Wybrana = ZaladowanieZmiennych(input("Wpisz nazwe albo id: "))
        if Wybrana.Err != 1:
            Menu.game_actions(Wybrana)
        else:
            print("Error: Nie znaleziono gry.")
        input()

    def game_actions(obiekt):
        os.system('cls')
        print("Jakiej akcji poddać grę \033[1;32;40m"+obiekt.Nazwa+"\033[1;37;40m?")
        print("    1. Zrób backup")
        print("    2. Wrzuć backup do gry")
        wybor = input("\n")
        if wybor == "1":
            FileManager.makebackup(obiekt)
        elif wybor == "2":
            FileManager.loadbackup(obiekt)
    
    def all_games():
        os.system('cls')
        count = len(open("config.txt").readlines())
        for x in range(1, count):
            Gra = ZaladowanieZmiennych(str(x))
            print(Gra.Id +". " + Gra.Nazwa)
            x =+ 1
        print("Co teraz zrobić?:")
        print("    1. Menu glowne")
        print("    2. Wybor gry")
        wybor = input()
        if wybor == "1":
            Menu()
        elif wybor == "2":
            Menu.game_select()
        else:
            print("spierdalaj psychopatko jebana")

class FileManager:
    def makebackup(obiekt):
        czas = datetime.now().strftime("%d.%m.%Y %H;%M;%S")
        FileManager.CreateAndOpen("Saves")
        FileManager.CreateAndOpen(obiekt.Nazwa)
        os.mkdir(czas)
        shutil.copytree(obiekt.Dir, czas, dirs_exist_ok=True)
        print("Zrobiono backup plików z datą: " + czas)
        
        

    def loadbackup(obiekt):
        os.system('cls')
        print(obiekt.Nazwa)
        FileManager.CreateAndOpen("Saves")
        FileManager.CreateAndOpen(obiekt.Nazwa)
        l = list(os.listdir())
        counter = 0
        for x in l:
            counter += 1
            print("\033[1;32;40m" + str(counter) + "\033[1;37;40m - " + x)
        print("\nKtóry backup wybrać?")
        wybor = input()
        os.chdir(l[int(wybor)-1])
        shutil.copytree(os.getcwd(), obiekt.Dir, dirs_exist_ok=True)
        print("Wgrano backup plików do: \033[1;32;40m"+ obiekt.Dir + "\033[1;37;40m")


    def CreateAndOpen(name):
        if os.path.exists(name) == True:
            os.chdir(name)
        else:
            os.mkdir(name)
            os.chdir(name)

Menu()









