from django.db import models


# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=100)
    name_book = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_picture_book = models.ImageField(upload_to='images/')
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name