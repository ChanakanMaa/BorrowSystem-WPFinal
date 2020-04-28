# Generated by Django 3.0.5 on 2020-04-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200428_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='addadmin',
            name='is_active',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AddField(
            model_name='addadmin',
            name='is_superuser',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
        migrations.AlterField(
            model_name='addadmin',
            name='is_staff',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]