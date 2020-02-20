from django.contrib import admin
from .models import BlogTittle, BlogPictures, BlogPost, References


# admin view settings


class PicturesInline(admin.TabularInline):
    model = BlogPictures
    extra = 1


class ReferencesInline(admin.StackedInline):
    model = References
    extra = 1


class PostInline(admin.TabularInline):
    model = BlogPost
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    inlines = [PicturesInline, ReferencesInline]
    list_display = ['topic', 'date']
    fieldsets = [
        ('Title and Post', {
            'fields': ['topic', 'date', 'post']
        })
    ]


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['reference_title', 'date', 'author']
    fieldsets = [
        (None, {
            'fields': ['reference_title', ('author', 'date')]
        }),
        ('Source', {
            'fields': [
                ('is_web_page'), ('web_page', 'website'),
                ('is_book'), ('chapter', 'page_number'),
                ('is_report', 'report_name')
            ]
        })
    ]


# Register your models here.
admin.site.register(BlogTittle, BlogAdmin)
admin.site.register(BlogPost)
admin.site.register(BlogPictures)
admin.site.register(References, ReferenceAdmin)
