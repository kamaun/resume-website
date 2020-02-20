from django.shortcuts import render
from resume.models import Profile
from .models import BlogTittle, References

# Create your views here.


def maintenance(request):
    return render(
        request=request,
        template_name='blog/maintenance.html',
        context={
            'title': 'Maintenance'
        }
    )


def blog_summary(request):
    return render(
        request=request,
        template_name='blog/summary.html',
        context={
            'title': 'Blog',
            'profile': Profile.objects.first(),
            'blogs': BlogTittle.objects.all(),
            # 'references': References,
        }
    )


def blog_detail(request, title):
    blog_post = BlogTittle.objects.get(topic=title, topic__contains=title)
    return render(
        request=request,
        template_name='blog/blog_detail.html',
        context={
            'title': 'Blog',
            'profile': Profile.objects.first(),
            'blog': blog_post,
            'references': References.objects.filter(post_title=blog_post),
        }
    )