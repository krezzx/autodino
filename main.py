import pyautogui
import time
# from numpy import asarray
from PIL import Image, ImageGrab


def takess():
    img = ImageGrab.grab().convert('L')
    return img


def hit(key):
    pyautogui.keyDown(key)


# def draw():

def iscollidedata(data):
    for i in range(300, 345):
        for j in range(300, 367):
            if data[i, j] > 150:
                return True
    return False


if __name__ == '__main__':
    time.sleep(3)
    while True:
        img = takess()
        data = img.load()
        if iscollidedata(data):
            hit("up")
    # print(asarray(img))
