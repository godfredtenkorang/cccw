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
