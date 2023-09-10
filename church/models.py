from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
import secrets
from .paystack import PayStack


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
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

class Pastor(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='paster-img')
    facebook = models.URLField(blank=True)
    gmail = models.URLField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    
    def __str__(self):
        return self.caption
    
class Payment(models.Model):
    amount = models.PositiveBigIntegerField()
    ref = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, null=True)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_created',)
        
    def __str__(self) -> str:
        return f"Payment: {self.amount}"
    
    def save(self, *args, **kwargs) -> None:
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)
    
    def amount_value(self) -> int:
        return self.amount * 101
    
    def verify_payment(self):
        paystack = PayStack()
        status, result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount'] / 101 == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False