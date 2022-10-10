from uuid import uuid4
from django.db import models
from usersapp.models import User

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.UUIDField(default=uuid4)
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)


class TODO(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(verbose_name='Заметка', blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    is_active = models.BooleanField(verbose_name='активация', default=True)
    project = models.ForeignKey(Project, verbose_name='uid проекта',
                                on_delete=models.PROTECT, null=True, related_name='project')