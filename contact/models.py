from django.db import models
from django.utils.timezone import now as current_date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Categories'
            
    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    created_at = models.DateTimeField(default=current_date)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    
    
    #toString
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'