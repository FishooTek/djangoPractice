
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('accounts/',include('accounts.urls')),
    path('user/',include('user.urls')),
    path('about/', views.about_view),
]
