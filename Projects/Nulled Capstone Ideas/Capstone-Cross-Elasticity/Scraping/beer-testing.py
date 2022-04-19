from requests_html import HTMLSession
import pandas as pd

url = 'https://bws.com.au/beer/craft-beer'
s = HTMLSession()
drinklist = []

def request(url):
    r = s.get(url)
    r.html.render(sleep=4)
    return r.html.xpath('//*[@class="row-card-list"]', first=True)

def parse(products):
    for item in products.absolute_links:
        r = s.get(item)
        name = r.html.find('h2.productTile_brand', first=True).text
        subtext = r.html.find('div.productTile_name', first=True).text
        price = r.html.find('div.productTile_price', first=True).text

        try:
            rating = r.html.find('div.productTile_rating', first=True).text
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
    df.to_csv('bws.csv', index=False)
    print('Saved to CSV Files')

products = request('https://bws.com.au/beer/craft-beer')
parse(products)
output()