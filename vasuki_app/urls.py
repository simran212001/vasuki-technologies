from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('contact', views.contactpage, name='contact'),
    path('service1', views.service1, name='service1'),
    path('service2', views.service2, name='service2'),
    path('service3', views.service3, name='service3'),
    path('service4', views.service4, name='service4'),
    path('service5', views.service5, name='service5'),
    path('clients', views.client, name='clients'),
    path('details', views.details, name='details'),
    path("blogs/", views.blog_detail, name="blog_list"),
    path("TOS", views.TOS, name="TOS"),
    path("privacy", views.privacy, name="privacy"),




   
]
