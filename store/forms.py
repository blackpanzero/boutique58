# forms.py 
from django import forms 
from .models import *
  
class ProductForm(forms.ModelForm): 
  
    class Meta: 
        model = Item 
        fields = ['name', 'Product_Img'] 