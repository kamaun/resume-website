from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404, HttpResponseRedirect, redirect
from django.core.mail import send_mail, BadHeaderError
from django.views import generic
from django.template import Context, loader
from .models import *
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def maintenance(request):
    return render(
        request=request,
        template_name='resume/maintenance.html',
        context={
            'title': 'Maintenance'
        }
    )


def resume(request):
    return render(
        request=request,
        template_name='resume/resume.html',
        context={
            'title': 'Resume',
            'profile': Profile,
            'jobs': WorkPlaces.objects.filter(extra=False).order_by('-id'),
            'other_jobs': WorkPlaces.objects.filter(extra=True).order_by('-id'),
            'schools': School.objects.order_by('-from_year', '-from_month'),
            'technologies': Technology.objects.all().order_by('-proficiency'),
            'cat_set_one': [cat[0] for cat in category()][:int((len(category())) / 2)],
            'cat_set_two': [cat[0] for cat in category()][int((len(category())) / 2):],
            'certificates': Certification.objects.all().order_by('-cert_year', '-cert_month')
        }
    )


def portfolio(request):
    all_projects = Projects.objects.all().order_by('-from_year', '-from_month', '-id')

    return render(
        template_name='resume/portfolio.html',
        request=request,
        context={
            'title': 'Portfolio',
            'personal_projects': all_projects.filter(personal=True),
            'work_projects': all_projects.filter(personal=False, job__isnull=False),
            'school_projects': all_projects.filter(personal=False, school__isnull=False),
            'tech_used': TechUsed.objects.all(),
            'tasks': Task.objects.all(),
        }
    )


def project(request, project_id):
    current_project = get_object_or_404(Projects, id=project_id)
    techused = TechUsed.objects.filter(project=current_project)


    return render(
        request=request,
        template_name='resume/project.html',
        context={
            'title': 'Project',
            'current_project': current_project,
            'technologies': TechUsed.objects.filter(project=current_project),
            'tech_set_one': techused[:(int(len(techused)/2))],
            'tech_set_two': techused[(int(len(techused)/2)):],
            'tasks': Task.objects.filter(project=current_project),
        }
    )


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(subject, message, from_email, ['devkevengineer@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(
        request=request,
        template_name="resume/contact.html",
        context={
            'title': 'Contact',
            'form': form,
        }
    )