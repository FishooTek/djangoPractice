from django.shortcuts import render
from django.http import HttpResponse
from .models import Accounts

# Create your views here.
def accounts_list(request):
    accounts = Accounts.objects.all().order_by('open_date')
    return render(request,'accounts/accounts_list.html',{'accounts':accounts})

