from django.db import models
from django.utils import timezone


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