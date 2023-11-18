from django.urls import path
from . import views
from .views import product_search

urlpatterns = [
    path('', views.index),
    path('new/', views.new), 
    path('search/', product_search, name='product_search'),
    # Add other URL patterns as needed
]