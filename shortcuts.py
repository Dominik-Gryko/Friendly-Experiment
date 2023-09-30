import os
import winshell
import sys


def create_desktop_shortcut(target_path, shortcut_name):
    # Get the path to the desktop folder
    desktop = winshell.desktop()
    shortcut_path = os.path.join(desktop, f"{shortcut_name}.lnk")

    winshell.CreateShortcut(
        Path= shortcut_path,
        Target = target_path,
        Icon=(target_path, 1)
    )

def create_startup_shortcut(target_path, shortcut_name):
    startup = winshell.startup() #"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\\" 
    print(startup)
    shortcut_path = os.path.join(startup, f"{shortcut_name}.lnk")

    winshell.CreateShortcut(
        Path= shortcut_path,
        Target = target_path,
        Icon=(sys.executable, 1)
    )