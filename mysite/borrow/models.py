from django.db import models
from item.models import Item
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Borrow(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.PROTECT, related_name='request_by')
    request_date = models.DateField(null=True)
    request_time = models.CharField(max_length=8, blank=True, null=True)
    borrow_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    takeback_date = models.DateField(blank=True, null=True)

    IN_CART = '01'
    WAIT = '02'
    CONFIRMED = '03'
    RETURNED = '04'
    CANCELED = '05'
    DEFECTIVE = '06'
    STATUS = (
        (IN_CART, 'อยู่ในตะกร้า'),
        (WAIT, 'รออนุมัติ'),
        (CONFIRMED, 'ยืนยันการยืม'),
        (RETURNED, 'คืนแล้ว'),
        (CANCELED, 'ยกเลิก'),
        (DEFECTIVE, 'ของเสีย/หาย'),
    )
    status = models.CharField(max_length=2, choices=STATUS, blank=True, null=True)
    confirm_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='confirm_by', null=True, blank=True)
    cancel_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='cancelpt_by', null=True, blank=True)
    return_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='return_by', null=True, blank=True)
    defective_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='defective_by', null=True, blank=True)
    fine = models.IntegerField(blank=True, null=True)
    def __int__(self):
        return self.id


class Borrow_Item(models.Model):
    borrow_id = models.ForeignKey(Borrow, on_delete=models.PROTECT)
    item_id = models.ForeignKey(Item, on_delete=models.PROTECT)
    borrow_amount = models.IntegerField(blank=True, null=True)