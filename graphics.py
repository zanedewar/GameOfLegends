import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import streamlit as st
import getPlayers

#statsList = ['KDA:', 'CS per Minute:', 'Gold Per Minute:', 'Gold%:', 'Kill Participation:']

playerDict = {}
statsDict = {}
index = []
@st.cache_data
def init():
    for i, s in enumerate(getPlayers.statsList):
        statsDict[s] = []
    return statsDict, getPlayers.init()
    
def getStats(name):
    stats = getPlayers.getPlayer(name, playerDict[name])
    index.append(name)
    for i, s in enumerate(stats):
        statsDict[getPlayers.statsList[i]].append(s)
    df = pd.DataFrame(data=statsDict, index=index)
    return df

    

    
statsDict, playerDict = init()
names = st.multiselect(label='Player Select', options=playerDict.keys())
for i, name in enumerate(names):
    df = getStats(name)
    if i == len(names) - 1:
        st.dataframe(df)
        #st.bar_chart(df)
        
