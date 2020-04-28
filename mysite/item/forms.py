from django import forms
from datetime import datetime

class ItemForm(forms.Form):
    item_name = forms.CharField(max_length=255, label='ชื่ออุปกรณ์')
    item_amount = forms.IntegerField(label='จำนวนอุปกรณ์ทั้งหมด')
    current_amount = forms.IntegerField(label='จำนวนอุปกรณ์ที่มีอยู่')
    item_image = forms.FileField(max_length=255, required=False, label='รูปภาพ')
    # create_date = forms.DateField(auto_now=False, auto_now_add=True, editable=False, label='วันที่เพิ่มอุปกรณ์')
    # update_date = forms.DateField(auto_now=True, auto_now_add=False, label='วันที่อัพเดทอุปกรณ์')

    item_name.widget.attrs.update({'class': 'form-control'})
    item_amount.widget.attrs.update({'class': 'form-control'})
    current_amount.widget.attrs.update({'class': 'form-control'})
    

class ItemSearchForm(forms.Form):
    item_name = forms.CharField(max_length=255, label='ค้นหาชื่ออุปกรณ์', required=False)

    item_name.widget.attrs.update({'class': 'form-control'})