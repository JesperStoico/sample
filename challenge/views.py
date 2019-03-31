'''
Generelt for mine views har jeg forsøgt og have så meget af min kode her i filen, frem for at have kode i mine
html filer
'''

import operator

from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from django.core.paginator import EmptyPage
from django.shortcuts import render
from challenge.models import Product

#View til simpel forside, med links til de andre views
def index(request):        
    return render(request, 'challenge/index.html')

#View til de 10 billigste produkter
def products(request):    
    data = Product.objects.order_by('price')[:10]
    return render(request, 'challenge/products.html', {'data': data})

#View til de 10 billigste børne produkter
def kids(request):
    data = Product.objects.order_by('price') & Product.objects.filter(kids=True)        
    return render(request, 'challenge/kids.html', {'data': data})

#View som viser produkt ud fra ID i URL
def id(request, product_id):
    data = Product.objects.filter(product_id=product_id)    
    return render(request, 'challenge/id.html', {'data':data})

def paging(request):
    data = Product.objects.all()
    #Sætter hvor mange varer vi ønsker pr. side
    paginator = Paginator(data, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)
    return render(request, 'challenge/paging.html', {'posts':posts})

