from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def home(request):
    events = HomeEvent.objects.all()
    context = {
        'events': events
    }
    return render(request, 'church/home.html', context)

def about(request):
    return render(request, 'church/about.html')

def event(request):
    myevents = Event.objects.all()
    context = {
        'myevents': myevents,
        'title': 'Events'
    }
    return render(request, 'church/event.html', context)

def event_view(request, slug):
    myevent = Event.objects.get(slug=slug)
    context = {
        'myevent': myevent,
        'title': 'Event Detail'
    }
    return render(request, 'church/event_view.html', context)

def event_detail(request, slug):
    event = HomeEvent.objects.get(slug=slug)
    context = {
        'event': event,
        'title': 'Event Detail'
    }
    return render(request, 'church/event_detail.html', context)

def gallery(request):
    return render(request, 'church/gallery.html')

def youtube(request):
    return render(request, 'church/youtube.html')

def ministry(request):
    return render(request, 'church/ministry.html')

def blog(request):
    return render(request, 'church/blog.html')

def blog_detail(request):
    return render(request, 'church/blog_detail.html')

def contact(request):
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
        'title': 'Contact us'
    }
    return render(request, 'church/contact.html', context)

def donate(request):
    return render(request, 'church/donate.html')
