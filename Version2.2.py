from bs4 import BeautifulSoup
import requests
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

df1 = pd.DataFrame(columns=['Score', 'Serve Team', 'Set Score', 'Game Score'], index=range(0))
finaldf = pd.DataFrame(columns=['Score', 'Serve Team', 'Set Score', 'Game Score'], index=range(0))
finaldfarr = []
gameLinks = []

def URL(url):
    theURL = requests.get(str(url))
    htmlParser = BeautifulSoup(theURL.text,'html.parser')
    Sets(htmlParser, df1)

def Sets(htmlParser, dataframe):
    Opponent1 = 0
    Opponent2 = 0
    Set1 = htmlParser.find(id="set-1")
    Set2 = htmlParser.find(id="set-2")
    Set3 = htmlParser.find(id="set-3")
    Set4 = htmlParser.find(id="set-4")
    Set5 = htmlParser.find(id="set-5")
    if Set1:
        scoresAndServes = pd.read_html(str(Set1), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet1 = currentSet.append(dataframe, ignore_index=True)
        currentSet1.loc[:,["Set Score"]] = "00"
        currentSet1.dropna(subset=['Score'], inplace=True)
        currentSet1 = currentSet1.reset_index(drop=True)
        tempCount = currentSet1.shape[0] - 1
    else:
        return
    if Set2:
        lastItem = currentSet1.at[tempCount,'Score']
        x = lastItem.split("-")
        if int(x[0]) > int(x[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)
        scoresAndServes = pd.read_html(str(Set2), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet2 = currentSet1.append(currentSet, ignore_index=True)
        SetScore = currentSet2.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet2.loc[:,["Set Score"]] = SetScore
        currentSet2.dropna(subset=['Score'], inplace=True)
        currentSet2 = currentSet2.reset_index(drop=True)
        tempCount = currentSet2.shape[0] - 1
    if Set3:
        lastItem = currentSet2.at[tempCount,'Score']
        x = lastItem.split("-")
        if int(x[0]) > int(x[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)
        scoresAndServes = pd.read_html(str(Set3), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet3 = currentSet2.append(currentSet, ignore_index=True)
        SetScore = currentSet3.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet3.loc[:,["Set Score"]] = SetScore
        currentSet3.dropna(subset=['Score'], inplace=True)
        currentSet3 = currentSet3.reset_index(drop=True)
        tempCount = currentSet3.shape[0] - 1
    if Set4:
        lastItem = currentSet3.at[tempCount,'Score']
        x = lastItem.split("-")
        if int(x[0]) > int(x[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)
        scoresAndServes = pd.read_html(str(Set4), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet4 = currentSet3.append(currentSet, ignore_index=True)
        SetScore = currentSet4.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet4.loc[:,["Set Score"]] = SetScore
        currentSet4.dropna(subset=['Score'], inplace=True)
        currentSet4 = currentSet4.reset_index(drop=True)
        tempCount = currentSet4.shape[0] - 1
        currentSet3 = currentSet4 # IMPORTANT STEP!!!!
    else:
        lastItem = currentSet3.at[tempCount,'Set Score']
        if int(x[0]) > int(x[-1]):
            gameWinner = "Opponent1"
        else:
            gameWinner = "Opponent2"
        GameScore = currentSet3.loc[:,["Game Score"]]
        GameScore = GameScore.fillna(gameWinner)
        currentSet3.loc[:,["Game Score"]] = GameScore
        finaldfarr.append(currentSet3)
        print("still running")
        return
    if Set5:
        lastItem = currentSet4.at[tempCount,'Score']
        x = list(lastItem)
        if int(x[0]) > int(x[-1]):
            Opponent1 += 1
            winner = str(Opponent1) + str(Opponent2)
        else:
            Opponent2 += 1
            winner = str(Opponent1) + str(Opponent2)

        scoresAndServes = pd.read_html(str(Set5), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet5 = currentSet4.append(currentSet, ignore_index=True)
        SetScore = currentSet5.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet5.loc[:,["Set Score"]] = SetScore
        currentSet5.dropna(subset=['Score'], inplace=True)
        currentSet5 = currentSet5.reset_index(drop=True)
        tempCount = currentSet5.shape[0] - 1
    else:
        lastItem = currentSet4.at[tempCount,'Set Score']
        x = list(lastItem)
        if int(x[0]) > int(x[-1]):
            gameWinner = "Opponent1"
        else:
            gameWinner = "Opponent2"
        GameScore = currentSet4.loc[:,["Game Score"]]
        GameScore = GameScore.fillna(gameWinner)
        currentSet4.loc[:,["Game Score"]] = GameScore
        finaldfarr.append(currentSet4)
        print("still running")    
        return
    
    lastItem = currentSet5.at[tempCount,'Set Score']
    x = list(lastItem)
    if int(x[0]) > int(x[-1]):
        gameWinner = "Opponent1"
    else:
        gameWinner = "Opponent2"
    GameScore = currentSet5.loc[:,["Game Score"]]
    GameScore = GameScore.fillna(gameWinner)
    currentSet5.loc[:,["Game Score"]] = GameScore
    # currentSet3 = currentSet5 # IMPORTANT STEP!!!!
    finaldfarr.append(currentSet5)  
    print("still running")

# listOfYears = ["https://gohuskies.com/sports/womens-volleyball/schedule/2020", "https://gohuskies.com/sports/womens-volleyball/schedule/2019", 
#                 "https://gohuskies.com/sports/womens-volleyball/schedule/2018", "https://gohuskies.com/sports/womens-volleyball/schedule/2017", 
#                 "https://gohuskies.com/sports/womens-volleyball/schedule/2016" ]

listOfYears = ["https://pepperdinewaves.com/sports/womens-volleyball/schedule/2018", "https://pepperdinewaves.com/sports/womens-volleyball/schedule/2019", "https://pepperdinewaves.com/sports/womens-volleyball/schedule/2020-21"]
listOfYears = ["https://pepperdinewaves.com/sports/womens-volleyball/schedule/2018"]

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
    URL("https://pepperdinewaves.com" + str(i))

finaldf = finaldf.append(finaldfarr[0])
a = 0
for i in finaldfarr:
    tempdf = finaldfarr[a]
    finaldf = finaldf.append(tempdf, ignore_index=True)
    a+=1

# compression_opts = dict(method='zip',
#                         archive_name='VolleyballGameData_Master2.csv')  
# finaldf.to_csv('VolleyballGameData_Master2.zip', index=False,
#           compression=compression_opts)  
print("done done done done")