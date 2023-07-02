from django.shortcuts import render


def home(request):
    return render(request, 'church/home.html')

def about(request):
    return render(request, 'church/about.html')

def event(request):
    return render(request, 'church/event.html')

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
    return render(request, 'church/contact.html')

def donate(request):
    return render(request, 'church/donate.html')
