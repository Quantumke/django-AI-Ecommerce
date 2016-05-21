from django import forms
from shop.models import *

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = ('name', 'slug', 'brand', 'sku','price', 'old_price','image','is_active',
        #           'is_bestseller','quantity','description','meta_keywords', 'meta_description',
        #           'created_at','updated_at','categories',)
