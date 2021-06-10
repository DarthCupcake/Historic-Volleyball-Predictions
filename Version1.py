from bs4 import BeautifulSoup
import requests
import pandas as pd
# from IPython.display import display_html
# from openpyxl.workbook import Workbook
# from openpyxl import load_workbook
import re
import numpy

pd.set_option("display.max_rows", None, "display.max_columns", None)

# washingtonSetScore = 0
# opponentSetScore = 0

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
        scoresAndServes = pd.read_html(str(Set1), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        Navigation(currentSet)
    if Set2:
        scoresAndServes = pd.read_html(str(Set2), header=0) [0]
    if Set3:
        scoresAndServes = pd.read_html(str(Set3), header=0) [0]
    if Set4:
        scoresAndServes = pd.read_html(str(Set4), header=0) [0]
    if Set5:
        scoresAndServes = pd.read_html(str(Set5), header=0) [0]

def Navigation(currentSet):
    # for i, row in currentSet.iterrows(): # Creation of array of tuples with the currentSet 
    #     scores.append(f"{row['Score'], row['Serve Team']}")
        # scores.append(row)
    #     temp = scores[-1] #isolating the last score
    # dfToArray = currentSet.values # Converting the currentSet to a numpy array
    subset = currentSet[['Score', 'Serve Team']]
    tuples = [tuple(x) for x in subset.values]
    y = WhoWonTheSet(tuples[-1])
    otherArray = [] # array for appending the set score, and the winner of the game
    for item in tuples:
        theItem = list(item)
        theItem.append(y)
        item = tuple(theItem)
        otherArray.append(item)
    # print(otherArray)
    # # dfToArray = numpy.array(currentSet)
    # # for j in dfToArray:
    # #     numpy.append("0-0")
    # numpy.insert(dfToArray, 1, "0-0")
    # numpy.insert(dfToArray, 1, "0-0", axis=1)
    # print(dfToArray)

def WhoWonTheSet(lastScore): 
    washingtonSetScore = 0
    opponentSetScore = 0
    finalPointScore = lastScore[0]
    x = re.split(r'(\W+)', finalPointScore)
    if int(x[0]) > int(x[-1]):
        # washingtonSetScore += 1 
        # washingtonCount = SetScoreCounterWash(washingtonSetScore)
        return int(str(washingtonSetScore) + str(opponentSetScore))
        # return washingtonCount
    elif int(x[0]) > int(x[-1]):
        # opponentSetScore += 1
        opponentCount = opponentSetScore + 1
        # return str(washingtonSetScore) + str(opponentSetScore)
        return opponentCount

def something():
    h = 0
    if 1 == 1:
        h += 1
        f = h
    if f == 1:
        print("hey")

    
# def SetScoreCounterWash(washingtonSetScore):
#     washingtonSetScore += 1
#     if 1 == 1:
#         contain += 1
#     container = washingtonSetScore
#     return washingtonSetScore




scores = []

URL("https://gohuskies.com/sports/womens-volleyball/stats/2016/james-madison/boxscore/9667")

print("YAY!! The program finished! :)")

# print(scores)