from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.maintenance, name='blog_main'),
    path('summary', views.blog_summary, name='summary'),
    path('<str:title>', views.blog_detail, name='blog_detail')

]