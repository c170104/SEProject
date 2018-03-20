from django.shortcuts import render
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from . import form
from django.core.mail import send_mail
from smtplib import SMTPException

# Create your views here.

@csrf_exempt
def index(request):
    success_msg = ''
    error_msg = ''
    if request.method == 'POST':
        f = form.contactForm(request.POST)
        if f.is_valid():
            try:
                send_mail(
                    request.POST.get('subject'),
                    request.POST.get('enquiry') + request.POST.get('email'),
                    'test_admin@villians.ntu.edu.sg',
                    ['randomemail12345@villians.ntu.edu.sg'],
                    fail_silently = False,
            )
                success_msg = "Succesfully sent enquiry. We well get back to you as soon as possible."
            except SMTPException as e:
                print(e.strerror)
                error_msg = "Failed to send enquiry. Please try again."
        else:
            error_msg = "Invalid inputs. Try again."
            

    return render(request, 'contact/index.html', {'active_page': 'contact', 'success_msg': success_msg, 'error_msg': error_msg})
