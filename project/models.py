from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    photo = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    url_github = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    last_change = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
