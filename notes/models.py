from django.db import models

# Create your models here.

class NoteRecord(models.Model):
    header = models.CharField(max_length=100, unique=True)
    body = models.CharField(max_length=4096) #hello, Telegram
    release_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    access_show = models.PositiveSmallIntegerField(default=0)
    access_comment = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f'{self.id} {self.header[:5]}: {self.body[:5]}'

class NoteComment(models.Model):
    author_name = models.CharField(max_length=20)
    body = models.CharField(max_length=256)
    release_date = models.DateField(auto_now_add=True)
    note = models.ForeignKey(NoteRecord, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author_name[:5]} {self.body[:5]}'
