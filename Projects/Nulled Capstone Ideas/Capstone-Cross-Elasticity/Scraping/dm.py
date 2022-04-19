from bs4 import BeautifulSoup
from requests_html import HTMLSession
import regex as re
import pandas as pd

HTMLFileToBeOpened = open("product-list-craft-beer.html", "r")
contents = HTMLFileToBeOpened.read()
html_content = contents
 
# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

s = HTMLSession()
drinklist = []

def request(soup):
    r = s.get(soup)
    r.html.render(sleep=6)
    return r.html.xpath('//*[@class="product-list"]', first=True)

def parse(products):
    for item in products.absolute_links:
        r = s.get(item)
        name = r.html.find('span.title', first=True).text
        subtext = r.html.find('span.subtitle', first=True).text
        price = r.html.find('span.price-container', first=True).text

        try:
            rating = r.html.find('a.no-of-reviews', first=True).text
        except:
            rating = 'none'
        if r.html.find('div.add-to-cart-container'):
            stock = 'in stock'
        else:
            stock = 'out of stock'
        drink = {
            'name': name,
            'subtext': subtext,
            'price': price,
            'rating': rating,
            'stock': stock
        }
        drinklist.append(drink)

def output():
    df = pd.DataFrame(drinklist)
    df.to_csv('dm-beer.csv', index=False)
    print('Saved to CSV Files')

products = request(soup)
parse(products)
output()