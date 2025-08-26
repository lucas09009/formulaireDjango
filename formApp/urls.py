from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('home/', views.home, name='home'),
    path('Logout/', views.Logout, name='Logout'),
]