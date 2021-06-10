from bs4 import BeautifulSoup
import requests
import pandas as pd
from IPython.display import display_html
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import re

pd.set_option("display.max_rows", None, "display.max_columns", None)

def URL(url):
    theURL = requests.get(str(url))
    htmlParser = BeautifulSoup(theURL.text,'html.parser')
    Sets(htmlParser)

def Sets(htmlParser):
    Set1 = htmlParser.find(id="set-1")
    Set2 = htmlParser.find(id="set-2")
    Set3 = htmlParser.find(id="set-3")
    Set4 = htmlParser.find(id="set-4")
    Set5 = htmlParser.find(id="set-5")
    if Set1:
        scoresAndServes = pd.read_html(str(Set1), header=0) [0]
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]]
        Navigation(currentSet)
    # if Set2:
    #     scoresAndServes = pd.read_html(str(Set2), header=0) [0]
    #     currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]]
    #     Navigation(currentSet)
    # if Set3:
    #     scoresAndServes = pd.read_html(str(Set3), header=0) [0]
    #     currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]]
    #     Navigation(currentSet)
    # if Set4:
    #     scoresAndServes = pd.read_html(str(Set4), header=0) [0]
    #     currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]]
    #     Navigation(currentSet)
    # if Set5:
    #     scoresAndServes = pd.read_html(str(Set5), header=0) [0]
    #     currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]]
    #     Navigation(currentSet)

def Navigation(currentSet):
    for i, row in currentSet.iterrows():
        scores.append(f"{row['Score'], row['Serve Team']}")
    Summary(scores[-1])

def whoWon():


def Summary(theFinalScore):
    print(theFinalScore[2], theFinalScore[3], theFinalScore[5], theFinalScore[6])
    if int(theFinalScore[2]) > int(theFinalScore[5]):
        summaryDictionary["Washington SetScore"] = 1
    elif int(theFinalScore[5]) > int(theFinalScore[2]):
        summaryDictionary["Opponent SetScore"] = 1
    elif int(theFinalScore[2]) == int(theFinalScore[5]) and 
        summaryDictionary.__setitem__("Opponent SetScore", 0)


scores = []
summaryDictionary = {
    "Washington SetScore" : 0,
    "Opponent SetScore" : 0
}

URL("https://gohuskies.com/sports/womens-volleyball/stats/2016/james-madison/boxscore/9667")
# scoresAndServes = pd.read_html(str(Set1), header=0) [0]
# scores.append(scoresAndServes.loc[:,["Score", "Serve Team"]])

# print(scores)
print("YAY!! The program finished! :)")
print(summaryDictionary)