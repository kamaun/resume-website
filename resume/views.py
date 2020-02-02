from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404, HttpResponseRedirect, redirect
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import get_template
from django.views import generic
from django.template import Context, loader
from .models import *
from .forms import ContactForm


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
    profile = Profile.objects.first()
    return render(
        request=request,
        template_name='resume/resume.html',
        context={
            'title': 'Resume',
            'profile': Profile.objects.first(),
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
            'all_projects': all_projects,
            'personal_projects': all_projects.filter(personal=True),
            'work_projects': all_projects.filter(personal=False, job__isnull=False),
            'school_projects': all_projects.filter(personal=False, school__isnull=False),
            'all_tech_uses': TechUsed.objects.all(),
            'all_tasks': Task.objects.all(),
        }
    )


def project(request, project_id):
    current_project = get_object_or_404(Projects, id=project_id)
    tech_used = TechUsed.objects.filter(project=current_project)

    return render(
        request=request,
        template_name='resume/project.html',
        context={
            'title': 'Project',
            'current_project': current_project,
            'technologies': TechUsed.objects.filter(project=current_project),
            'tech_set_one': tech_used[:(int(len(tech_used) / 2))],
            'tech_set_two': tech_used[(int(len(tech_used) / 2)):],
            'tasks': Task.objects.filter(project=current_project),
        }
    )


def contact2(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['devkevengineer@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect('success')

    return render(
        request=request,
        template_name="resume/contact.html",
        context={
            'title': 'Contact',
            'form': form,
        }
    )


def contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email_address = contact_form.cleaned_data['email_address']
            phone_number = contact_form.cleaned_data['phone_number']
            message = contact_form.cleaned_data['message']

            message_body = f'''
                    Name: {name}
                    Email: {email_address}      Phone: {phone_number}
                    Message:
                            {message}
            '''

            html_body = f'''
                <section>
                    <div>
                        <h4>Name: {name}</h4>
                        <h5>Email: {email_address}</h5>
                        <h5>Phone Number: {phone_number}</h5>
                        <div id="email_message">
                            <h5>Message:<h5>
                            <br>
                            <p>{message}</p>
                        </div>
                    </div>
                </section>
            '''

            try:
                send_mail(
                    subject='[PORTFOLIO] New contact from website',
                    message=message_body,
                    from_email=email_address,
                    recipient_list=['devkevengineer@gmail.com'],
                    html_message=html_body,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('message_sent/')
    else:
        contact_form = ContactForm()

    return render(
        request=request,
        template_name="resume/contact.html",
        context={
            'title': 'Contact',
            'contact_form': contact_form,
        }
    )


def sent_email(request):
    return render(
        request=request,
        template_name='resume/contact_form_sent.html',
        context={
            'title': 'Email Sent'
        }
    )
