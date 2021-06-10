# import requests
import requests
from bs4 import BeautifulSoup
import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import re

# from requests.models import guess_filename

# # listOfYears = ["https://gohuskies.com/sports/womens-volleyball/schedule/2020", "https://gohuskies.com/sports/womens-volleyball/schedule/2019", 
# #                 "https://gohuskies.com/sports/womens-volleyball/schedule/2018", "https://gohuskies.com/sports/womens-volleyball/schedule/2017", 
# #                 "https://gohuskies.com/sports/womens-volleyball/schedule/2016" ]

# # # f = open("AllURLS", "a")

# # a = 0

# # gameURLList = []
# # temp = []

# # f = open("AllURLS", "a")

# # for link in listOfYears:
# #     theURL = requests.get(link)
# #     soup = BeautifulSoup(theURL.text, 'html.parser')
# #     f.write(str(soup.prettify))

# #     # l = open("AllURLS", "w")
# # f.close()

# # f = open("AllURLS", "r")
# # # print(f.readlines())
# # g = f.readlines()
# # for line in g:
# #     if line.__contains__("<li class=\"sidearm-schedule-game-links-boxscore\">"):
# #         print(line)
# #         temp.append(line)

# # with open("AllURLS", "w") as w:
# #     for item in temp:
# #         w.write(item)
# # # print(temp)

# # f.close()
# #     # for i in f.readlines():
# #     #     print(i)
# #     #     if a % 2 == 0:
# #     #         gameURLList.append(i)
# #     #         a+=1 
# #     #     else:
# #     #         a+=1 
# #     #         continue
# #     #     if a > 47:
# #     #         break

# file = open("AllURLS", "r")
# arrForStuff = []
# a = 0
# for line in file.readlines():
#     if a % 2 == 0:
#         splitTag = line.split("\"")
#         arrForStuff.append(splitTag[-2])

# file.close()
# a = 0
# file = open("AllURLS", "w")
# for item in arrForStuff:
#     if a % 2 == 0:
#         file.write(item)
#     a+=1 
# file.close()

# theURL = requests.get("https://gohuskies.com/sports/womens-volleyball/schedule/2020")

# table_MN = pd.read_html(theURL.text)

# print(len(table_MN))

theURL = requests.get("https://gohuskies.com/sports/womens-volleyball/schedule/2020")
soup = BeautifulSoup(theURL.text, 'html.parser')
a = 0
h = soup.find(id="schedule-view-default")

gameLinks = []

for link in h.find_all('a'):
    everyLink = link.get('href')
    if str(everyLink).__contains__("boxscore") and gameLinks.__contains__(everyLink) == False:
        gameLinks.append(everyLink)

print(gameLinks)

