# Generated by Django 3.0.5 on 2020-04-28 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0007_remove_item_del_flag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(null=True)),
                ('request_time', models.CharField(blank=True, max_length=8, null=True)),
                ('borrow_date', models.DateField(null=True)),
                ('return_date', models.DateField(null=True)),
                ('takeback_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('01', 'อยู่ในตะกร้า'), ('02', 'รออนุมัติ'), ('03', 'ยืนยันการยืม'), ('04', 'คืนแล้ว'), ('05', 'ยกเลิก'), ('06', 'ของเสีย/หาย'), ('07', 'จอง')], max_length=2, null=True)),
                ('fine', models.IntegerField(blank=True, null=True)),
                ('cancel_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cancelpt_by', to=settings.AUTH_USER_MODEL)),
                ('confirm_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='confirm_by', to=settings.AUTH_USER_MODEL)),
                ('defective_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='defective_by', to=settings.AUTH_USER_MODEL)),
                ('return_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='return_by', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='request_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_amount', models.IntegerField(blank=True, null=True)),
                ('borrow_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='borrow.Borrow')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='item.Item')),
            ],
        ),
    ]