import bs4
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import requests

url = 'https://hpr-rps.hres.ca/pdl.php#a1'
response = requests.get(url)
bsobj = soup(response.content, 'html.parser')
product_cards = bsobj.find_all('div', {'id': 'wb-auto-1_wrapper'})

num = len(product_cards)
print(num)
print(response.status_code)


print("hey")
