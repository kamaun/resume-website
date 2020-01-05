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
    return render(
        request=request,
        template_name='resume/portfolio.html',
        context={
            'title': 'Portfolio',
            'projects': Projects.objects.all()
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


def project(request, project_id):
    return render(
        request=request,
        template_name='resume/project.html',
        context={
            'title': 'Project',
            'project': Projects.objects.filter(id=project_id)
        }
    )


def projects(request):
    projectscnt = get_list_or_404(Projects)
    num = len(projectscnt)
    if num % 2 == 0:
        p = int(num / 2)
    else:
        p = int(num / 2) + 1

    projects = get_list_or_404(Projects)[:p]
    projects2 = get_list_or_404(Projects)[p:num]
    techs_used = get_list_or_404(TechUsed)
    task = get_list_or_404(Task)
    context = {
        'projects': projects,
        'projects2': projects2,
        'techs_used': techs_used,
        'tasks': task,
    }
    template = 'Resume/projects.html'
    return render(request, template, context)


def projectdetails(request, projectid):
    project = get_object_or_404(Projects, projectid=projectid)
    techcnt = get_list_or_404(TechUsed, project=project)
    num = len(techcnt)
    if num % 2 == 0:
        p = int(num / 2)
    else:
        p = int(num / 2) + 1
    technology = get_list_or_404(TechUsed, project=project)[:p]
    technology2 = get_list_or_404(TechUsed, project=project)[p:num]
    tasks = get_list_or_404(Task, project=project)
    template = 'Resume/projectdetails.html'
    content = {
        'project': project,
        'TechUse1': technology,
        'TechUse2': technology2,
        'tasks': tasks,
    }
    return render(request, template, content)


def other(request):
    template = 'Resume/other.html'
    work = get_list_or_404(WorkPlaces, extra=True)
    content = {
        'work_experience': work,
    }
    return render(request, template, content)


def successView(request):
    return HttpResponse("You email has been sent! Thank you for reaching out!")
