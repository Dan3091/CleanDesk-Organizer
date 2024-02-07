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


def folder_organizer(item):
    """
       The function takes the name of a folder as argument,
       first it checks if the folder is not empty then
       it tries to create the main folder(Desktop_Data_Folders),
       checks if there isn't any folder with the same name,
       move it to the main folder on desktop(Desktop_Data_Folders),
       otherwise move it and change the name of the folder.
    """

    if os.listdir(path + item):
        try:
            os.mkdir(os.path.join(path, folders_folder))
        except:
            pass
        if item not in os.listdir(path + folders_folder + "\\"):
            os.rename(path + item, path + folders_folder + "\\" + item)
        else:
            while True:
                generated_number = str(random.randint(1000, 9999))
                if item + generated_number not in os.listdir(path + folders_folder + "\\"):
                    os.rename(path + item, path + folders_folder + "\\" + item + generated_number)
                    break
    else:
        os.rmdir(path + item)

def file_organizer(item):
    """
       The function takes the name of a file as argument,
       first it checks if the size of the file is diverse from 0
       then it tries to create the main folder(Desktop_Data_Files)
       if it doesn't already exist then it try to create a folder
       for the specified file format, finally it move the file
       to that folder, if the file with the same name already exists
       then it rename it then move it.
    """

    if os.path.getsize(path + item) != 0:
        name_format = os.path.splitext(item)
        folder_name = name_format[1][1:]
        try:
            os.mkdir(os.path.join(path, files_folder))
        except:
            pass
        try:
            os.mkdir(os.path.join(path + files_folder + "\\", folder_name))
        except:
            pass
        if item not in os.listdir(path + files_folder + "\\" + folder_name + "\\"):
            os.rename(path + item, path + files_folder + "\\" + folder_name + "\\" + item)
        else:
            while True:
                generated_number = str(random.randint(1000, 9999))
                if item + generated_number not in os.listdir(path + files_folder + "\\"
                                                             + folder_name + "\\"):
                    os.rename(path + item, path + files_folder + "\\"
                              + folder_name + "\\" + name_format[0]
                              + generated_number + name_format[1])
                    break
    else:
        os.remove(path + item)