from django.db import models

# Create your models here.
class RestApp(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField()
    subtitle = models.CharField()