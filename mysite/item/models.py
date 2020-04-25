from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200, blank=True, null=True)
    item_amount = models.IntegerField(blank=True, null=True)
    item_image = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True, null=True)
    create_date = models.DateField(auto_now=False, auto_now_add=True, editable=False)
    update_date = models.DateField(auto_now=True, auto_now_add=False)
    reserve_status = models.CharField(max_length=2, default='01')
    amount_reserve = models.IntegerField(default=0)
