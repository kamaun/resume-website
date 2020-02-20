from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.home, name='portfolio'),
    path('profile/', views.resume, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('contact/message_sent/', views.sent_email, name='contact_sent')
]