from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('dashboard/products/', views.admin_products, name='admin_products'),
    path('dashboard/products/add/', views.admin_add_product, name='admin_add_product'),
    path('dashboard/products/<int:pk>/edit/', views.admin_edit_product, name='admin_edit_product'),
    path('dashboard/products/<int:pk>/delete/', views.admin_delete_product, name='admin_delete_product'),

    path('dashboard/orders/', views.admin_orders, name='admin_orders'),
    path('dashboard/orders/<int:pk>/update/', views.admin_update_order, name='admin_update_order'),

    path('dashboard/customers/', views.admin_customers, name='admin_customers'),
]
