# Generated by Django 3.0.5 on 2020-04-28 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_auto_20200428_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]
