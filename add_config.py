def add_configuration():

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
        print(" |___/\___/_||_\___|" , message)
        print("")

    def menu():
        print("  __  __              ")
        print(" |  \/  |___ _ _ _  _ ")
        print(" | |\/| / -_) ' \ || |")
        print(" |_|  |_\___|_||_\_,_|")
        print("")

    import json
    from ahk import AHK
    from time import sleep
    from os import system

    ahk = AHK(executable_path="E:\\programfiles\\AutoHotkey\\AutoHotkey.exe")
    found = False
    data = {}
    data["windows"] = []

    with open("configuration.json", "r") as infile:
        indata = json.load(infile)
        for window in indata["windows"]:
            data["windows"].append(window)

    add = input("Neue configuration hinzufügen oder vorhandene configuration bearbeiten? [Y/N]  ").upper()
    _ = system("cls")
    title()
    while add == "Y":
        edit = int(input("Wähle zwischen hinzufügen [1] und bearbeiten [2].  "))
        _ = system("cls")
        title()
        if edit == 1:
            name = input("Name des neuen Prozesses: ").lower()
            input("Öffne das Programm und bring das Fenster in die gewünschte Position und größe. Drücke dann Enter.")
            _ = system("cls")
            title()
            for window in ahk.windows():
                if name in str(window.title).lower() and name in str(window.process).lower():
                    found = True
                    
                    coord_values = []

                    for coord in window.rect:
                        coord_values.append(coord)
                    
                    edit = input("Möchten sie an Größe und Position Feinabstimmungen vornehmen? [Y/N]  ").upper()
                    _ = system("cls")
                    title()
                    if edit == "Y":
                        indexes = ["x", "y", "breite", "höhe"]
                        for i, index in zip(range(4), indexes):
                            edit_var = input("Möchten sie Änderungen am {} Wert vornehmen? [Y/N]  ".format(index)).upper()
                            _ = system("cls")
                            title()
                            while edit_var == "Y":
                                print(coord_values)
                                coord_values[i] += int(input("Um wie viele Pixel möchten sie den {} Wert ändern? [positive oder negavive Zahl]  ".format(index)))
                                _ = system("cls")
                                title()
                                window.move(coord_values[0], coord_values[1], coord_values[2], coord_values[3])
                                edit_var = input("Möchten sie weitere Änderungen am {} Wert vornehmen? [Y/N]  ".format(index)).upper()
                                _ = system("cls")
                                title()

                    data["windows"].append({
                        "name": name,
                        "process": str(window.process),
                        "x": window.rect[0],
                        "y": window.rect[1],
                        "width": window.rect[2],
                        "height": window.rect[3]
                    })
            if found == False:
                print("Fenster konnte nicht gefunden werden. Stlle sicher das das Fenster offen ist und der Name der Programmes stimmt.")
                sleep(3)
                _ = system("cls")
                title()
            found = False
        elif edit == 2:
            name_list = []
            for config in data["windows"]:
                name_list.append(config["name"])
            
            edit_option = input("Wähle eine den folgenden configurationen zum bearbeiten: {} \n[namen eingeben]:  ".format(name_list))
            _ = system("cls")
            title()
            for config in data["windows"]:
                if config["name"] == edit_option.lower():
                    editing = "Y"
                    while editing == "Y":
                        print("[0] Ich möchte das Fenster in die gewünschte Position und Größe ziehen.")
                        print("[1] X-Koordinate: {}".format(config["x"]))
                        print("[2] Y-Koordinate: {}".format(config["y"]))
                        print("[3] Breite: {}".format(config["width"]))
                        print("[4] Höhe: {}".format(config["height"]))
                        print("")
                        sub_edit_option = int(input("Wähle eine der Optionen oben. [Zahl eingeben]  "))
                        _ = system("cls")
                        title()
                        if sub_edit_option == 0:
                            input("Bringe das Fenster in die gewünschte Position und größe. Drücke dann Enter.")
                            _ = system("cls")
                            title()
                            sub_found = False
                            for window in ahk.windows():
                                if config["name"] in str(window.title).lower() and config["name"] in str(window.process).lower():
                                    sub_found = True

                                    config["x"] = window.rect[0]
                                    config["y"] = window.rect[1]
                                    config["width"] = window.rect[2]
                                    config["height"] = window.rect[3]

                            if sub_found == False:
                                print("Fenster konnte nicht gefunden werden. Stelle sicher das das Fenster offen ist und der Name der Programmes stimmt.")
                                sleep(3)
                                _ = system("cls")
                                title()
                        
                        elif sub_edit_option >= 1:
                            indexes = ["x", "y", "Breite", "Höhe"]
                            sub_coord_values = []
                            change = "Y"
                            while change == "Y":
                                sub_coord_values.clear()
                                sub_coord_values.append(config["x"])
                                sub_coord_values.append(config["y"])
                                sub_coord_values.append(config["width"])
                                sub_coord_values.append(config["height"])
                                sub_coord_values[sub_edit_option - 1] += int(input("Um wie viele Pixel möchten sie den {} Wert ändern? [positive oder negavive Zahl]  ".format(indexes[sub_edit_option - 1])))
                                _ = system("cls")
                                title()
                                sub_found = False
                                for window in ahk.windows():
                                    if config["name"] in str(window.title).lower() and config["name"] in str(window.process).lower():
                                        sub_found = True

                                        window.move(sub_coord_values[0], sub_coord_values[1], sub_coord_values[2], sub_coord_values[3])

                                if sub_found == False:
                                    print("Fenster konnte nicht gefunden werden. Vorschau nicht möglich.")
                                    sleep(3)
                                    _ = system("cls")
                                    title()

                                if sub_edit_option == 1:
                                    config["x"] = sub_coord_values[0]
                                elif sub_edit_option == 2:
                                    config["y"] = sub_coord_values[1]
                                elif sub_edit_option == 3:
                                    config["width"] = sub_coord_values[2]
                                elif sub_edit_option == 4:
                                    config["height"] = sub_coord_values[3]


                                change = input("Möchten sie weitere Änderungen am {} Wert vornehmen? [Y/N]  ".format(indexes[sub_edit_option - 1])).upper() 
                                _ = system("cls")
                                title()

                        editing = input("Möchtest du weitere Änderungen an {} vornehmen? [Y/N]  ".format(config["name"])).upper()
                        _ = system("cls")
                        title()

        add = input("Weitere configuration hinzufügen oder vorhandene configuration bearbeiten? [Y/N]  ").upper()
        _ = system("cls")
        title()

    with open("configuration.json", "w") as outfile:
            json.dump(data, outfile, indent=4)

    done("Deine Configuration ist gespeichert.")
    sleep(2)
    _ = system("cls")
    title()

    with open("configuration.json", "r") as infile:
        indata = json.load(infile)
        return len(indata["windows"])