from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100, unique=False)
    slug=models.SlugField(max_length=100, unique=True)
    description=models.TextField(blank=False)
    is_active=models.BooleanField(default=True)
    meta_keywords=models.CharField("Meta Keywords", max_length=100)
    meta_description=models.CharField("Meta Description", max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='categories'
        ordering=['-created_at']
        verbose_name_plural= "Categories"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug':self.slug})


class Product(models.Model):
    name=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    brand=models.CharField(max_length=100)
    sku=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=9, decimal_places=2)
    old_price=models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image=models.ImageField(upload_to='images/', verbose_name='images')
    is_active=models.BooleanField(default=True)
    is_bestseller=models.BooleanField(default=False)
    quantity=models.IntegerField()
    description=models.TextField(blank=False)
    meta_keywords=models.CharField(max_length=200)
    meta_description=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    categories=models.ManyToManyField(Category)
    class Meta:
        db_table='products'
        ordering =['-created_at']

    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('catalog_product',(), {'product_slug':self.slug} )

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None