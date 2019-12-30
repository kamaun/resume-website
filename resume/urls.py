from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.resume, name='resume'),
    path('portfolio/', views.maintenance, name='portfolio'),
    path('contact/', views.maintenance, name='contact'),
    path('project/<int:id>/', views.maintenance, name='project')
]