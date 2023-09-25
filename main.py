import os
import requests

def download_github_file(raw_link, filepath = None):
    
    response = requests.get(raw_link)
    if filepath == None: print("Need to enter filepath aswell.")
    
    with open(filepath, "wb") as f:
        f.write(response.content)




desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
download_github_file("https://raw.githubusercontent.com/Dominik-Gryko/Geko-Bot/main/cogs/fun.py", f"{desktop}/robux.py")

