from django.contrib import admin
from django.urls import path, include
from WebApp import views

urlpatterns =[
    path('home_page/', views.home_page, name="home_page"),
    path('about_page/', views.about_page, name="about_page"),
    path('all_product/', views.all_product, name="all_product"),
    path('contact/', views.contact, name="contact"),
    path('filtered_page/<cat_name>/', views.filtered_page, name="filtered_page"),
    path('single_product/<int:pro_id>/', views.single_product, name="single_product"),
    path('signin_signup/', views.signin_signup, name="signin_signup"),
    path('save_registration/', views.save_registration, name="save_registration"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('help/', views.help, name="help"),
    path('support_page/', views.support_page, name="support_page"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),



]