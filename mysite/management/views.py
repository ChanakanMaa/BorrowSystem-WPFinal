from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404

# from item.models import Item


# Create your views here.
def addItem(request):
    username = None
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'manageItem.html')

def addAdmin(request):
    username = None
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'add_admin.html')