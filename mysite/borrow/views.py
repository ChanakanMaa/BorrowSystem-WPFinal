from django.shortcuts import render, HttpResponseRedirect, redirect
from django.utils.translation import gettext as _
from datetime import date, timedelta, datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import messages

from .models import Borrow, Borrow_Item
from item.models import Item

# Create your views here.
# def add_cart(request):
#     return render(request, 'add_cart.html')

def add_cart(request):
    username = None
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)

        if 'item' in request.POST:
            print(request.POST)
            addcart = request.POST['addcart']
            items = request.POST.getlist('item')
            #check user choose reserve or borrow
            # if addcart == 'reserve':
            #     if request.POST['borrow_date'] == '':
            #         messages.success(request, _('กรุณาเลือกวันที่ต้องการจองพัสดุ'))
            #         return redirect('/item')
            #     for it in items:
            #         it_id = int(it)
            #         item = Item.objects.get(id=it_id)
            #         if item.reserve_status == '02':
            #             messages.success(request, _('พัสดุที่เลือกถูกจองแล้ว'))
            #             return redirect('/item')
            #     borrow = Borrow.objects.filter(student_id=user.id, status='00')
            #     borrow_date = request.POST['borrow_date']
            #     #user have reserve-cart, then add just new item to reserve-cart
            #     if borrow:
            #         print('have reserve-cart')
            #         for br in borrow:
            #             borrow = Borrow.objects.get(id=br.id)
            #             break
            #         borrow.borrow_date = borrow_date
            #         borrow.save()
            #         for it in items:
            #             it_id = int(it)
            #             item_id = Item.objects.get(id=it_id)
            #             count = 0
            #             borrow_item = Borrow_Item.objects.filter(borrow_id=br.id)
            #             for brit in borrow_item:
            #                 print('add item: ', item_id.item_name)
            #                 if item_id.id == brit.item_id.id:
            #                     print('count')
            #                     count = count+1
            #                     print(item_id.id, '=', brit.item_id.id, 'break loop')
            #                     break
            #             if count == 0:
            #                 borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
            #                 borrow_item.save()
            #                 reserve = Reserve(borrow_item_id=borrow_item, borrow_id=borrow, item_id=item_id)
            #                 reserve.save()
            #     user do not have reserve-cart, then create new reserve-cart
            #     else:
            #         print('do not have reserve-cart')
            #         borrow = Borrow.objects.create(status='00', student_id=user, borrow_date=borrow_date)
            #         for it in items:
            #             it_id = int(it)
            #             item_id = Item.objects.get(id=it_id)
            #             borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
            #             borrow_item.save()
            #             reserve = Reserve(borrow_item_id=borrow_item, borrow_id=borrow, item_id=item_id)
            #             reserve.save()
            #     print('go to reserve date')
            #     return HttpResponseRedirect('/borrow/reserve_date/%d' % (borrow.id))
            if addcart == 'borrow':
                print('borrow')
                borrow = Borrow.objects.filter(student_id=user.id, status='01')

                if borrow:
                    for br in borrow:
                        borrow = Borrow.objects.get(id=br.id)
                        break
                    try:
                        for it in items:
                            it_id = int(it)
                            item_id = Item.objects.get(id=it_id)
                            print('pass 1')
                            count = 0
                            borrow_item = Borrow_Item.objects.filter(borrow_id=borrow)
                            print('brit0')
                            for brit in borrow_item:
                                print('brit1')
                                if item_id.id == brit.item_id.id:  # if item has been in cart
                                    count = count + 1
                                    break
                                    print('pass 2')
                            if count == 0:
                                borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
                                borrow_item.save()
                                print('pass 3')
                    except:
                        print('error')
                        return HttpResponseRedirect('cart')
                else:
                    borrow = Borrow.objects.create(status='01', student_id=user)

                    for it in items:
                        it_id = int(it)
                        item_id = Item.objects.get(id=it_id)
                        borrow_item = Borrow_Item(id=None, borrow_id=borrow, item_id=item_id)
                        borrow_item.save()
                        print("borrow_id:", borrow.id, "saved")
            #             if addcart == 'reserve':
            #                 reserve = Reserve(borrow_item_id=borrow_item, borrow_id=borrow.id, item_id=item_id)
            #                 reserve.save()

            return HttpResponseRedirect('cart')
        else:
            print(request.POST)
            messages.success(request, _('กรุณาเลือกพัสดุ'))
    return redirect('index')


def cart(request):
    if not request.user.is_authenticated:
        return redirect('/')
        
    user = User.objects.get(username=request.user.username)
    borrow = Borrow.objects.filter(student_id=user.id, status='01')
    br = None
    for b in borrow:
        print('borrowid: ', b.id)
        br = Borrow.objects.get(id=b)
    if borrow:
        for br in borrow:
            borrow = Borrow.objects.get(id=br.id)
            break
        borrow_item = Borrow_Item.objects.filter(borrow_id=br.id)
    else:
        message = 'ไม่มีพัสดุที่เลือก'
        return render(request, 'cart.html', {'message': message})
    item = Item.objects.all()
    print('borrow.id', borrow.id)
    status = '0'
    rt_status = '0'
    if request.POST:
        print('request: ', request.POST)
        return_date = request.POST['return_date']
        rd = return_date.split('-')
        return_date = date(int(rd[0]),int(rd[1]),int(rd[2]))
        current_date = date.today()
        diff = return_date - current_date
        if diff.days > 5 or diff.days < 0: #check invalid diff day
            rt_status = '01'

        for brit in borrow_item:
            name = 'borrow_amount' + str(brit.item_id)
            borrow_amount = request.POST.get(name)
            try:
                if (int(borrow_amount) > brit.item_id.current_amount) or (int(borrow_amount) <= 0):
                    status = '01'
                else:
                    pass
            except:
                messages.success(request, _('ไม่มีพัสดุที่สามารถยืมได้'))
                print(messages)
                return redirect('cart')

        if status == '0' and rt_status == '0':
            borrow.status = '02'
            borrow.request_date = date.today()
            borrow.request_time = datetime.now().time().strftime("%H:%M:%S")
            borrow.return_date = return_date
            borrow.save()
            count=0
            for brit in borrow_item:
                name = 'borrow_amount' + str(brit.item_id)
                borrow_amount = request.POST.get(name)
                print('borrow_item_id: ', brit.id)
                brit.borrow_amount = borrow_amount
                brit.save()
                count = count + 1
            # if count == 0:
            #     borrow.delete()
            # return redirect('/borrow/history/02')

    context = {
        'borrow': borrow,
        'borrow_item': borrow_item,
        'item': item,
        'status': status,
        'rt_status': rt_status,
        'br': br,
    }
    return render(request, 'cart.html', context)

# def cart(request):
#     return render(request, 'cart.html')