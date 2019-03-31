'''
Jeg har brugt denne fil til at importere data ind SQLite DB
'''

import urllib.request, json
from challenge.models import Product

#Henter data ind i en Dict
url = urllib.request.urlopen("https://www.unisport.dk/api/sample/")
data = json.loads(url.read())

#Kører Dict igennem og gemmer den data som skal bruges i DB
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
    #Konvertering af string til float, og udskiftning af , med .
    b.price = float(a['price'].replace(',','.'))    
    b.currency = a['currency']
    b.product_id = a['id']
    b.save()