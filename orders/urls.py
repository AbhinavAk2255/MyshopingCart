from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('cart/',views.show_cart,name='cart'),
    path('orders/',views.view_orders,name='orders'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
    path('removing/<pk>',views.remove,name='remove_item'),
    path('checkout/',views.checkout_cart,name='checkout')
]