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
    pass
def check_pc_health():
    pass

def change_title():
    pass

def check_desktop_status():
    pass

def optimizer(icon, item):
    clean_desktop()

def quit_window(icon, item):
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