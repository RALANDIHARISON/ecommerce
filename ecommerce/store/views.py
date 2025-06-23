from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .utils import cookieCart, cartData, guestOrder
from .models import Product, Order, OrderItem, Customer, ShippingAddress


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    products = Product.objects.all()

    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems = data['cartItems']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'store/checkout.html', context)


def updateItem(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        if request.user.is_authenticated:
            customer = request.user.customer
            product = Product.objects.get(id=productId)
            order, created = Order.objects.get_or_create(customer=customer, complete=False)

            orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

            if action == 'add':
                orderItem.quantity += 1
            elif action == 'remove':
                orderItem.quantity -= 1

            orderItem.save()

            if orderItem.quantity <= 0:
                orderItem.delete()

            return JsonResponse('Item was updated for authenticated user', safe=False)
        else:
            print('User is not authenticated. Implement guest cart logic here.')
            return JsonResponse('Item update for guest user (logic to be added)', safe=False)
    else:
        return JsonResponse('Invalid request method', safe=False, status=405)


def processOrder(request):
    if request.method == 'POST':
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body.decode('utf-8'))
        total = float(data['form']['total'])

        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
        else:
            print('User is not logged in')
            print('COOKIES:', request.COOKIES)
            customer, order = guestOrder(request, data)

        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping:
            ShippingAddress.objects.create(
                customer=order.customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

        return JsonResponse('Payment submitted.', safe=False)

    else:
        return JsonResponse('Invalid request method', safe=False, status=405)
