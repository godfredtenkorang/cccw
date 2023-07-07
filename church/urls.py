from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('event/', views.event, name='event'),
    path('event_detail/<slug>/', views.event_detail, name='event-detail'),
    path('event_view/<slug>/', views.event_view, name='event-view'),
    path('gallery/', views.gallery, name='gallery'),
    path('our_pastors/', views.paster, name='pastor'),
    path('youtube/', views.youtube, name='youtube'),
    path('ministry/', views.ministry, name='ministry'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<slug>/', views.blog_detail, name='blog-detail'),
    path('blog_view/<slug>/', views.blog_view, name='blog-view'),
    path('post_detail/<slug>/', views.post_detail, name='post-detail'),
    path('contact/', views.contact, name='contact'),
    path('donate/', views.donate, name='donate'),
]
