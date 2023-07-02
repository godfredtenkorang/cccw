from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('gallery/', views.gallery, name='gallery'),
    path('youtube/', views.youtube, name='youtube'),
    path('ministry/', views.ministry, name='ministry'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/', views.blog_detail, name='blog-detail'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
]
