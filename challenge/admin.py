from django.contrib import admin

#importere product ind i admin modulet, så vi kan redigere, slette og oprette
from .models import Product

admin.site.register(Product)
