from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404, HttpResponseRedirect, redirect
from django.core.mail import send_mail, BadHeaderError
from django.views import generic
from django.template import Context, loader
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def resume(request):
    template = 'Resume/index.html'
    account = get_object_or_404(Profile, pk=1)
    technologies = get_list_or_404(Technology)
    work_experience = get_list_or_404(WorkPlaces, extra=False)
    projects = get_list_or_404(Projects)
    school = get_list_or_404(School)

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

    content = {
        'account': account,
        'technologies': technologies,
        'work_experience': work_experience,
        'schools': school,
        'projects': projects,
        'category': [cat[0] for cat in category()][:3],
        'category2': [cat[0] for cat in category()][3:],
        'form': form,
    }

    return render(request, template, content)


def projects(request):
    projectscnt = get_list_or_404(Projects)
    num = len(projectscnt)
    if num % 2 == 0:
        p = int(num/2)
    else:
        p = int(num/2) + 1

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
        p = int(num/2)
    else:
        p = int(num/2) + 1
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


def emailview(request):
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
    return render(request, "Resume/contact.html", { 'form': form })


def successView(request):
    return HttpResponse("You email has been sent! Thank you for reaching out!")
