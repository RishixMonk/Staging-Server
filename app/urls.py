from django.contrib import admin
from django.urls import path
from app import views

urlpatterns=[
    path("",views.index),
    path("id",views.id),
    path("123",views.test)
]