from builtins import object
from fnmatch import filter
from venv import create

from astroid.protocols import objects
# def upload_list(request):
from astroid.scoped_nodes import objects
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import Http404, HttpResponse
from django.shortcuts import HttpResponseRedirect, redirect, render

from item.forms import ItemForm, ItemSearchForm
from item.models import Item


# Create your views here.
@login_required
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    # ต้องเช็คว่า form ที่ส่งเข้ามาเป็น POST
    if request.method == 'POST':
        # ถ้าส่งมา POST ก็จะสร้าง ItemForm + ส่ง request.POST เข้าไป ; จาก form หน้า html เข้าไปใน Itemform
        form = ItemForm(request.POST, request.FILES)
            # ต้องเช็ค is_valid จะเช็คให้เบื้องต้น
        if form.is_valid():
            Item.objects.create(
                item_name=form.cleaned_data['item_name'],
                item_amount=form.cleaned_data['item_amount'],
                current_amount=form.cleaned_data['current_amount'],
                item_image=form.cleaned_data['item_image'],
                create_date=False,
                update_date=False,
            )
            # form.save()
        
        # uploaded_file = request.FILES['item_image']
        # fs = FileSystemStorage()
        # fs.save(uploaded_file.name, uploaded_file)
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        return redirect('index')
    else:
        form = ItemForm()

    return render(request, 'item.html', {'form': form})

@login_required
def item_delete(request):
    form = ItemSearchForm(request.GET)

    if form.is_valid():
        item_name = form.cleaned_data['item_name']

        item_list = Item.objects.filter(item_name__icontains=item_name)
    else:
        item_list = []

    return render(request, 'item_delete.html', {'form':form, 'item_list': item_list})


@login_required
def delete(request, item_id):
    item = Item.objects.get(pk=item_id)
    # print(item_id)
    item.delete()
    # item.save()

    return redirect('item_delete')
