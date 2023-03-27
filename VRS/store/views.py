from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
  
# Create your views here.

def role(request):
     return render(request, 'store/role.html')


def store(request):
     products = Product.objects.all()
     context = {'products': products}
     return render(request, 
     'store/store.html', context)

def cart(request):
     context = {}
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()  

     else:
          items = []
          order = {'get_cart_total': 0, 'get_cart_items': 0}
     
     context = {'items': items, 'order': order}
     return render(request, 'store/cart.html', context)

def checkout(request):
     context = {}
     if request.user.is_authenticated:
          customer = request.user.customer
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          items = order.orderitem_set.all()  

     else:
          items = []
          order = {'get_cart_total': 0, 'get_cart_items': 0}
     
     context = {'items': items, 'order': order}
     return render(request, 'store/checkout.html', context)


def customer_signup(request):
     if request.method == 'POST':
          username = request.POST.get('username', '')
          password1 = request.POST.get('password1', '')
          password2 = request.POST.get('password2', '')
          email = request.POST.get('email', '')

          if password1 != password2 : 
              return render(request, 'store/customer_signup.html', {'message': 'Password is not confirmed!'})
          if len(User.objects.filter(username=username))!=0:
               return render(request, 'store/customer_signup.html', {'message': 'User already exists!'})
          
          user = User.objects.create_user(username=username, password=password1, email=email)
          
          user.save()
          return redirect('/customer/login/')
     
     return render(request, 'store/customer_signup.html', {'message': 'Account Succesfully created!'})

        

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
               return render(request, 'store/staff_login.html', {'error_message': 'Invalid username or password'})
     
     return render(request, 'store/staff_login.html', {'error_message': ''})
