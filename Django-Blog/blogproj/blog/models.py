from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField(default="Intro")
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)
    def get_absolute_url(self):
        return reverse('blog-home')