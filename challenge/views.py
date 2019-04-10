# I have tried to keep my code for my views in this file, so I have a minimum of code in my html files.


from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from django.core.paginator import EmptyPage
from django.shortcuts import render
from challenge.models import Product


def index(request):  # View to a simple html file, with links to the other views
    return render(request, 'challenge/index.html')


def products(request):  # View for the 10 cheapest products, taken away any with zero in price
    data = Product.objects.order_by('price')[:10]
    data1 = [x for x in data if x.price != 0]
    diff = len(data) - len(data1)
    if diff < 10:
        number = 10 + diff
        data = Product.objects.order_by('price')[:number]
        data = [x for x in data if x.price != 0]

    return render(request, 'challenge/products.html', {'data': data})

# View for the 10 cheapest products with 'kids' = True


def kids(request):
    data = Product.objects.order_by('price') & Product.objects.filter(kids=True)        
    return render(request, 'challenge/kids.html', {'data': data})

# View for showing products by there ID in the URL


def id(request, product_id):
    data = Product.objects.filter(product_id=product_id)    
    return render(request, 'challenge/id.html', {'data':data})

# View for paginating the products (10 each page)


def paging(request):
    data = Product.objects.all()
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

