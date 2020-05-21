from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import *
from .forms import CustomContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
from django.contrib import messages
import requests


# Create your views here.
def index(request):
    account = get_object_or_404(profile, id=1)
    technologies = get_list_or_404(Technology)
    work_experience = get_list_or_404(WorkPlaces)
    projects = get_list_or_404(Projects)
    school = get_list_or_404(School)
    sections = [cat[0] for cat in category()]

    return render(request, 'main/index.html', {
        'profile': account,
        'technologies': technologies,
        'work_experience': work_experience,
        'schools': school,
        'projects': projects,
        'category': sections[:3],
        'category2': sections[3:],
    })


def projects(request):
    projects = get_list_or_404(Projects)[::2]
    projects2 = get_list_or_404(Projects)[1::2]
    techs_used = get_list_or_404(TechUsed)
    task = get_list_or_404(Task)

    return render(request, 'main/projects.html', {
        'projects': projects,
        'projects2': projects2,
        'techs_used': techs_used,
        'tasks': task,
    })


def projectdetails(request, projectid):
    project = get_object_or_404(Projects, projectid=projectid)
    technology = get_list_or_404(TechUsed, project=project)[::2]
    technology2 = get_list_or_404(TechUsed, project=project)[1::2]
    tasks = get_list_or_404(Task, project=project)

    return render(request, 'main/projectdetails.html', {
        'project': project,
        'TechUse1': technology,
        'TechUse2': technology2,
        'tasks': tasks,
    })


def other(request):
    work = get_list_or_404(WorkPlaces, extra=True)

    return render(request=request, template_name='main/other.html', context={
        'work_experience': work,
    })


def ContactSentView(request):
    return render(request=request, template_name='contact_form/contact_form_sent.html')


def ContactView(request):
    account = get_object_or_404(profile, pk=1)

    if request.method == 'POST':
        form = CustomContactForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            name = data.get('name')
            subject = data.get('subject')
            from_email = data.get('from_email')
            message = data.get('message')

            template = get_template('contact_form/contact_form.txt')

            context = {
                'name': name,
                'subject': subject,
                'from_email': from_email,
                'message': message,
            }

            email_body = template.render(context)
            email = EmailMessage(
                subject='New contact form submission',
                body=email_body,
                from_email='devkevengineer@gmail.com',
                to=['devkevengineer@gmail.com'],
                reply_to=[from_email]
            )

            email.send()
            messages.success(request, f"Thank you! Your message has been sent...")
            return redirect("/contact/")
    else:
        form = CustomContactForm()

    return render(request=request, template_name='contact_form/contact_form.html', context={
        'account': account,
        'form': form,
    })


