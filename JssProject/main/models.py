from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #USER가 지워지면 그에 해당하는 자소서도 지워짐

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #USER가 지워지면 그에 해당하는 자소서도 지워짐
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)