from django.db import models
# tinymce is a rich text editor for Django, and HTMLField is a field that allows you to store HTML content in the database. It provides a user-friendly interface for editing and formatting text, making it ideal for fields like descriptions or content that may require rich formatting.
from tinymce.models import HTMLField
# 
from autoslug import AutoSlugField

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = HTMLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

# another models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField() 

class News(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()
    slug = AutoSlugField(populate_from='title', unique=True, null=True, blank=True, default=None)
    

# python manage.py startup service
# python manage.py makemigrations
# python manage.py migrate