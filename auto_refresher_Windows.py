import time
import pyautogui
import os
from scraper import check_keywords

def main():
    urls = []
    while True:
        time.sleep(1)
        pyautogui.keyDown('ctrl')
        pyautogui.press('r')
        pyautogui.keyUp('ctrl')
        check_keywords(urls)

if __name__ == '__main__':
    main()