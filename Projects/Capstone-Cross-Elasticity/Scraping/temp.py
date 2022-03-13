import os
from bs4 import BeautifulSoup as soup
phone = [] # A list to store all the phone
path = 'product-list-craft-beer.html' # This is your folder name which stores all your html 
#be careful that you might need to put a full path such as C:\Users\Niche\Desktop\htmlfolder 
for filename in os.listdir(path): #Read files from your path
     #Here we are trying to find the full pathname
     for x in filename: #We will have A-H stored as path
           subpath = os.path.join(path, filename) 
           for filename in os.listdir(subpath):
           #Getting the full path of a particular html file
                fullpath = os.path.join(subpath, filename)
                #If we have html tag, then read it
                if fullpath.endswith('.html'): continue
                #Then we will run beautifulsoup to extract the contents
                    soup = BeautifulSoup(open(fullpath), 'lxml')
                    #Then run your code
                    # grabs each field
                    contactname = page_soup.findAll("td", {"itemprop": "name"})
                    contactstreetaddress = page_soup.findAll("td", {"itemprop": "streetAddress"})
                    contactpostalcode = page_soup.findAll("td", {"itemprop": "postalCode"})
                    contactaddressregion = page_soup.findAll("td", {"itemprop": "addressRegion"})
                    contactaddresscountry = page_soup.findAll("td", {"itemprop": "addressCountry"})
                    contactfax = page_soup.findAll("td", {"itemprop": "faxNumber"})
                    contactemail = page_soup.findAll("td", {"itemprop": "email"})
                    contactphone = page_soup.findAll("td", {"itemprop": "telephone"})
                    contacturl = page_soup.findAll("a", {"itemprop": "url"})
                    #Outputs as text without tags
                    Company = contactname[0].text
                    Address = contactstreetaddress[0].text
                    Zip = contactpostalcode[0].text
                    Region = contactaddressregion[0].text
                    Country = contactaddresscountry[0].text
                    Fax = contactfax[0].text
                    Email = contactemail[0].text
                    Phone = contactphone[0].text
                    URL = contacturl[0].text
                    #Here you might want to consider using dictionary or a list
                    #For example append Phone to list call phone
                    phone.append(Phone)