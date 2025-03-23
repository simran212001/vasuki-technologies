from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import HomeStats
from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'subject', 'created_at')  
    search_fields = ('name', 'email', 'subject')  
    list_filter = ('created_at',)  
    ordering = ('-created_at',)  


@admin.register(HomeStats)
class HomeStatsAdmin(admin.ModelAdmin):
    list_display = ('happy_clients', 'projects', 'hours_of_support', 'hard_workers')


from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'meta_description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
