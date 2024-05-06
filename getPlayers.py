import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession

#https://stackoverflow.com/questions/38489386/how-to-fix-403-forbidden-errors-when-calling-apis-using-python-requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
playerDict = {}
def init():
    r = requests.get('https://gol.gg/players/list/season-S14/split-Spring/tournament-ALL/', headers=headers)
    #print(r.text)
    #nameList = r.text.split('}')
    i = r.text.find('class:\'player\'')
    text = r.text[i:]
    textList = text.split(',')
    stop = len(textList)
    for i in range(0, stop, 3):
        firstQ = textList[i+1].find('\'')
        secondQ = firstQ + textList[i+1][firstQ+1:].find('\'')
        index = textList[i+1][firstQ+3:secondQ+1]
        
        if(ord(index[0]) < 48 or ord(index[0]) > 57):
            break

        firstQ = textList[i+2].find('\'')
        secondQ = firstQ + textList[i+2].find('-')
        name = textList[i+2][firstQ+1:secondQ-7]
        playerDict[name] = index

init()
print(playerDict)
print(playerDict['YellOwStaR'])