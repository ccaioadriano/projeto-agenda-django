from django.db import models
from django.utils.timezone import now as current_date
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default=current_date)