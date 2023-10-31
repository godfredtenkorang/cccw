from django.contrib import admin
from .models import *
from embed_video.admin import AdminVideoMixin

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(HomeEvent)
admin.site.register(Event)
admin.site.register(HomeBlog)
admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Gallery)
admin.site.register(YouTube, AdminVideo)
admin.site.register(LiveTv)
admin.site.register(Contact)
admin.site.register(Newsletter)
admin.site.register(Video)
admin.site.register(Pastor)
admin.site.register(Payment)
admin.site.site_header = "Church Admin"
admin.site.site_title = "Church Admin Area"
admin.site.index_title = "Welcome to the Church Admin Area"

class MinistryInLine(admin.TabularInline):
    model = Ministry
    extra = 1
  
  
class CategoryMinistryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['name']}), ('Date Information', {
        'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [MinistryInLine]
  
  
admin.site.register(MinistryCategory, CategoryMinistryAdmin)