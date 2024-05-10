import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import streamlit as st

#https://stackoverflow.com/questions/38489386/how-to-fix-403-forbidden-errors-when-calling-apis-using-python-requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
playerDict = {}
statsDict = {}
statsList = ['KDA:', 'CS per Minute:', 'Gold Per Minute:', 'Gold%:', 'Kill Participation:']
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
    return playerDict
def getPlayer(name, id):
    stats = [0,0,0,0,0]
    r = requests.get(f'https://gol.gg/players/player-stats/{id}/season-S14/split-Spring/tournament-ALL/champion-ALL/', headers=headers)
    s = r.text.split('\n')
    def check(checkString, statIndex, i):
        line = s[i]
        if checkString in line:
            out = ''
            for c in line:
                if ((ord(c) >= 48 and ord(c) <= 57) or c == '.'):
                   out += c
            try:
                float(out)
            except ValueError:
                return
            stats[statIndex] = float(out)

    for i in range(0, len(s)):
        for j in range(5):
            check(statsList[j], j, i)
    return stats

init()
'''print(playerDict)
print(playerDict['YellOwStaR'])'''
getPlayer('Faker', playerDict['Faker'])