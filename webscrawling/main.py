# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'}
#url ='https://www.purdue.edu/newsroom/archive.html'
url = 'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop'
req = requests.get(url, headers = headers)

soup =  BeautifulSoup(req.text, 'html.parser')
#print(soup)
player_info= soup.find_all('tr', class_=['odd', 'even'])
print(player_info[0])
print("the number of players is " + str(len(player_info)))

number = []
name = []
position = []
age = []
nation = []
team = []
value = []

for info in player_info:
    player = info.find_all('td')
    number.append(player[0].text)
    position.append(player[1].text)
    name.append(player[3].text)

print(number)
print(position)
print(name)
