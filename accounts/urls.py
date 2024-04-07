from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', views.accounts_list,name="list"),
]
