from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'get_html_photo', 'is_published', 'is_pinned')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'get_html_photo', 'photo', 'is_published',
              'is_pinned', 'time_create', 'time_update')
    list_editable = ('is_published', 'is_pinned')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, obj: Post):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=75>')
        return None

    get_html_photo.short_description = 'Фото на данный момент'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author')
    list_display_links = ('id', 'post', 'author')
    search_fields = ('author',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_html_photo')
    list_display_links = ('id', 'user', 'get_html_photo')
    search_fields = ('author',)

    def get_html_photo(self, obj: UserProfile):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width=75>')
        return None

    get_html_photo.short_description = 'Фото'


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Category, CategoryAdmin)
