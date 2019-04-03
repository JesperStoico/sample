'''

Import script for importing the data from the sample site, into a Dict and from the Dict into the DB

'''

import urllib.request, json
from challenge.models import Product

#Importing data into a Dict
url = urllib.request.urlopen("https://www.unisport.dk/api/sample/")
data = json.loads(url.read())

# Looping through Dict to save the data in the DB
for a in data['products']:
    
    b = Product()
    
    if a['kids'] == "1":
        b.kids = True
    else:
        b.kids = False

    if a['kid_adult'] == "1":
        b.kid_adult = True
    else:
        b.kid_adult = False 

    b.name = a['name']
    # Converting the price string to a float and replacing , with . to converting it to a code readable number
    b.price = float(a['price'].replace(',','.'))    
    b.currency = a['currency']
    b.product_id = a['id']
    b.save()