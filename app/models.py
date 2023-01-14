from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    num_view = models.IntegerField(null=True, blank=True)
    is_featured = models.BooleanField(default=True, blank=True)
    
    def __str__(self):
        return f"{self.title}({self.author.username})"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.post.title
    
    class Meta:
        ordering = ('-updated', '-created')


