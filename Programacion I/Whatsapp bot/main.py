import pyautogui as auto
import time 

time.sleep(5)

f = open('texto.txt','r')

for word in f:
    auto.typewrite(word)
    auto.press("enter")
