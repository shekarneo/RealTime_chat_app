from django.contrib import admin
from .models import Post
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/created_date/published_date", {'fields': ["title", "created_date", "published_date"]}),
        ("Content", {"fields": ["content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Post,PostAdmin)