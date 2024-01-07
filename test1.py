import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import csv

html = urlopen('https://en.wikipedia.org/wiki/list_of_largest_recorded_music_markets')
bsobj = soup(html.read(), "html.parser")
tbody = bsobj('table', {'class':"wikitable plainrowheaders sortable"})[0].findAll('tr')
xl = []
for row in tbody:
    cols = row.findChildren(recursive = False)
    cols = tuple(element.text.strip().replace("%","") for element in cols)
    xl.append(cols)
xl = xl[1:-1]
print(xl)