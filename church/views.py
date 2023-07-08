from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from .models import *
from django.contrib import messages


def home(request):
    events = HomeEvent.objects.all()
    blogs = HomeBlog.objects.all()
    posts = Post.objects.all()
    video = Video.objects.all()
    category = request.GET.get('category')
    minstry = Ministry.objects.filter(category__name=category).first()
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministry': minstry,
        'ministries': ministries,
        'categories': categories,
        'events': events,
        'blogs': blogs,
        'posts': posts,
        'video': video,
    }
    return render(request, 'church/home.html', context)

def about(request):
    posts = Post.objects.all()
    category = request.GET.get('category')

    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'posts': posts,
        'title': 'About'
    }
    return render(request, 'church/about.html', context)

def event(request):
    myevents = Event.objects.all()
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'myevents': myevents,
        'posts': posts,
        'title': 'Events'
    }
    return render(request, 'church/event.html', context)

def event_view(request, slug):
    myevent = Event.objects.get(slug=slug)
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'categories': categories,
        'ministries': ministries,
        'myevent': myevent,
        'posts': posts,
        'title': 'Event Detail'
    }
    return render(request, 'church/event_view.html', context)

def event_detail(request, slug):
    event = HomeEvent.objects.get(slug=slug)
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'event': event,
        'posts': posts,
        'title': 'Event Detail'
    }
    return render(request, 'church/event_detail.html', context)

def gallery(request):
    posts = Post.objects.all()
    galleries = Gallery.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'posts': posts,
        'galleries': galleries,
        'title': 'Gallery',
    }
    return render(request, 'church/gallery.html', context)

def youtube(request):
    youtubes = YouTube.objects.all()
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'youtubes': youtubes,
        'posts': posts,
        'title': 'YouTube'
    }
    return render(request, 'church/youtube.html', context)

def ministry(request):
    category = request.GET.get('category')
    minstry = Ministry.objects.filter(category__name=category).first()
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    posts = Post.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministry': minstry,
        'ministries': ministries,
        'categories': categories,
        'posts': posts,
        'title': 'Ministry'
    }
    return render(request, 'church/ministry.html', context)

def blog(request):
    myblogs = Blog.objects.all()
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories':  categories,
        'myblogs': myblogs,
        'posts': posts,
        'title': 'Blogs'
    }
    return render(request, 'church/blog.html', context)

def blog_view(request, slug):
    myblog = Blog.objects.get(slug=slug)
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories':  categories,
        'myblog': myblog,
        'posts': posts,
        'title': 'Blog View'
    }
    return render(request, 'church/blog_view.html', context)

def blog_detail(request, slug):
    blog = HomeBlog.objects.get(slug=slug)
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'blog':blog,
        'posts': posts,
        'title': 'Blog Detail'
    }
    return render(request, 'church/blog_detail.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'post':post,
        'posts': posts,
        'title': 'Blog Detail'
    }
    return render(request, 'church/post_detail.html', context)

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
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    # if request.method == 'POST':
    #     email_address = request.POST['email_address']
    #     newsletter = Newsletter(email_address=email_address)
    #     newsletter.save()
    #     return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'posts': posts,
        'title': 'Contact us'
    }
    return render(request, 'church/contact.html', context)

def paster(request):
    pastors = Pastor.objects.all()
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'pastors': pastors,
        'ministries': ministries,
        'categories': categories,
        'posts':posts,
        'title': 'Donate'
    }
    return render(request, 'church/paster.html', context)

def donate(request):
    posts = Post.objects.all()
    category = request.GET.get('category')
    
    if category == None:
        ministries = Ministry.objects.order_by('image')
    else:
        ministries = Ministry.objects.filter(category__name=category)
    categories = MinistryCategory.objects.all()
    if request.method == 'POST':
        email_address = request.POST['email_address']
        newsletter = Newsletter(email_address=email_address)
        newsletter.save()
        return redirect('home')
    context = {
        'ministries': ministries,
        'categories': categories,
        'posts':posts,
        'title': 'Donate'
    }
    return render(request, 'church/donate.html', context)