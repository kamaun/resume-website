from django.urls import path
from . import views

app_name = 'resume'
urlpatterns = [
    path('', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('contact/', views.maintenance, name='contact'),
]
