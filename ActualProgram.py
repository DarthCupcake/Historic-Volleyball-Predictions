import pandas as pd

df1 = pd.read_csv("V-ballGameData_TrueMaster.csv")

score = input("Point Score: ")
setScore = input("Set Score: ")

flippedScore = score.split("-")
flippedScore = str(flippedScore[1]+"-"+flippedScore[0])

flippedSetScore = setScore [::-1]

totalDf = df1.loc[((df1['Score'] == score) & (df1['Set Score'] == int(setScore))) | ((df1['Score'] == flippedScore) & (df1['Set Score'] == int(flippedSetScore)))]
otherDf = totalDf.loc[(totalDf['Game Score'] == 'Opponent1') & ((totalDf['Score'] == score) & (totalDf['Set Score'] == int(setScore)))]
otherOtherDf = totalDf.loc[(totalDf['Game Score'] == 'Opponent2') & ((totalDf['Score'] == flippedScore) & (totalDf['Set Score'] == int(flippedSetScore)))]


print((otherDf.count()[0] + otherOtherDf.count()[0]) / totalDf.count()[0])
