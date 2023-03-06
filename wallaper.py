import requests
import cv2
import random
import os
import numpy as np
import ctypes

def get_img():
    try:
        keywords = ['beach','mercedes','coding','code','setup','lamborghini','BMW','coder','bugatti']
        url = f"https://source.unsplash.com/random/3840x2160/?{random.choice(keywords)}"
        response = requests.get(url)
        image_array = response.content
        image = cv2.imdecode(np.frombuffer(image_array, np.uint8), cv2.IMREAD_UNCHANGED)
        cv2.imwrite("image.jpg", image)
        return True
    except Exception as e:
        return False

def set_wallpaper():
    path = f'{os.getcwd()}\\image.jpg'
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 3)

if(get_img()):
    set_wallpaper()