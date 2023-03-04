import requests
import ctypes
import random
from PIL import Image
import os

keywords = ['trees','wild','coding','code','setup','lamborghini','BMW','coder','nature']
url = f"https://source.unsplash.com/random/3840x2160/?{random.choice(keywords)}"

img = Image.open(requests.get(url, stream = True).raw)
img.save('image.jpg')
path = f'{os.getcwd()}\\image.jpg'


SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 3)