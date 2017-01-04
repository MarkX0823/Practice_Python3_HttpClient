# C:\Users\User\AppData\Local\Programs\Python\Python35-32\python.exe
# -*- coding:utf-8 -*-

import urllib.request

urlTemp1 = "https://docs.google.com/"
urlTemp2 = "spreadsheets/d/"
urlTemp3 = "1b56-7EekWIOectUGbaU4bOuAsM2ot3scHdC7JzVxcCA/"
urlTemp4 = "htmlview?sle=true#"
url = urlTemp1 + urlTemp2 + urlTemp3 + urlTemp4
print(url)

htmlRaw = urllib.request.urlopen(url).read()
htmlStr = htmlRaw.decode("utf-8")

file = open('D:\Download\Concert.txt', 'w', encoding = 'UTF-8')
file.write(htmlStr)
file.close()

dataTableInHtmlStr = htmlStr[htmlStr.find("<table"):htmlStr.find("</table")]
file = open('D:\Download\ConcertTable.txt', 'w', encoding = 'UTF-8')
file.write(dataTableInHtmlStr)
file.close()

 
