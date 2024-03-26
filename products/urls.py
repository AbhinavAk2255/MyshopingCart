from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.index,name='home'),
    path('products/', views.products_category,name='products_category'),
    path('product_category_list/<genter>',views.products_category,name='products_category_filtered'),
    path('product_detail/<pk>',views.products_details,name='detail_of_product'),
    
]