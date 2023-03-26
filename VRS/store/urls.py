from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [    #Leave as empty string for base url
	path('', views.role, name="role"),
	path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('staff/login/', LoginView.as_view(template_name='store/staff_login.html'), name='staff_login'),
    path('customer/login/', LoginView.as_view(template_name='store/customer_login.html'), name='customer_login'),
    path('customer/signup/', LoginView.as_view(template_name='store/customer_signup.html'), name='customer_signup'),
]