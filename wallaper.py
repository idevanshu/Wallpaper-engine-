import requests
import cv2
import random
import os
import numpy as np
import hashlib
import ctypes
import threading

CACHE_DIR = "cache"

def get_img():
    try:
<<<<<<< HEAD
        keywords = ['bugatti','hills','lamborghini','mercedes','bmw','moutains']
=======
        keywords = ['supercars','nature','hills']
        keywords.sort()
>>>>>>> 5b1753971fdb4ada1f4f14847777e8c3a93130bb
        url = f"https://source.unsplash.com/random/3840x2160/?{random.choice(keywords)}"
        # Generate a hash of the URL to use as the filename
        filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"
        cache_path = os.path.join(CACHE_DIR, filename)
        if os.path.exists(cache_path):
            # If the image is already downloaded, load it from the cache
            image = cv2.imread(cache_path)
        else:
            # Otherwise, download the image and save it to the cache
            response = requests.get(url)
            image_array = response.content
            image = cv2.imdecode(np.frombuffer(image_array, np.uint8), cv2.IMREAD_UNCHANGED)
            cv2.imwrite(cache_path, image)
        cv2.imwrite("image.jpg", image)
        return True
    except Exception as e:
        return False

def set_wallpaper():
    path = f'{os.getcwd()}\\image.jpg'
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 3)

if get_img():
    # Download image in the background
    t = threading.Thread(target=get_img)
    t.start()

# Set the wallpaper
set_wallpaper()
