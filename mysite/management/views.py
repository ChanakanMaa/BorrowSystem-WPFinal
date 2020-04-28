from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT
from django.shortcuts import HttpResponseRedirect, redirect, render
from MySQLdb.constants.ER import USERNAME

from management.forms import AddadminForm
from management.models import Addadmin

# from item.models import Item


# Create your views here.
@login_required
def register(request):
    if request.method == 'POST':
        form = AddadminForm(request.POST)
        if form.is_valid():
            Addadmin.objects.create(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password1=form.cleaned_data['password1'],
                password2=form.cleaned_data['password2'],
                is_staff=form.cleaned_data['is_staff'],
                is_active=form.cleaned_data['is_active'],
                is_superuser=form.cleaned_data['is_superuser'],
            )
            form.save()
            print(form)
            print(request.POST)
        return redirect('index')
    else:
        form = AddadminForm()

        # args = {'form': form}
    return render(request, 'add_admin.html', {'form': form})
