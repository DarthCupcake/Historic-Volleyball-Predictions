import numpy as np
import requests
import pandas as pd
from bs4 import BeautifulSoup

pd.set_option("display.max_rows", None, "display.max_columns", None)

finaldf = pd.DataFrame(columns=['Score', 'Serve Team', 'Set Score', 'Game Score'], index=range(0))
finaldfarr = []
gameLinks = []

def URL(url):
    # theURL = requests.get(str(url))
    htmlParser = BeautifulSoup(requests.get(str(url)).text,'html.parser')
    Sets(htmlParser)

def Sets(htmlParser):
    Opponent1, Opponent2 = 0, 0
    Set = htmlParser.find(id="set-1")
    if Set:
        currentSet2 = pd.read_html(str(Set), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = currentSet2.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet['Set Score'] = 00
        currentSet.dropna(subset=['Score'], inplace=True)
        currentSet = currentSet.reset_index(drop=True)
    else:
        return
    Set = htmlParser.find(id="set-2")
    if Set:
        lastItem = currentSet.at[currentSet.shape[0] - 1,'Score']
        comparableResult = lastItem.split("-")
        if int(comparableResult[0]) > int(comparableResult[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)
        currentSet2 = pd.read_html(str(Set), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet2 = currentSet2.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet2['Set Score'] = int(winner)
        currentSet = currentSet.append(currentSet2, ignore_index=True)
        currentSet.dropna(subset=['Score'], inplace=True)
        currentSet = currentSet.reset_index(drop=True)
    Set = htmlParser.find(id="set-3")
    if Set:
        lastItem = currentSet.at[currentSet.shape[0] - 1,'Score']
        comparableResult = lastItem.split("-")
        if int(comparableResult[0]) > int(comparableResult[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)
        currentSet2 = pd.read_html(str(Set), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet2 = currentSet2.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet2['Set Score'] = int(winner)
        currentSet = currentSet.append(currentSet2, ignore_index=True)
        currentSet.dropna(subset=['Score'], inplace=True)
        currentSet = currentSet.reset_index(drop=True)
    Set = htmlParser.find(id="set-4")    
    if Set:
        lastItem = currentSet.at[currentSet.shape[0] - 1,'Score']
        comparableResult = lastItem.split("-")
        if int(comparableResult[0]) > int(comparableResult[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)
        currentSet2 = pd.read_html(str(Set), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet2 = currentSet2.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet2['Set Score'] = int(winner)
        currentSet = currentSet.append(currentSet2, ignore_index=True)
        currentSet.dropna(subset=['Score'], inplace=True)
        currentSet = currentSet.reset_index(drop=True)
    else:
        lastItem = currentSet.at[currentSet.shape[0] - 1,'Set Score']
        comparableResult = list(lastItem)
        if int(comparableResult[0]) > int(comparableResult[-1]):
            currentSet['Game Score'] = True
        else:
            currentSet['Game Score'] = False
        finaldfarr.append(currentSet)
        print("still running")
        return
    Set = htmlParser.find(id="set-5")
    if Set:
        lastItem = currentSet.at[currentSet.shape[0] - 1,'Score']
        comparableResult = lastItem.split("-")
        if int(comparableResult[0]) > int(comparableResult[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)
        currentSet2 = pd.read_html(str(Set), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet2 = currentSet2.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet2['Set Score'] = int(winner)
        currentSet = currentSet.append(currentSet2, ignore_index=True)
        currentSet.dropna(subset=['Score'], inplace=True)
        currentSet = currentSet.reset_index(drop=True)
    else:
        lastItem = currentSet.at[currentSet.shape[0] - 1,'Set Score']
        comparableResult = list(lastItem)
        if int(comparableResult[0]) > int(comparableResult[-1]):
            currentSet['Game Score'] = True
        else:
            currentSet['Game Score'] = False
        finaldfarr.append(currentSet)
        print("still running")
        return

    lastItem = currentSet.at[currentSet.shape[0] - 1,'Set Score']
    x = list(lastItem)
    if int(x[0]) > int(x[-1]):
        currentSet['Game Score'] = True
    else:
        currentSet['Game Score'] = False
    finaldfarr.append(currentSet)  
    print("still running")

# listOfYears = ["https://gohuskies.com/sports/womens-volleyball/schedule/2020", 
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2019", 
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2018",                 # # WASH
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2017", 
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2016" ]

# listOfYears = ["https://pepperdinewaves.com/sports/womens-volleyball/schedule/2018", 
#               "https://pepperdinewaves.com/sports/womens-volleyball/schedule/2019",                               # # PEPPERDINE
#               "https://pepperdinewaves.com/sports/womens-volleyball/schedule/2020-21"]

listOfYears = ["https://pepperdinewaves.com/sports/womens-volleyball/schedule/2018"]                            # # PEPPERDINE

def GatherLinks(tableWithSites, gameLinks):
    for link in tableWithSites.find_all('a'):
        everyLink = link.get('href')
        if str(everyLink).__contains__("boxscore") and gameLinks.__contains__(everyLink) == False:
            gameLinks.append(everyLink)

for i in listOfYears:
    theURL = requests.get(i)
    soup = BeautifulSoup(theURL.text, 'html.parser')
    tableWithSites = soup.find(id="schedule-view-default")
    GatherLinks(tableWithSites, gameLinks)

for i in gameLinks:
    # print(i)
    URL("https://pepperdinewaves.com" + str(i))

finaldf = pd.concat(finaldfarr)
finaldf = finaldf.reset_index(drop=True)

# compression_opts = dict(method='zip',
#                         archive_name='VolleyballGameData_Master2.csv')  
# finaldf.to_csv('VolleyballGameData_Master2.zip', index=False,
#           compression=compression_opts)  
# print("done done done done")

print(finaldf)