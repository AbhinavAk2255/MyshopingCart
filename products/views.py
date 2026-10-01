from django.shortcuts import render,get_object_or_404
from . models import product,newproducts
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    featured_products = product.objects.exclude(delete_status=product.DELETE).order_by('priority')[:4]
    latest_products = product.objects.exclude(delete_status=product.DELETE).order_by('-id')[:8]
    context = {
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)



def products_details(request,pk):
    detailes = get_object_or_404(product, pk=pk, delete_status=product.LIVE)
    
    detail_product = {'detail':detailes}
    return render(request,'product_detail.html',detail_product)


def products_category(request,genter=None):
    page=1
    if request.GET:
        page = request.GET.get('page',1)
    
    allproducts = product.objects.exclude(delete_status=product.DELETE).order_by('id')
    if genter:
        allproducts = allproducts.filter(genter=genter)

    all_product_paginator = Paginator(allproducts,8)
    allproducts = all_product_paginator.get_page(page)
    context = {'allproducts':allproducts}
    return render(request,'products.html',context)

