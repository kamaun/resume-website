from django.shortcuts import render

# Create your views here.


def maintenance(request):
    return render(
        request=request,
        template_name='blog/maintenance.html',
        context={
            'title': 'Maintenance'
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