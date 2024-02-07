from tkinter import *
import pystray
from PIL import Image
from pystray import MenuItem as item
from desk_clean import *
import psutil
import shutil
import time
import threading

def popup_window(message):
    """
    The function take a message as argument and create a popup window.
    """

    pass

def check_pc_health():
    """
    This function by using psutil and shutil modules return the cpu usage,
    ram usage and free disk space in % in a tuple format.
    """

    cpu = psutil.cpu_percent(interval=0.5, percpu=False)
    ram = psutil.virtual_memory()[2]
    disk = round(shutil.disk_usage("C:")[2] / shutil.disk_usage("C:")[0] * 100)
    return cpu, ram, disk

def change_title():
    """
    The function enter in a while loop and checks every 1 second the cpu usage,
    ram usage and free disk space and assign to (icon.title) object.
    """

    while True:
        icon.title = f"CPU: {check_pc_health()[0]}%\n" + \
                     f"RAM: {check_pc_health()[1]}%\n" + \
                     f"DISK: {check_pc_health()[2]}%"
        time.sleep(1)

def check_desktop_status():
    """
    The function checks automatically every 30 minutes, if on desktop there are
    more than 10 folders and files then it call a popup window.
    """

    while True:
        time.sleep(1800)
        desktop = check_desktop()
        counter = 0
        if desktop:
            for item in desktop:
                if item != files_folder and item != folders_folder and "lnk" not in item:
                    counter += 1
        if exit_event.is_set():
            break
        if counter > 10:
            popup_window("Your desktop need to be cleaned!")

def optimizer(icon, item):
    """
    This function is a part of system tray menu it calls the clean_desktop function.
    """
    clean_desktop()

def quit_window(icon, item):
    """
    This function is a part of system tray menu it calls the stop() function from icon object.
    """

    icon.stop()

if __name__ == "__main__":
    #Created a threading event object
    exit_event = threading.Event()
    #Created a thread object that creates a separate process and run check_desktop_status function
    thread_check_desktop = threading.Thread(daemon=True, target=check_desktop_status)
    thread_check_desktop.start()
    #Created on system tray bar a menu
    image = Image.open("favicon.ico")
    menu = item("Clean Desktop", optimizer), item("Quit", quit_window)
    icon = pystray.Icon("name", image, str(check_pc_health()), menu)
    #Created a thread object that creates a separate process and run change_title function
    thread_change_title = threading.Thread(daemon=True, target=change_title)
    thread_change_title.start()
    icon.run()
    exit_event.set()