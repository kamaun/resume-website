from django.urls import path, include
from django.views.generic import TemplateView
from contact_form.views import ContactFormView
from . import views
from .forms import CustomContactForm

app_name = "main"
urlpatterns = [
    path("", views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:projectid>', views.projectdetails, name='projectdetails'),
    path('other/', views.other, name='other'),
    path('contact/', views.ContactView, name='contact'),
    path('contact/sent/', views.ContactSentView, name='contact_sent')
]
