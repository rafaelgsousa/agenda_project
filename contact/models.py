import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


#exemplo de model
# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True)
    show = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='internal', on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, related_name='internal', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'