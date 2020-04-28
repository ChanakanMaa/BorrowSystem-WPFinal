from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError

class ItemForm(forms.Form):
    item_name = forms.CharField(max_length=255, label='ชื่ออุปกรณ์')
    item_amount = forms.IntegerField(label='จำนวนอุปกรณ์ทั้งหมด')
    current_amount = forms.IntegerField(label='จำนวนอุปกรณ์ที่มีอยู่')
    item_image = forms.FileField(max_length=255, required=False, label='รูปภาพ')
    # create_date = forms.DateField(auto_now=False, auto_now_add=True, editable=False, label='วันที่เพิ่มอุปกรณ์')
    # update_date = forms.DateField(auto_now=True, auto_now_add=False, label='วันที่อัพเดทอุปกรณ์')

    # self คือ instance จาก form
    def clean_item_amount(self):
        data = self.cleaned_data['item_amount']
        # เวลาเกิดเออเร่อต้อง raise ออกมา
        if data < 0:
            raise forms.ValidationError('จำนวนอุปกรณ์ทั้งหมดต้องมากกว่า 0')
        # ต้อง return ข้อมูลออกไปเสมอ ไม่งั้นจะหาย
        return data

    def clean_current_amount(self):
        data = self.cleaned_data['current_amount']
        if data <= 0:
            raise forms.ValidationError('จำนวนอุปกรณ์ที่มีอยู่ต้องไม่น้อยกว่า 0')
        return data

    # เข้าถึงข้อมูลของทุก field ได้
    def clean(self):
        # เรียก class แม่ method form
        cleaned_data = super().clean()
        item_amount = cleaned_data.get('item_amount')
        current_amount = cleaned_data.get('current_amount')

        if item_amount and current_amount:
            if current_amount > item_amount:
                raise forms.ValidationError('จำนวนอุปกรณ์ทั้งหมดต้องมากกว่าอุปกรณ์ที่มีอยู่')


    item_name.widget.attrs.update({'class': 'form-control'})
    item_amount.widget.attrs.update({'class': 'form-control'})
    current_amount.widget.attrs.update({'class': 'form-control'})


class ItemSearchForm(forms.Form):
    item_name = forms.CharField(max_length=255, label='ค้นหาชื่ออุปกรณ์', required=False)

    item_name.widget.attrs.update({'class': 'form-control'})