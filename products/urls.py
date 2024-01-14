from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.index,name='home'),
    path('product_list/',views.products_list,name='listof_products'),
    path('product_detail/<pk>',views.products_details,name='detail_of_product'),
]