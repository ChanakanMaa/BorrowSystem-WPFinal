# Generated by Django 3.0.5 on 2020-04-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20200427_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='current_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
