from django.db import models
from uuid import uuid4


class Footer(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    contact_details = models.CharField(max_length=64)
    copyright = models.CharField(max_length=64)

