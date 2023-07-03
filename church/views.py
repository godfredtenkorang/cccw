from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def home(request):
    events = HomeEvent.objects.all()
    blogs = HomeBlog.objects.all()
    posts = Post.objects.all()
    context = {
        'events': events,
        'blogs': blogs,
        'posts': posts
    }
    return render(request, 'church/home.html', context)

def about(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'About'
    }
    return render(request, 'church/about.html', context)

def event(request):
    myevents = Event.objects.all()
    posts = Post.objects.all()
    context = {
        'myevents': myevents,
        'posts': posts,
        'title': 'Events'
    }
    return render(request, 'church/event.html', context)

def event_view(request, slug):
    myevent = Event.objects.get(slug=slug)
    posts = Post.objects.all()
    context = {
        'myevent': myevent,
        'posts': posts,
        'title': 'Event Detail'
    }
    return render(request, 'church/event_view.html', context)

def event_detail(request, slug):
    event = HomeEvent.objects.get(slug=slug)
    posts = Post.objects.all()
    context = {
        'event': event,
        'posts': posts,
        'title': 'Event Detail'
    }
    return render(request, 'church/event_detail.html', context)

def gallery(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Gallery',
    }
    return render(request, 'church/gallery.html', context)

def youtube(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'YouTube'
    }
    return render(request, 'church/youtube.html', context)

def ministry(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'title': 'Ministry'
    }
    return render(request, 'church/ministry.html', context)

def blog(request):
    myblogs = Blog.objects.all()
    posts = Post.objects.all()
    context = {
        'myblogs': myblogs,
        'posts': posts,
        'title': 'Blogs'
    }
    return render(request, 'church/blog.html', context)

def blog_view(request, slug):
    myblog = Blog.objects.get(slug=slug)
    posts = Post.objects.all()
    context = {
        'myblog': myblog,
        'psots': posts,
        'title': 'Blog Detail'
    }
    return render(request, 'church/blog_view.html', context)

def blog_detail(request, slug):
    blog = HomeBlog.objects.get(slug=slug)
    posts = Post.objects.all()
    context = {
        'blog':blog,
        'posts': posts,
        'title': 'Blog Detail'
    }
    return render(request, 'church/blog_detail.html', context)

def contact(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()
        messages.success(request, "Your form is submitted")
        return redirect('contact')
    context = {
        'posts': posts,
        'title': 'Contact us'
    }
    return render(request, 'church/contact.html', context)

def donate(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'church/donate.html', context)
