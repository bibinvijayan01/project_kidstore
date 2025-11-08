
from django.urls import path
from . import views




urlpatterns =[
    path('', views.store, name="store"),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),


]