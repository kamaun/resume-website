import os
from django.db import models
from django.utils import timezone
from datetime import datetime, date


def get_blog_image_url(instance, filename):
    return os.path.join('blog/profile', str(instance.id), filename)


# Create your models here.

class BlogTittle(models.Model):
    date = models.DateField(auto_now_add=True)
    topic = models.CharField(max_length=100)

    class Meta:
        managed = True
        app_label = 'blog'
        verbose_name = 'Blog Title'

    def __str__(self):
        return f'{self.topic}'


class BlogPost(models.Model):
    post_title = models.ForeignKey('BlogTittle', on_delete=models.CASCADE)
    post = models.TextField()

    class Meta:
        managed = True
        app_label = 'blog'
        verbose_name = 'Blog Post'

    def __str__(self):
        return self.post[:100]


class References(models.Model):
    post_title = models.ForeignKey('BlogTittle', on_delete=models.CASCADE)
    author = models.CharField(max_length=30, blank=True)
    date = models.DateField(blank=True)
    reference_title = models.CharField(max_length=100, blank=True)
    is_web_page = models.BooleanField(default=False)
    is_book = models.BooleanField(default=False)
    web_page = models.URLField(verbose_name='Web Page', blank=True)
    website = models.URLField(verbose_name='Web Site', blank=True)
    chapter = models.CharField(max_length=100, blank=True)
    page_number = models.IntegerField(blank=True)

    class Meta:
        managed = True
        app_label = 'blog'
        verbose_name = 'Blog Title'

    def __str__(self):
        return f'{self.reference_title} by {self.author}'


class BlogPictures(models.Model):
    post_title = models.ForeignKey('BlogTittle', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to=get_blog_image_url)

    class Meta:
        managed = True
        app_label = 'blog'
        verbose_name = 'Blog Pictures'

    def __str__(self):
        return self.post_title
