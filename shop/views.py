from django.shortcuts import render, render_to_response, get_object_or_404
from shop.models import *
from django.template import RequestContext

# Create your views here.

def catalog(request):
    context=RequestContext(request)

    return  render_to_response('index.html', {}, context_instance=context)

def index(request):
    context=RequestContext(request)
    return render_to_response('catalog/index.html', locals(), context_instance=context)

def show_category(request, category_slug):
    context = RequestContext(request)
    c= get_object_or_404(Category, slug=category_slug)
    products=c.product_set.all()
    return render_to_response('catalog/category.html', locals(), context_instance=context)
def showproduct(request, product_slug):
    context=RequestContext(request)
    p=get_object_or_404(Product, slug=product_slug)
    categories=p.categories.filter(is_active=True)
    return  render_to_response('catalog/praduct.html', locals(),context)

