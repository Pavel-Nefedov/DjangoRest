from django.db import models
from uuid import uuid4


class Menu(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    home = models.CharField(max_length=64)
    catalog = models.CharField(max_length=64)
    contacts = models.CharField(max_length=64)
    settings = models.CharField(max_length=64)