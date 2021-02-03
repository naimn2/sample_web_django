from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('about.html', views.about),
    path('testmonial.html', views.testimonial),
    path('clients.html', views.clients),
    path('contact.html', views.contact),
]