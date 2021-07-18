import json
from add_config import add_configuration
from ahk import AHK
from time import sleep
from os import system

_ = system('cls')

ahk = AHK(executable_path="E:\\programfiles\\AutoHotkey\\AutoHotkey.exe")
data = {}
data["windows"] = []
log = True

def title():
    print("_________________________________________________________________________")
    print("  _      ___         __             __  ___                              ")    
    print(" | | /| / (_)__  ___/ /__ _    __  /  |/  /__ ____  ___ ____ ____ ____   ") 
    print(" | |/ |/ / / _ \/ _  / _ \ |/|/ / / /|_/ / _ `/ _ \/ _ `/ _ `/ -_) __/   ")
    print(" |__/|__/_/_//_/\_,_/\___/__,__/ /_/  /_/\_,_/_//_/\_,_/\_, /\__/_/      ")
    print("                                                       /___/ Adam G.     ")
    print("_________________________________________________________________________")
    print("")

def done(message):
    print("  ___               ")
    print(" |   \ ___ _ _  ___ ")
    print(" | |) / _ \ ' \/ -_)")
    print(" |___/\___/_||_\___|", message)
    print("")

def end(message):
    print("  ___          ")
    print(" | _ )_  _ ___ ")
    print(" | _ \ || / -_)")
    print(" |___/\_, \___|", message)
    print("      |__/     ")
    print("")

def move_windows():
    for window in ahk.windows():
        for config in data["windows"]:
            if config["name"] in str(window.process).lower() and config["name"] in str(window.title).lower():

                window.move(config["x"], config["y"], config["width"], config["height"])

                if log == True:
                    print("LOG: MOVED: moved {} to saved location {}.".format(config["name"], window.rect))
    
    if log == True:
                print("LOG: END: moving-sequence.")
                print("")

def open_windows():
    checklist = []
    for config in data["windows"]:
        checklist.clear()
        for window in ahk.windows():
            if config["name"] in str(window.title).lower():
                checklist.append(True)
            
        if not True in checklist:
            path = config["process"]
            ahk.run_script("Run {}".format(path))
            if log == True:
                print("LOG: STARTING: starting {} at location: {}.".format(config["name"], config["process"]))
                detection_list = []
                while not True in detection_list:
                    if log == True:
                        print("LOG: WAITING: waiting for {} at location: {} to open a window.".format(config["name"], config["process"]))
                    for window in ahk.windows():
                        if config["name"] in str(window.title).lower() or config["name"] in str(window.title).lower():
                            detection_list.append(True)
                            if log == True:
                                print("LOG: DETECTED: detected window from {} at location: {}.".format(config["name"], config["process"]))
        else:
            if log == True:
                print("LOG: OPEN: programm {} at location: {} is allready open.".format(config["name"], config["process"]))
    
    if log == True:
                print("LOG: END: starting-sequence.")
                print("")

title()
with open("configuration.json", "r") as infile:
        indata = json.load(infile)
        if len(indata["windows"]) == 0:
            print("Sie haben noch keine configuration angelegt.")
            add_configuration()
        else:
            for window in indata["windows"]:
                data["windows"].append(window)
            open_windows()
            move_windows()
            if log == True:
                sleep(3)
                _ = system("cls")
                title()
            done("Deine gespeicherte configuration wurde hergestellt.")
            sleep(3)
            _ = system("cls")
            title()
            add_configuration()
            _ = system("cls")
            title()

end("Auf Wiedersehen.")
