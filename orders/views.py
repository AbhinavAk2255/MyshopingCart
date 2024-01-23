from django.shortcuts import render,redirect
from . models import Order,OrderedItem
from products.models import product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def show_cart(request):
    user = request.user
    customer = user.customer_profile
    amount = 0

    cart_obj,create = Order.objects.get_or_create(
        owner = customer,
        order_status = Order.CART_STAGE
    )
    cart = OrderedItem.objects.filter(owner=cart_obj)
    for item in cart:
        amount = amount + item.product.price * item.quantity

    total = amount + 35
    context = {'cart':cart_obj,'amount':amount,'total':total}
    return render(request,'cart.html',context)

@login_required(login_url='account')
def view_orders(request):
    user = request.user
    customer = user.customer_profile
    added_item = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)

    context = {'orders':added_item}

    return render(request,'order.html',context)


def checkout_cart(request):
    if request.POST:
        try:

            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get('total'))
            order_obj = Order.objects.get(
                owner = customer,
                order_status = Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_message = 'your order is confirmed..'
                messages.success(request,status_message)
            else:
                status_message = 'Unable to processed the order'
                messages.error(request,status_message)
        
        except Exception as e:
            status_message = 'Unable to processed the order'
            messages.error(request,status_message)

        return redirect('cart')

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        
        cart_obj,created = Order.objects.get_or_create(
            owner = customer,
            order_status = Order.CART_STAGE
        )
        product_detai = product.objects.get(id=product_id)
        orderd_item,create = OrderedItem.objects.get_or_create(
            product = product_detai,
            owner = cart_obj
        )
        if create:
            orderd_item.quantity = quantity
            orderd_item.save()
        else:
            orderd_item.quantity = orderd_item.quantity + quantity
            orderd_item.save()
    
        return redirect('cart')
    

    
def remove(request,pk):
    # user = request.user
    # customer = user.customer_profile
    # product_id = product.objects.get(pk=pk)
    # print(product_id)

    # cart_obj,create = Order.objects.get_or_create(
    # owner = customer,
    # order_status = Order.CART_STAGE
    # )
    # item = OrderedItem.objects.filter(owner=cart_obj,product=product_id)
    # item.delete()
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()

    return redirect('cart')