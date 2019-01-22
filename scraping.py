import requests
import re
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('https://www.newegg.ca/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+card&N=-1&isNodeId=1')

soup = BeautifulSoup(response.text, 'html.parser')
containers = soup.find_all("div",{"class":"item-container"})


brands = soup.find_all("a", {"class":"item-brand"})

titles = soup.find_all("a", {"class":"item-title"})
price_ship = soup.find_all("li", {"class":"price-ship"})


brandlist = []
for brand in brands:
	print(brand.img["title"])	
	brandlist.append(brand.img["title"])

print(brandlist)


titlelist = []
for title in titles:
	print(title.text.strip())
	titlelist.append(title.text.strip())
print(titlelist)


shiplist = []
for ship in price_ship:
	print(ship.text.strip())
	shiplist.append(ship.text.strip())
print(shiplist)


print(brandlist[0], shiplist[0])




