import ctypes
import os
import random

SUPPORTED_TYPES = (".jpg", ".png")
PATHS = ["D:\\Wallpaper", "E:\\Wallpaper"]

# source: https://www.geeksforgeeks.org/python/how-to-change-desktop-background-with-python/
# parameter explanation: https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-systemparametersinfow
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x14 
    SPIF_UPDATEINIFILE = 0x01 
    SPIF_SENDWININICHANGE = 0x02 

    try:
        return ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
    except Exception as e:
        print(f"Could not set wallpaper: {e}")
        return False

def get_radndom_picture(path, type):
    all_files = os.listdir(path)
    picutres = []
    for file in all_files:
        if file.lower().endswith(SUPPORTED_TYPES):
            picutres.append(file)
    return picutres

path = random.choice(PATHS)
new_wallpaper = random.choice(get_radndom_picture(path, SUPPORTED_TYPES))
wallpaper_path = os.path.join(path, new_wallpaper)
set_wallpaper(wallpaper_path)