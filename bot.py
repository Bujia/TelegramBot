#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: guobujia
"""
import telepot
import feedparser
from datetime import datetime

url = "http://horriblesubs.info/rss.php?res=720"  
token = "insert token here"
chat = "insert chatnumber here"
bot = telepot.Bot(token)


feed = feedparser.parse(url)
feed_entries = feed.entries

today = datetime.today().day
#f-formating
today_match = f', {today}'
for entry in feed_entries:
    #checking only todays new releases
     if today_match in entry["published"]:
         sentence = entry.title
         #remocing useless words from string
         words = sentence.replace(" [720p].mkv", "")
         anime = words.replace("[HorribleSubs] ", "")
         message = "Check out todays new episodes!\n" + anime
         print(message)
         #printing the message to telegram
         #bot.sendMessage(chat, message)
         
url1 = "http://fanfox.net/manga/onepunch_man/"
#Fetching the source code
source_code = requests.get(url1).text
soup = BeautifulSoup(source_code, "html.parser")
#Finding the latest chapter
table = soup.find("div", {"class": "detail-main-list-main"}).findAll("p")
manga_match = datetime.datetime.strftime(datetime.datetime.now()," %b %d, %Y")
print(manga_match)
for element in table:
    print(element.text)
