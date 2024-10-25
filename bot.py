import time
import keyboard
import pyautogui

def ss():
    ss = pyautogui.screenshot()
    ss.save('ss.png')
# ss()

def like_video():
    pyautogui.click(1626, 699)
    time.sleep(1)

def google_search():
    if (pyautogui.locateOnScreen('search_bar.png') != None):
        google_bar = pyautogui.locateOnScreen('search_bar.png')
        pyautogui.click(google_bar)
        time.sleep(3)
        pyautogui.write('https://www.youtube.com/watch?v=393C3pr2ioY&pp=ygUDd293')
        pyautogui.press('enter')
        time.sleep(3)
        like_video()
google_search()

def show_coords():
    while not keyboard.is_pressed('z'):
        print(pyautogui.position())
        time.sleep(0.5)
# show_coords()