import pyautogui
import time
if __name__ == '__main__':
    f=open('try.txt','r')
    str=f.read()
    time.sleep(5)
    pyautogui.write(str)