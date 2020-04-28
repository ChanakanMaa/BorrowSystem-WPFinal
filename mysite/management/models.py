from django.db import models

# Create your models here.
class Addadmin(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length = 254)
    password1 = models.CharField(max_length=255, null=True)
    password2 = models.CharField(max_length=255, null=True)
    staff_choice = ((True, 'Yes'), (False, 'No'))
    is_staff = models.BooleanField(choices=staff_choice, null=True)
    active_choice = ((True, 'Yes'), (False, 'No'))
    is_active = models.BooleanField(choices=active_choice, null=True)
    superuser_choice = ((True, 'Yes'), (False, 'No'))
    is_superuser = models.BooleanField(choices=superuser_choice, null=True)
