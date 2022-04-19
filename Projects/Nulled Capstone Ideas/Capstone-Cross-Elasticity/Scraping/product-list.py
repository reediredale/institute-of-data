
from bs4 import BeautifulSoup
HTMLFileToBeOpened = open("product-list-craft-beer.html", "r")
contents = HTMLFileToBeOpened.read()
beautifulSoupText = BeautifulSoup(contents, 'lxml')
print(beautifulSoupText.body.prettify())
# from requests_html import HTMLSession
# import pandas as pd
# url = 'product-list-craft-beer.html'
# s = HTMLSession()
# drinklist = []
# ​
# def request(url):
#     r = s.get(url)
#     r.html.render(sleep=1)
#     return r.html.xpath('//*[@class="product-list"]', first=True)
# ​
# def parse(products):
#     for item in products.absolute_links:
#         r = s.get(item)
#         name = r.html.find('div.product-detail-info-title', first=True).text
#         subtext = r.html.find('div.product-subtext', first=True).text
#         price = r.html.find('span.price', first=True).text
# ​
#         try:
#             rating = r.html.find('span.label-stars', first=True).text
#         except:
#             rating = 'none'
#         if r.html.find('div.add-to-cart-container'):
#             stock = 'in stock'
#         else:
#             stock = 'out of stock'
#         drink = {
#             'name': name,
#             'subtext': subtext,
#             'price': price,
#             'rating': rating,
#             'stock': stock
#         }
#         drinklist.append(drink)
# ​
# def output():
#     df = pd.DataFrame(drinklist)
#     df.to_csv('dans.csv', index=False)
#     print('Saved to CSV Files')
# ​
# products = request('product-list-craft-beer.html')
# parse(products)
# output()