from distutils.command.upload import upload


from django.conf import settings  # reading conf
from django.db import models
from django.utils import timezone
# for authentifications.
from django.contrib.auth.models import User

class LocalUser(User):
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=20,  null=True, blank=True)
    link = models.URLField(null=True, blank=True)

    class Meta:
        # ordering
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, default='Nature Lifestyle')
    link = models.URLField(null=True, blank=True)
    
    class Meta:
        # ordering
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        BANNER = 'BN','Banner'
        DEMO = 'DM','Demo'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    author = models.ForeignKey(LocalUser, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    image = models.ImageField(upload_to='post_images/')

    class Meta:
        # ordering
        ordering = ['-publish']
        # add index
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title
class Message(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject  = models.CharField(max_length=100)
    message = models.TextField()
    author = models.ForeignKey(LocalUser, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        indexes = [models.Index(fields=['created_at']), ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class Social(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(default='', blank=True)

    class Meta:
        # ordering
        ordering = ['title']

    def __str__(self):
        return self.title


class Banner(models.Model):
    name = models.CharField(max_length=10, default='', blank=True)
    title = models.CharField(max_length=50)
    page = models.CharField(max_length=50)
    slug = models.SlugField()
    author = models.ForeignKey(LocalUser, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        # ordering
        ordering = ['-name']

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    complement = models.CharField(max_length=50, default='', blank=True)
    mail = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name
