from django.db import models

# Database formatet kan optimeres hvis det er nødvendigt, sat med standard værdier blot for test formål
class Product(models.Model):
    kids = models.BooleanField(null=True, blank=True)
    name = models.CharField(max_length=255, blank=True)
    #relative_url = models.CharField(max_length=255, blank=True)
    #discount_percentage = models.IntegerField(blank=True)
    kid_adult = models.BooleanField(null=True, blank=True)
    #free_porto = models.BooleanField()
    #image = models.CharField(max_length=255)
    #sizes = models.CharField(max_length=255)
    #package = models.BooleanField()    
    price = models.FloatField(blank=True)
    #discount_type = models.CharField(max_length=255)
    #product_labels = models.CharField(max_length=255)
    #url = models.CharField(max_length=255)
    #online = models.BooleanField()
    #price_old = models.FloatField()
    currency = models.CharField(max_length=255, blank=True)
    #img_url = models.CharField(max_length=255)    
    product_id = models.CharField(max_length=255, blank=True)
    #women = models.BooleanField()    

    def __str__(self):
        return self.name