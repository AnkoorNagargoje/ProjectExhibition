from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authentication/phone/', views.email_signup),
    path('authentication/signup/', views.signup),
    path('authentication/signin/', views.signin, name='signin'),
    path('authentication/signout/', views.signout),

]