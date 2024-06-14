import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup as bs
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
    #st.write(statsDict)
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
        df.rename(columns={'Damage Per Minute': 'DPM'},inplace=True)
        st.dataframe(df)
        #st.bar_chart(df)
xAxis = st.selectbox("X-Axis",getPlayers.statsList,index=None,placeholder='X-Axis')
yList = []
for i in getPlayers.statsList:
    if i == xAxis:
        continue
    yList.append(i)
yAxis = st.selectbox("Y-Axis",yList,index=None,placeholder='Y-Axis')
rows = {0: xAxis, 1: yAxis}
#colors = [(np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))]
if xAxis and yAxis:
    chartData = pd.DataFrame([statsDict[xAxis],statsDict[yAxis]],columns=names)
    chartData = chartData.rename(index=rows)
    chartData = chartData.T
    fig, ax = plt.subplots()
    ax.plot(statsDict[xAxis],statsDict[yAxis],'ko')
    for i, xy in enumerate(zip(statsDict[xAxis],statsDict[yAxis])):
        ax.annotate(names[i],xy=xy,textcoords='offset pixels',xytext=(7,7))
    ax.set(xlabel=xAxis,ylabel=yAxis)
    #plt.plot(statsDict[xAxis])
    #st.write(chartData)
    #plt.show()
    
    
    #st.scatter_chart(data=chartData,x=xAxis,y=yAxis)
    st.pyplot(fig)
    #test