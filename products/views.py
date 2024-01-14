from django.shortcuts import render
from . models import product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products = product.objects.order_by('priority')[:4]
    latest_products = product.objects.order_by('-id')[:4]
    context = {
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)

def products_list(request):
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    products_list = product.objects.all()
    product_paginator = Paginator(products_list,2)
    products_list = product_paginator.get_page(page)
    context = {'products':products_list}
    return render(request,'products.html',context)

def products_details(request,pk):
    detailes = product.objects.get(pk=pk)
    print(detailes)
    detail_product = {'detail':detailes}
    return render(request,'product_detail.html',detail_product)