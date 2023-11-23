from django.db import models

# Create your models here.

class NoteRecord(models.Model):
    header = models.CharField(max_length=10, unique=True)
    body = models.CharField(max_length=4096) #hello, Telegram
    release_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    access_show = models.PositiveSmallIntegerField(default=0)
    access_comment = models.PositiveSmallIntegerField(default=0)
