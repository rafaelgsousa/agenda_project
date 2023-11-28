import uuid

from django.db import models
from django.utils import timezone


#exemplo de model
# Create your models here.
class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    # category = models.ForeignKey('auth.Category', related_name='internal', on_delete=models.CASCADE)
    show = models.BooleanField(default=True)
    # owner = models.ForeignKey('auth.User', related_name='internal', on_delete=models.CASCADE)

    def __str__(self):
        return self.name