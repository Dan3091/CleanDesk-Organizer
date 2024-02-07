import os
import random


user = os.getlogin()
path = f"C:\\Users\\{user}\\Desktop\\"
files_folder = "Desktop_Data_Files"
folders_folder = "Desktop_Data_Folders"

def check_desktop():
    """
       The function checks if on desktop there are files
       or folders that needs to be organized.
    """

    desktop = os.listdir(path)
    if desktop != []:
        for item in desktop:
            if item != files_folder and item != folders_folder and "lnk" not in item:
                return desktop
    return False