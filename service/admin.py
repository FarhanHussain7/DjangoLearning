from django.contrib import admin

from .models import Service, Contact, News

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'contact_image')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','news_image', 'slug')

# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(Contact)
admin.site.register(News, NewsAdmin)