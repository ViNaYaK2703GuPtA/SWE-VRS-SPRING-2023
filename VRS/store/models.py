from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your models here.



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    image=models.ImageField(null=True, blank=True)
    description=models.TextField( null=True, blank=True)
    rating=models.FloatField(default=0)
    genre=models.CharField(max_length=200, null=True, blank=True)
    inlist=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 
    


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return str(self.id) 
    


class Staff(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    password= models.CharField(max_length=200, null=True)
    Status= models.CharField(default='Staff', max_length=200, null=True)
    date_joined= models.DateTimeField(auto_now_add=True)
    class Meta:
        permissions = (
            ("can_view_staff", "Can view staff"),
            ("can_edit_staff", "Can edit staff"),
            ("can_delete_staff", "Can delete staff"),
        )
   


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Create a new user instance with the same email as the staff instance
        user = User.objects.create_user(
            username=self.name,
            email=self.email,
            password=self.password,
            is_staff=True,
        )

        # Set the user instance as the `user` attribute of the staff instance
        self.user = user

        super(Staff, self).save(*args, **kwargs)


