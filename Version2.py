from bs4 import BeautifulSoup
# from pandas.core.frame import DataFrame
import requests
import pandas as pd
import re
import time


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("Press Enter to start")
start_time = time.time()
pd.set_option("display.max_rows", None, "display.max_columns", None)

df1 = pd.DataFrame(columns=['Score', 'Serve Team', 'Set Score', 'Game Score'], index=range(0))

def URL(url):
    theURL = requests.get(str(url))
    htmlParser = BeautifulSoup(theURL.text,'html.parser')
    Sets(htmlParser, df1)

def Sets(htmlParser, dataframe):
    WashSetScore = 0
    OpponentSetScore = 0
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
        tempCount = currentSet1.shape[0] - 1
    if Set2:
        lastItem = currentSet1.at[tempCount,'Score']
        x = re.split(r'(\W+)', lastItem)
        if int(x[0]) > int(x[-1]):
            WashSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        else:
            OpponentSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        scoresAndServes = pd.read_html(str(Set2), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet2 = currentSet1.append(currentSet, ignore_index=True)
        SetScore = currentSet2.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet2.loc[:,["Set Score"]] = SetScore
        tempCount = currentSet2.shape[0] - 1
    if Set3:
        lastItem = currentSet2.at[tempCount,'Score']
        x = re.split(r'(\W+)', lastItem)
        if int(x[0]) > int(x[-1]):
            WashSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        else:
            OpponentSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        scoresAndServes = pd.read_html(str(Set3), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet3 = currentSet2.append(currentSet, ignore_index=True)
        SetScore = currentSet3.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet3.loc[:,["Set Score"]] = SetScore
        tempCount = currentSet3.shape[0] - 1
    if Set4:
        lastItem = currentSet3.at[tempCount,'Score']
        x = re.split(r'(\W+)', lastItem)
        if int(x[0]) > int(x[-1]):
            WashSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        else:
            OpponentSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        scoresAndServes = pd.read_html(str(Set4), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet4 = currentSet3.append(currentSet, ignore_index=True)
        SetScore = currentSet4.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet4.loc[:,["Set Score"]] = SetScore
        tempCount = currentSet4.shape[0] - 1
        currentSet3 = currentSet4 # IMPORTANT STEP!!!!
    else:
        lastItem = currentSet3.at[tempCount,'Set Score']
        x = list(lastItem)
        if int(x[0]) > int(x[-1]):
            gameWinner = "Washington"
        else:
            gameWinner = "Opponent"
        GameScore = currentSet3.loc[:,["Game Score"]]
        GameScore = GameScore.fillna(gameWinner)
        currentSet3.loc[:,["Game Score"]] = GameScore
        f = open("file.txt", "w")
        f.write(str(currentSet3))
        f.close()
        return
    if Set5:
        lastItem = currentSet4.at[tempCount,'Score']
        x = re.split(r'(\W+)', lastItem)
        if int(x[0]) > int(x[-1]):
            WashSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        else:
            OpponentSetScore += 1
            winner = str(WashSetScore) + str(OpponentSetScore)
        scoresAndServes = pd.read_html(str(Set5), header=0) [0] #scoresAndServes is the entire dataframe of the Set
        currentSet = scoresAndServes.loc[:,["Score", "Serve Team"]] #currentSet is the dataframe
        currentSet5 = currentSet4.append(currentSet, ignore_index=True)
        SetScore = currentSet5.loc[:,["Set Score"]]
        SetScore = SetScore.fillna(winner)
        currentSet5.loc[:,["Set Score"]] = SetScore
        tempCount = currentSet5.shape[0] - 1 # Is it necessary?
    else:
        lastItem = currentSet4.at[tempCount,'Set Score']
        x = list(lastItem)
        if int(x[0]) > int(x[-1]):
            gameWinner = "Washington"
        else:
            gameWinner = "Opponent"
        GameScore = currentSet4.loc[:,["Game Score"]]
        GameScore = GameScore.fillna(gameWinner)
        currentSet4.loc[:,["Game Score"]] = GameScore
        f = open("file.txt", "w")
        f.write(str(currentSet3))
        f.close()
        return
    
    lastItem = currentSet5.at[tempCount,'Set Score']
    x = list(lastItem)
    if int(x[0]) > int(x[-1]):
        gameWinner = "Washington"
    else:
        gameWinner = "Opponent"
    GameScore = currentSet5.loc[:,["Game Score"]]
    GameScore = GameScore.fillna(gameWinner)
    currentSet5.loc[:,["Game Score"]] = GameScore
    currentSet3 = currentSet5 # IMPORTANT STEP!!!!
    
    f = open("file.txt", "w")
    f.write(str(currentSet3))
    f.close()

# URL("https://gohuskies.com/sports/womens-volleyball/stats/2016/james-madison/boxscore/9667")
# URL("https://gohuskies.com/sports/womens-volleyball/stats/2019/san-diego/boxscore/16985")
# URL("https://gohuskies.com/sports/womens-volleyball/stats/2020/ucla/boxscore/19495")
URL("https://gohuskies.com/sports/womens-volleyball/stats/2019/hawai-i/boxscore/16986")


print("YAY!! The program finished! :)")

input("Press Enter to stop")
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)