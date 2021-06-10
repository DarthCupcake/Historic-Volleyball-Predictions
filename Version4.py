import requests
import pandas as pd
from bs4 import BeautifulSoup
import timeit
import numpy as np
import threading

# pd.set_option("display.max_rows", None, "display.max_columns", None)

start = timeit.default_timer()

finaldfarr = []
gameLinks = []
listOfYears = ["https://pepperdinewaves.com/sports/womens-volleyball/schedule/2018"]

def URL(url):
    theURL = requests.get(str(url))
    htmlParser = BeautifulSoup(theURL.text,'html.parser')
    return htmlParser

def findingSet(htmlParser, id):
    Set = htmlParser.find(id=id)
    return Set

def editingDataFrameOther(currentSet, Set, id, Opponent1, Opponent2):
    if id == "set-1":
        currentSet = pd.read_html(str(Set), header=0) [0]
        currentSet = currentSet.loc[:,["Score", "Serve Team"]] 
        currentSet['Set Score'] = 00
        return currentSet  

    lastItem = currentSet.at[currentSet.shape[0] - 1,'Score']
    x = lastItem.split("-")
    if int(x[0]) > int(x[-1]):
        Opponent1 += 1
        winner = str(Opponent1) + str(Opponent2)
    else:
        Opponent2 += 1
        winner = str(Opponent1) + str(Opponent2)
    currentSet2 = pd.read_html(str(Set), header=0) [0]
    currentSet2 = currentSet2.loc[:,["Score", "Serve Team"]]
    currentSet2['Set Score'] = int(winner)
    currentSet = currentSet.append(currentSet2, ignore_index=True)
    return [currentSet, Opponent1, Opponent2]

def gameWinner(currentSet):
    lastItem = currentSet.at[currentSet.shape[0] - 1,'Set Score']
    x = list(str(lastItem))
    if int(x[0]) > int(x[-1]):
        currentSet['Game Score'] = True
    else:
        currentSet['Game Score'] = False
    finaldfarr.append(currentSet)  
    print("done with a game")

def cleanUp(currSet):
    currSet.dropna(subset=['Score'], inplace=True)
    currSet = currSet.reset_index(drop=True)
    return currSet

def GatherLinks(tableWithSites, gameLinks):
    for link in tableWithSites.find_all('a'):
        everyLink = link.get('href')
        if str(everyLink).__contains__("boxscore") and gameLinks.__contains__(everyLink) == False:
            gameLinks.append(everyLink)

def main():
    for i in listOfYears:
        theURL = requests.get(i)
        soup = BeautifulSoup(theURL.text, 'html.parser')
        tableWithSites = soup.find(id="schedule-view-default")
        GatherLinks(tableWithSites, gameLinks)
        # print(gameLinks)
    for i in gameLinks:
        Opponent1, Opponent2 = 0, 0
        currLink = URL("https://pepperdinewaves.com" + str(i))
        id = "set-1"
        Set = findingSet(currLink, id)
        if Set:
            currSet = editingDataFrameOther(Set, Set, id, Opponent1, Opponent2)
            currSet = cleanUp(currSet)
        else:
            continue
        id = "set-2"
        Set = findingSet(currLink, id)
        data = editingDataFrameOther(currSet, Set, id, Opponent1, Opponent2)
        Opponent1 = data[1]
        Opponent2 = data[2]
        currSet = data[0]
        currSet = cleanUp(currSet)
        id = "set-3"
        Set = findingSet(currLink, id)
        data = editingDataFrameOther(currSet, Set, id, Opponent1, Opponent2)
        Opponent1 = data[1]
        Opponent2 = data[2]
        currSet = data[0]
        currSet = cleanUp(currSet)
        id = "set-4"
        Set = findingSet(currLink, id)
        if Set:
            data = editingDataFrameOther(currSet, Set, id, Opponent1, Opponent2)
            Opponent1 = data[1]
            Opponent2 = data[2]
            currSet = data[0]
            currSet = cleanUp(currSet)
        else:
            gameWinner(currSet)
            continue
        id = "set-5"
        Set = findingSet(currLink, id)
        if Set:
            data = editingDataFrameOther(currSet, Set, id, Opponent1, Opponent2)
            Opponent1 = data[1]
            Opponent2 = data[2]
            currSet = data[0]
            currSet = cleanUp(currSet)
        else:
            gameWinner(currSet)
            continue

        gameWinner(currSet)     


if __name__=="__main__":
    main()





finaldf = pd.concat(finaldfarr)
finaldf = finaldf.reset_index(drop=True)

# finaldf.to_csv(r'C:\Users\srikardevarakonda\Downloads\VballStuff.csv', index = False, header=True)

stop = timeit.default_timer()

print('Time: ', stop - start)  