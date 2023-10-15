
from django.db import models
from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     author = models.CharField(max_length=100)

from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

