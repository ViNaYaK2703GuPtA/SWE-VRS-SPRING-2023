from django.http import JsonResponse
import json
import datetime
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def role(request):
     return render(request, 'store/role.html')

def store(request):
     if request.user.is_authenticated:
          if( request.user.is_staff == True):
               return redirect('/admin')
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
          cartItems = order.get_cart_items
     else:
          items = []
          order = {'get_cart_total': 0, 'get_cart_items': 0}
          cartItems = order['get_cart_items']
     products = Product.objects.all()
     context = {'products': products, 'cartItems': cartItems}
     return render(request,
               'store/store.html', context)

def view_product(request, product_name):
     product= Product.objects.get(name=product_name)
     context = {'product': product}
     return render(request, 'store/view.html', context)





def cart(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
          cartItems = order.get_cart_items

     else:
          items = []
          order = {'get_cart_total': 0, 'get_cart_items': 0}
          cartItems = order['get_cart_items']

     context = {'items': items, 'order': order, 'cartItems': cartItems}
     return render(request, 'store/cart.html', context)


def checkout(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()
          cartItems = order.get_cart_items

     else:
          items = []
          order = {'get_cart_total': 0, 'get_cart_items': 0}
          cartItems = order['get_cart_items']

     context = {'items': items, 'order': order, 'cartItems': cartItems}
     return render(request, 'store/checkout.html', context)


def updateItem(request):
     data = json.loads(request.body)
     productId = data['productId']
     action = data['action']

     print('Action:', action)
     print('productId:', productId)

     customer = request.user.customer
     product = Product.objects.get(id=productId)
     order, created = Order.objects.get_or_create(customer=customer, complete=False)

     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

     if action == 'add':
          orderItem.quantity = (orderItem.quantity + 1)
     elif action == 'remove':
          orderItem.quantity = (orderItem.quantity - 1)

     orderItem.save()

     if orderItem.quantity <= 0:
          orderItem.delete()

     return JsonResponse('item was added', safe=False)

def processOrder(request):
     transaction_id = datetime.datetime.now().timestamp()
     data = json.loads(request.body)

     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          total = float(data['form']['total'])
          order.transaction_id = transaction_id

          if total == order.get_cart_total:
               order.complete = True
          order.save()

     else:
          print("User is not logged in!")

     return JsonResponse('Payment Complete!', safe=False)

def customer_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        if password1 != password2:
            return render(request, 'store/customer_signup.html', {'message': 'Password is not confirmed!'})

        if User.objects.filter(username=username).exists():
            return render(request, 'store/customer_signup.html', {'message': 'User already exists!'})

        user = User.objects.create_user(username=username, password=password1, email=email)
        customer = Customer.objects.create(user=user, name=username, email=email, password=password1)

        login(request, user)
        return redirect('/customer/login/')

    return render(request, 'store/customer_signup.html', {'message': 'Account Successfully created!'})

        

def customer_login(request):
     if request.method == 'POST':
          username = request.POST.get('username', '')
          password = request.POST.get('password', '')
          user = authenticate( username=username, password=password)
          if user is not None:
               login(request, user)
               return redirect('/store')
          else:
               return render(request, 'store/customer_login.html', {'message': 'Invalid username or password'})
     
     return render(request, 'store/customer_login.html', {'message': ''})

def staff_login(request):
     if request.method == 'POST':
          username = request.POST.get('username', '')
          password = request.POST.get('password', '')
          user = authenticate( username=username, password=password)
          if user is not None:
               login(request, user)
               return redirect('/store')
          else:
               return render(request, 'store/staff_login.html', {'message': 'Invalid username or password'})
     
     return render(request, 'store/staff_login.html', {'message': ''})