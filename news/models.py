from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=32, null=False)