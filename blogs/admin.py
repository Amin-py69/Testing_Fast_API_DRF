from django.contrib import admin
from . import models


@admin.register(models.Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'publish')


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('create',)
    list_display = ('text', 'create', 'blogs')
