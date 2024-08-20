from django.urls import path
from .views import create_customer

urlpatterns = [
    path('api/create-customer/', create_customer, name='create_customer'),
]
