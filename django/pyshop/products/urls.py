from django.urls import path
from . import views

#/products (the root of the app)

urlpatterns = [
    path('', views.index) 
]