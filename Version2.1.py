from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
import requests
import pandas as pd
import re

pd.set_option("display.max_rows", None, "display.max_columns", None)

df1 = pd.DataFrame(columns=['Score', 'Serve Team', 'Set Score', 'Game Score'], index=range(0))
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
        # tempDataFrame = pd.DataFrame(columns=['Score', 'Serve Team', 'Set Score', 'Game Score'], index=range(0))
        currentSet1 = currentSet.append(dataframe, ignore_index=True)
        currentSet1.loc[:,["Set Score"]] = "00"
        currentSet1.dropna(subset=['Score'], inplace=True)
        currentSet1 = currentSet1.reset_index(drop=True)
        tempCount = currentSet1.shape[0] - 1
    if Set2:
        lastItem = currentSet1.at[tempCount,'Score']
        # x = list(lastItem)
        x = lastItem.split("-")
        print(x)
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
        # x = list(lastItem)
        x = re.split(r'(\W+)', lastItem)
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
        # print(currentSet3)
        # print(tempCount)
        # print(str(lastItem))
        lastItem = currentSet3.at[tempCount,'Score']
        # x = list(lastItem)
        x = re.split(r'(\W+)', lastItem)
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
        # x = list(lastItem)
        if int(x[0]) > int(x[-1]):
            gameWinner = "Opponent1"
        else:
            gameWinner = "Opponent2"
        GameScore = currentSet3.loc[:,["Game Score"]]
        GameScore = GameScore.fillna(gameWinner)
        currentSet3.loc[:,["Game Score"]] = GameScore
        f = open("file.txt", "a")
        f.write(str(currentSet3))
        f.close()
        return
    if Set5:
        lastItem = currentSet4.at[tempCount,'Score']
        x = list(lastItem)
        #x = re.split(r'(\W+)', lastItem)
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
        f = open("file.txt", "a")
        f.write(str(currentSet3))
        f.close()
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
    currentSet3 = currentSet5 # IMPORTANT STEP!!!!
    
    f = open("file.txt", "a")
    f.write(str(currentSet3))
    f.close()

listOfYears = ["https://gohuskies.com/sports/womens-volleyball/schedule/2020", "https://gohuskies.com/sports/womens-volleyball/schedule/2019", 
                "https://gohuskies.com/sports/womens-volleyball/schedule/2018", "https://gohuskies.com/sports/womens-volleyball/schedule/2017", 
                "https://gohuskies.com/sports/womens-volleyball/schedule/2016" ]

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
    URL("https://gohuskies.com" + str(i))
    print(i)
# URL("https://gohuskies.com/sports/womens-volleyball/stats/2016/james-madison/boxscore/9667")
# URL("https://gohuskies.com/sports/womens-volleyball/stats/2019/san-diego/boxscore/16985")
# URL("https://gohuskies.com/sports/womens-volleyball/stats/2020/ucla/boxscore/19495")
# URL("https://gohuskies.com/sports/womens-volleyball/stats/2020/arizona-state/boxscore/19499")


print("YAY!! The program finished! :)")


































#### ATTEMPT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 

# theURL = requests.get("https://gohuskies.com/sports/womens-volleyball/schedule")
# soup = BeautifulSoup(theURL.text, 'html.parser')

# # f = open("file.txt", "w")
# # f.write(str(soup.prettify))
# # f.close()

# f = open("AllURLS", "r")
# # l = open("AllURLS", "w")
# # for line in f:
# #     if line.__contains__("<li class=\"sidearm-schedule-game-links-boxscore\">"):
# #         l.write(line)
# a = 0
# URLlist = []
# for i in f.read():
#     print(i)
#     if a % 2 == 0:
#         URLlist.append(i)
#         a+=1 
#     else:
#         a+=1 
#         continue
#     if a > 47:
#         break

# print(URLlist)


#### ATTEMPT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 