import bs4
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import requests

url = 'https://shoponline.calgarycoop.com/crowfoot#/search?q=pharmacy'
response = requests.get(url)
bsobj = soup(response.content, 'html.parser')
product_cards = bsobj.find_all('single-product-card')

num = len(product_cards)
print(num)
print(response.status_code)

for card in product_cards:
    product_name = card.find('h2', class_='pc-title').text.strip()
    product_price = card.find('strong', class_='product-price').text.strip()
    product_image = card.find('img', class_='pc-image')['src']

print("hey")
