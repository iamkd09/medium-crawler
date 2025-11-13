from django.contrib import admin
from .models import Tag, Blog, Response

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'crawled_at')
    search_fields = ('title','creator')
    list_filter = ('crawled_at',)
    filter_horizontal = ('tags',)

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('author', 'blog')
    search_fields = ('author', 'content')
