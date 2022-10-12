from django.conf import settings  # reading conf
from django.db import models
from django.utils import timezone
# for authentifications.
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=20, default='Nature Lifestyle')
    
    class Meta:
        # ordering
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    image = models.ImageField(default=None, upload_to='post_images/')

    class Meta:
        # ordering
        ordering = ['-publish']
        # add index
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created']), ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
