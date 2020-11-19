from django.db import models
from datetime import datetime

# Create your models here.

TYPE = (
    ('ACCESSORIES', 'Accessories'),
    ('CLOTHING', 'Clothing'),
    ('SHOES','Shoes'),



    )

CATEGORIES = (
    ('DRESSES','Dresses'),
    ('TROUSERS','Trousers'),
    ('SWEATERS','Sweaters'),
    ('BLAZERS','Blazers'),
    ('ROMPERS','Rompers'),
    ('T-SHIRTS','T-shirts'),
    ('TOPS','Tops'),
    ('BOOTS','Boots'),
    ('HEALS','Heals'),
    ('SNEAKERS','Sneaks'),
    ('SUNGLASSES','Sunglasses'),
    ('UNDERWARE','Underware'),
    ('BAGS','Bags'),
    ('HEELS','Heels'),
    ('SNEAKERS','Sneakers'),
    ('PERFUMES','Perfumes'),


    )





GENDER = (
    ('MEN', 'Men'),
    ('WOMEN', 'Women'),
    ('KIDS', 'KIDS'),
   
    )

class Item(models.Model): 
    name = models.CharField(max_length=50) 
    Product_Img = models.ImageField(upload_to='images/') 
    Price = models.DecimalField(max_digits=19, decimal_places=2)
    category_type=models.CharField(max_length=64,default="",choices=TYPE)
    categories=models.CharField(max_length=64,default="",choices=CATEGORIES)
    date = models.DateTimeField(default=datetime.now())
    gender=models.CharField(max_length=64,default="",choices=GENDER)

class Team(models.Model):
    first_name = models.CharField(max_length=50) 
    second_name= models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',default="none") 

class Subscriber(models.Model):
    email = models.CharField(max_length=255) 
  
    
    
