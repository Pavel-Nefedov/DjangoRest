from django.db import models



class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(null=False, default=False)
    is_staff = models.BooleanField(null=False, default=False)
