from django import forms
from datetime import datetime

class ItemForm(forms.Form):
    item_name = forms.CharField(max_length=255, label='ชื่ออุปกรณ์')
    item_amount = forms.IntegerField(label='จำนวนอุปกรณ์ทั้งหมด')
    current_amount = forms.IntegerField(label='จำนวนอุปกรณ์ที่มีอยู่')
    item_image = forms.FileField(max_length=255, required=False, label='รูปภาพ')
    # create_date = forms.DateField(auto_now=False, auto_now_add=True, editable=False, label='วันที่เพิ่มอุปกรณ์')
    # update_date = forms.DateField(auto_now=True, auto_now_add=False, label='วันที่อัพเดทอุปกรณ์')

# class FileForm(forms.ModelForm):
#     class Meta:
#         model = File
#         fields = ['item_name, item_amount, current_amount, item_image']