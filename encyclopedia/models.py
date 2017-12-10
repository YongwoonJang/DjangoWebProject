from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=50)
    csscontents = models.TextField()
    htmlcontents = models.TextField()
    javascriptcontents = models.TextField()
    
class Service(models.Model):
    menu = models.CharField(max_length=100)
