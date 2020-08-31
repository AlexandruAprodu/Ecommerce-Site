from django.contrib import admin
from django.urls import path, include
from ecomm import views as ecomm_views
from users import views as users_views

app_name = 'ecomm'

urlpatterns = [
    path('', ecomm_views.index, name='index'),
    path('contact/', ecomm_views.contact, name='contact'),
    path('results/', ecomm_views.SearchView.as_view(), name='search'),
    path('about/', ecomm_views.about, name='about'),
    path('categories/', ecomm_views.categories, name='categories'),

    ]

