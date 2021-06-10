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
# listOfYears = ["https://gohuskies.com/sports/womens-volleyball/schedule/2020", 
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2019", 
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2018",                 # # WASH
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2017", 
#               "https://gohuskies.com/sports/womens-volleyball/schedule/2016"]

listOfYears = ["https://pepperdinewaves.com/sports/womens-volleyball/schedule/2018", 
              "https://pepperdinewaves.com/sports/womens-volleyball/schedule/2019",                               # # PEPPERDINE
              "https://pepperdinewaves.com/sports/womens-volleyball/schedule/2020-21"] 

# listOfYears = ["https://pepperdinewaves.com/sports/womens-volleyball/schedule/2018"]                            # # PEPPERDINE

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

def main2(gameLinks):
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


def requestingYearLinks(year):
    theURL = requests.get(year)
    soup = BeautifulSoup(theURL.text, 'html.parser')
    tableWithSites = soup.find(id="schedule-view-default")
    GatherLinks(tableWithSites, gameLinks)


def main():
    yearScraping1 = threading.Thread(target=requestingYearLinks, args=(listOfYears[0],))
    yearScraping1.start()

    yearScraping2 = threading.Thread(target=requestingYearLinks, args=(listOfYears[1],))
    yearScraping2.start()

    yearScraping3 = threading.Thread(target=requestingYearLinks, args=(listOfYears[2],))
    yearScraping3.start()

    # yearScraping4 = threading.Thread(target=requestingYearLinks, args=(listOfYears[3],))
    # yearScraping4.start()

    # yearScraping5 = threading.Thread(target=requestingYearLinks, args=(listOfYears[4],))
    # yearScraping5.start()

    yearScraping1.join()
    yearScraping2.join()
    yearScraping3.join()
    #yearScraping4.join()
    # yearScraping5.join()

    splitArr = np.split(gameLinks,[len(gameLinks)//4, len(gameLinks)//2, (len(gameLinks)//4 *3)])

    mainProgramt1 = threading.Thread(target=main2, args=(splitArr[0],))
    mainProgramt1.start()   

    mainProgramt2 = threading.Thread(target=main2, args=(splitArr[1],))
    mainProgramt2.start()

    mainProgramt3 = threading.Thread(target=main2, args=(splitArr[2],))
    mainProgramt3.start()

    mainProgramt4 = threading.Thread(target=main2, args=(splitArr[3],))
    mainProgramt4.start()

    mainProgramt1.join()
    mainProgramt2.join()
    mainProgramt3.join()
    mainProgramt4.join()


if __name__=="__main__":
    main()





finaldf = pd.concat(finaldfarr)
finaldf = finaldf.reset_index(drop=True)

# finaldf.to_csv(r'C:\Users\srikardevarakonda\Downloads\VballStuff.csv', index = False, header=True)

stop = timeit.default_timer()
print(finaldf)

print('Time: ', stop - start)  