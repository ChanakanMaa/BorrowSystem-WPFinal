from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404

from item.models import Item


# Create your views here.
def index(request):
    # username = None
    # if not request.user.is_authenticated:
    #     return redirect('')
    # item_list = Item.objects.get()
    # context = {
    #     'item_list': item_list,
    # }
    return render(request, 'index.html')