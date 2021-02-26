from PIL import Image,ImageGrab
import time
time.sleep(3)
img=ImageGrab.grab()
data=img.load()
for i in range(300,365):
    for j in range(320,380):
        data[i, j]=0
img.show()