# from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    socialname = models.CharField(max_length=120)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    
    def __str__(self):
        return self.socialname