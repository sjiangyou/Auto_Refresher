import pyautogui
import time
from bs4 import BeautifulSoup
import requests

def check_keywords():
    url = 'https://www.palmettopanthers.org'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
 
    urls = []
    links = 0
    for link in soup.find_all('a'):
        if(link.get('href')[:8] == 'https://'):
            links += 1
            print(link.get('href'))
    print(links)

check_keywords()