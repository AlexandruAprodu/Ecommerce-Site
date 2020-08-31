from django.contrib import admin
from django.urls import path, include
from ecomm import views as ecomm_views
from products import views as products_views

app_name = 'products'

urlpatterns = [
    path('<str:category_category_slug>/', products_views.filter_products, name='categorii'),
    ]
