from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.paginator import Paginator
from products.models import product
from customers.models import customer
from orders.models import Order


# ─────────────────────────────────────────────
# All views here require a staff/superuser login
# ─────────────────────────────────────────────

@staff_member_required(login_url='account')
def admin_dashboard(request):
    total_products   = product.objects.filter(delete_status=product.LIVE).count()
    total_customers  = customer.objects.count()
    all_orders       = Order.objects.exclude(order_status=Order.CART_STAGE)
    total_orders     = all_orders.count()
    pending_orders   = all_orders.filter(order_status=Order.ORDER_CONFIRMED).count()
    delivered_orders = all_orders.filter(order_status=Order.ORDER_DELIVERED).count()
    total_revenue    = sum(o.total_price for o in all_orders)

    recent_orders    = all_orders.order_by('-id')[:8]
    top_products     = product.objects.filter(delete_status=product.LIVE).order_by('priority')[:6]
    recent_customers = customer.objects.order_by('-id')[:5]

    context = {
        'total_products':   total_products,
        'total_customers':  total_customers,
        'total_orders':     total_orders,
        'pending_orders':   pending_orders,
        'delivered_orders': delivered_orders,
        'total_revenue':    total_revenue,
        'recent_orders':    recent_orders,
        'top_products':     top_products,
        'recent_customers': recent_customers,
    }
    return render(request, 'admin/dashboard.html', context)


@staff_member_required(login_url='account')
def admin_products(request):
    qs = product.objects.all().order_by('priority', 'id')
    cat = request.GET.get('cat')
    if cat:
        qs = qs.filter(genter=cat)
    paginator = Paginator(qs, 15)
    page = request.GET.get('page', 1)
    products = paginator.get_page(page)
    return render(request, 'admin/products.html', {'products': products})


@staff_member_required(login_url='account')
def admin_add_product(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            price = float(request.POST.get('price'))
            description = request.POST.get('description')
            genter = request.POST.get('genter')
            priority = int(request.POST.get('priority', 0))
            image = request.FILES.get('image')

            product.objects.create(
                title=title,
                price=price,
                description=description,
                genter=genter,
                priority=priority,
                image=image,
            )
            messages.success(request, f'"{title}" has been added successfully.')
            return redirect('admin_products')
        except Exception as e:
            messages.error(request, f'Error adding product: {e}')

    return render(request, 'admin/product_form.html', {'editing': False, 'product': {}})


@staff_member_required(login_url='account')
def admin_edit_product(request, pk):
    obj = get_object_or_404(product, pk=pk)

    if request.method == 'POST':
        try:
            obj.title = request.POST.get('title')
            obj.price = float(request.POST.get('price'))
            obj.description = request.POST.get('description')
            obj.genter = request.POST.get('genter')
            obj.priority = int(request.POST.get('priority', 0))
            if request.FILES.get('image'):
                obj.image = request.FILES['image']
            obj.save()
            messages.success(request, f'"{obj.title}" has been updated.')
            return redirect('admin_products')
        except Exception as e:
            messages.error(request, f'Error updating product: {e}')

    return render(request, 'admin/product_form.html', {'editing': True, 'product': obj})


@staff_member_required(login_url='account')
def admin_delete_product(request, pk):
    obj = get_object_or_404(product, pk=pk)
    title = obj.title
    obj.delete_status = product.DELETE
    obj.save()
    messages.success(request, f'"{title}" has been removed from the catalog.')
    return redirect('admin_products')


@staff_member_required(login_url='account')
def admin_orders(request):
    qs = Order.objects.exclude(order_status=Order.CART_STAGE).order_by('-id')
    status = request.GET.get('status')
    if status:
        qs = qs.filter(order_status=int(status))
    paginator = Paginator(qs, 12)
    page = request.GET.get('page', 1)
    orders = paginator.get_page(page)
    return render(request, 'admin/orders.html', {'orders': orders})


@staff_member_required(login_url='account')
def admin_update_order(request, pk):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=pk)
        new_status = int(request.POST.get('status', order.order_status))
        order.order_status = new_status
        order.save()
        messages.success(request, f'Order #{pk} status updated.')
    return redirect('admin_orders')


@staff_member_required(login_url='account')
def admin_customers(request):
    qs = customer.objects.select_related('user').order_by('-id')
    paginator = Paginator(qs, 15)
    page = request.GET.get('page', 1)
    customers = paginator.get_page(page)
    return render(request, 'admin/customers.html', {'customers': customers})
