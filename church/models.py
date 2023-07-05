from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class HomeEvent(models.Model):
    image = models.ImageField(upload_to='home-event-img')
    title = models.CharField(max_length=100)
    content = models.TextField()
    organizer = models.CharField(max_length=50)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    time = models.DateTimeField(default=timezone.now)
    venue = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    slug = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return self.title
    
class Event(models.Model):
    image = models.ImageField(upload_to='home-event-img')
    title = models.CharField(max_length=100)
    content = models.TextField()
    organizer = models.CharField(max_length=50)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    time = models.DateTimeField(default=timezone.now)
    venue = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    slug = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return self.title
    
class HomeBlog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='home-blog-img')
    date = models.DateTimeField(default=timezone.now)
    slug = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='home-blog-img')
    date = models.DateTimeField(default=timezone.now)
    slug = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='home-blog-img')
    date = models.DateTimeField(default=timezone.now)
    slug = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery-img')
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added',]
    
    def __str__(self):
        return self.title
    
class YouTube(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()
    
    class Meta:
        ordering = ['-date_added',]
        
    def __str__(self):
        return self.title
    
class MinistryCategory(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name

class Ministry(models.Model):
    category = models.ForeignKey(MinistryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ministry-img')
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return str(self.category)
    
class Newsletter(models.Model):
    email_address = models.EmailField()
    
    def __str__(self):
        return str(self.email_address)
    
class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    
    def __str__(self):
        return self.caption