import time
import pyautogui
import os
from scraper import check_keywords

def main():
    while True:
        time.sleep(1)
        pyautogui.keyDown('command')
        pyautogui.press('r')
        pyautogui.keyUp('command')

if __name__ == '__main__':
    main()