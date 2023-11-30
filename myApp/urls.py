from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('get-drinks/', views.getDrinks, name="getDrinks"),
    path('get-drinks/<int:drink_id>', views.getDrinkDetails, name="getDrinkById"),
]
