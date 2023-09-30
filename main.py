import os
import sys

import download
import shortcuts
import wallpaper


def main():

    shortcut_name = "Microsoft Teens"
    shortcuts.run_on_startup(shortcut_name=shortcut_name)

    documents = os.path.normpath(os.path.expanduser("~/Documents"))
    image_path = f"{documents}\Reader\\texture_01.png"
    download.download_raw_content("https://pbs.twimg.com/media/Fu8AKWJWIAApsVk.jpg", image_path)
    wallpaper.change_wallpaper(image_path)

main()