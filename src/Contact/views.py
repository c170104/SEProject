from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from . import form
from django.core.mail import send_mail
from smtplib import SMTPException
from django.utils.html import escape

# Create your views here.

@csrf_exempt
def index(request):
    success_msg = ''
    error_msg = ''
    if request.method == 'POST':
        f = form.contactForm(request.POST)
        if f.is_valid():
            try:
                email_content = "\nEnquirer Name: " + f.cleaned_data['lname'] + " " + f.cleaned_data['fname'] + "\n\nEnquiry: " + f.cleaned_data['enquiry'] + "\n\n"
                send_mail(
                    f.cleaned_data['subject'],
                    escape(email_content),
                    'test_admin@villians.ntu.edu.sg',
                    [f.cleaned_data['email']],
                    fail_silently = False,
            )
                success_msg = "Succesfully sent enquiry. We well get back to you as soon as possible."
            except SMTPException as e:
                print(e.strerror)
                error_msg = "Failed to send enquiry. Please try again."
        else:
            error_msg = "Invalid inputs. Try again."
            

    return render(request, 'contact/index.html', {'active_page': 'contact', 'success_msg': success_msg, 'error_msg': error_msg})
