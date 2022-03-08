import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

jumiaURL = "https://www.jumia.com.ng"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

k = requests.get('https://www.jumia.com.ng/catalog/?q=phones').text
soup=BeautifulSoup(k,'html.parser')
productlist = soup.find_all("article",{"class":"_fb"})
# lis = soup.find_all("article")
productlist
# lis

products = soup.find_all("h3", {"class": "name"})
prices = soup.find_all("div", {"class": "prc"})

for product, price in zip(products, prices):

    name_of_phone = productlist.text.ljust(100)
    price = prices.text.replace("₦", "").replace(",","").strip()
    # print(product.text.ljust(100), price.text.replace("#", " ").replace(","," ").strip())

    # print(name, price)
    print(f"insert into iphones (name_of_phone, price) values('{name_of_phone}', '{price}')")