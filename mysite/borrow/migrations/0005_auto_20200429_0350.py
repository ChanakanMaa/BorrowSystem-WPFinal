# Generated by Django 3.0.5 on 2020-04-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0004_borrow_borrow_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='status',
            field=models.CharField(blank=True, choices=[('01', 'อยู่ในตะกร้า'), ('02', 'รออนุมัติ'), ('03', 'ยืนยันการยืม'), ('04', 'คืนแล้ว'), ('05', 'ยกเลิก'), ('06', 'ของเสีย/หาย')], max_length=2, null=True),
        ),
    ]