import os
from django.db import models
from django.utils import timezone
from datetime import datetime, date


def get_blog_image_url(instance, filename):
    return os.path.join('blog/profile', str(instance.id), filename)


# Create your models here.

class BlogTittle(models.Model):
    # date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField('date published')
    topic = models.CharField(max_length=100)
    post = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'blog'
        verbose_name = 'Blog Title'

    def __str__(self):
        return f'{self.topic}'

    def short_post(self):
        return f'{self.post[:300]}...'

    def full_post(self):
        return self.post


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
    is_web_page = models.BooleanField(default=False, verbose_name='Is is a web page?')
    web_page = models.URLField(verbose_name='Web Page', blank=True)
    website = models.URLField(verbose_name='Web Site', blank=True)
    is_book = models.BooleanField(default=False, verbose_name='Is it a book')
    book_name = models.CharField(max_length=100, blank=True)
    chapter = models.CharField(max_length=100, blank=True)
    page_number = models.IntegerField(blank=True, null=True)
    is_report = models.BooleanField(default=False, verbose_name='Is it a report?')
    report_name = models.CharField(max_length=100, blank=True)



    class Meta:
        managed = True
        app_label = 'blog'
        verbose_name = 'Reference'

    def __str__(self):
        return f'{self.reference_title} by {self.author}'


class BlogPictures(models.Model):
    post_title = models.ForeignKey('BlogTittle', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to=get_blog_image_url)
    caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'blog'
        verbose_name = 'Blog Picture'

    def __str__(self):
        return self.post_title
