from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404


# Create your views here.
def index(request):
    return render(request, template_name='index.html')