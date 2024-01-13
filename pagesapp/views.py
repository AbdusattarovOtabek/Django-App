from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *

navbar =[
    {'title' : 'Home', 'url_name' : '#home'},
    {'title' : 'About','url_name' : '#about'},
    {'title' : 'Services','url_name' : '#services'},
    {'title' : 'Product','url_name' : '#product'},
    {'title' : 'Contact','url_name' : '#contact'},
]
@login_required(login_url='register')
def menu(request):
    menu = Catalog.objects.all()
    menu = {
        'menu' : menu,
        'navb' : navbar,
        'catalog' : menu,
    }
    return render(request, 'pagesapp/main.html', menu)
def catalog(request):
    catalog = Catalog.objects.all()
    
    return render(request,'pagesapp/base.html', catalog)

def tovar(request,cat_id):
    catalog = Catalog.objects.all()
    productpost = Product.objects.filter(cat_id=cat_id)
    productpost = {
        'catalog' : catalog,
        'productpost' : productpost
    }
    return render(request,'pagesapp/laptop.html', productpost)

def intro(request):
    return render(request,'pagesapp/intro.html')
# @login_required(login_url='register')
class product_add(CreateView):
    model = Product
    template_name = 'pagesapp/add-product.html'
    success_url = reverse_lazy('menu')
    fields = ['cat','product_img','product_name','product_price','product_info','product_item']
