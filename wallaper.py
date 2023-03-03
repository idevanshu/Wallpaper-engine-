import requests
import ctypes
import random
from PIL import Image
import os

keywords = ['space','coding','code','setup','lamborghini']
url = f"https://source.unsplash.com/random/1900x1080/?{random.choice(keywords)}"

img = Image.open(requests.get(url, stream = True).raw)
img.save('image.jpg')
path = f'{os.getcwd()}\\image.jpg'


SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 3)