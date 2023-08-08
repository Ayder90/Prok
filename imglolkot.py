from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import cv2
import numpy as np

url4 = "https://lolkot.ru/album/"


page4 = requests.get(url4)

sup = BeautifulSoup(page4.text, "html.parser")

img = set()

for com in sup.find_all("img"):
    image = com.get("src")
    img.add(image)

print(img)

for img_1 in img:
    resp = requests.get(img_1, stream=True).raw #stream - будет передавть все по потоку (True), raw- позволяет передавать все информацию одной строкой
    image2 = np.asarray(bytearray(resp.read()), dtype="uint8") # assaray - массив numpy, bytearraw - массив байтов 
    image2 = cv2.imdecode(image2, cv2.IMREAD_COLOR)
    print(img_1)
    
    try:
        cv2.imshow('image',image2)
        cv2.waitKey(0)
    except cv2.error:
        continue






# cv2.imshow()
# cv2.waitKey

