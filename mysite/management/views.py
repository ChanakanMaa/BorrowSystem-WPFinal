from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT
from django.shortcuts import HttpResponseRedirect, redirect, render
from MySQLdb.constants.ER import USERNAME

from management.forms import AddadminForm

# from item.models import Item


# Create your views here.
@login_required
def register(request):
    if request.method == 'POST':
        form = AddadminForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            print(request.POST)
        return redirect('index')
    else:
        form = AddadminForm()

        # args = {'form': form}
    return render(request, 'add_admin.html', {'form': form})
