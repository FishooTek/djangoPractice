from django.http import HttpResponse
from django.shortcuts import render
# from djangonautic import te

def home_view(request):
    return render(request,'homepage.html')
    # return HttpResponse("Hello world,this is home ")


def about_view(request):
    return render(request,'about.html')
    # return HttpResponse("Hello world ")