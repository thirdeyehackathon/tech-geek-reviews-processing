try:
    from bs4 import BeautifulSoup
except ImportError:
    from BeautifulSoup import BeautifulSoup
import urllib
import re

import os

#Generate the URL
site_source = 'http://www.flipkart.com/search?q='
print 'Enter the Product name:',
prod_name = raw_input()
prod_name = prod_name.lower()
search_page = site_source + prod_name + '&otracker=start&as-show=on&as=off'
print ('Search Link: ' + search_page)
#Open the Search page
Soup_URL = urllib.urlopen(search_page).read()
soup = BeautifulSoup(Soup_URL,'html.parser')

#Print Search page info
prod_links = []
for link in soup.find_all('a', class_='pu-image fk-product-thumb '):
   plink = str(link.get('href'))
   prod_links.append(plink)

#get all the Product names
prod_names = []
for link1 in soup.find_all('a', class_='fk-display-block'):
	pnames = str(link1.get('title'))
	prod_names.append(pnames)
value = 'None'
while value in prod_names:
	prod_names.remove(value)

#Display Search Result Prdoucts
for x in range(len(prod_names)):
	print str(x).center(20, '-')
	print prod_names[x]
	
#Get the Product
print ''
print 'Enter the Product number:',
prod = int(raw_input())
sel_prod = prod_links[prod]
sel_prod = 'http://www.flipkart.com' + sel_prod
print ('Product Link: ' + sel_prod)

#Open the Product page
Soup_URL2 = urllib.urlopen(sel_prod).read()
soup2 = BeautifulSoup(Soup_URL2,'html.parser')
#print soup2.prettify('utf-8')

#Details about the product
star_box = []
print ''
print str(soup2.title.string)
for link2 in soup2.find_all('div', class_='progress'):
	star_box.append(link2.getText())
star_box.reverse()
for z in range(0,5):
	print (str(z+1) + ' Star: ' + str(star_box[z]))
	
#Get the Reviews
review_block = []
for link3 in soup.find_all('span', class_='review-text-short'):
   ptext = link3.getText()
   print ptext
   review_block.append(ptext)
print review_block

