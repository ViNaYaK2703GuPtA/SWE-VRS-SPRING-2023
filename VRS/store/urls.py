from django.urls import path
from . import views
from . import models
from .views import toggle_inlist
from django.contrib.auth import views as auth_views
urlpatterns = [
	# Leave as empty string for base url
	path('', views.role, name="role"),
	path('store/', views.store, name="store"),
	path('my-list/', views.mylist, name="mylist"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('staff/login/', views.staff_login, name='staff_login'),
    path('customer/login/', views.customer_login, name='customer_login'),
    path('customer/signup/', views.customer_signup, name='customer_signup'),
	path('get_products/', views.get_products, name='get_products'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('view/<str:product_name>/', views.view_product, name="view_product"),
    path('toggle_inlist/<int:product_id>/', toggle_inlist, name='toggle_inlist'),
]
