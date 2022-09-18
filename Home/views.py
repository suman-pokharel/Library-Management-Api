import datetime
from datetime import date
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from Home.models import Borrow

# Create your views here.


def send_emails(request):
    obj=Borrow.objects.filter(return_date=date.today()).values()
    if Borrow.objects.filter(return_date=date.today()):
        obj=Borrow.objects.filter(return_date=date.today()).values()
        subject = 'Library Membership Alert'
        # message = "Hi " + obj.student['first_name'] + ", Today is your last date. Please return issued book. "
        # recipient_email = obj.student['email']
        message = "Hi " + 'Ram' + ", Today is your last date. Please return issued book. "
        recipient_email = obj.student['sumanpokharel8@gmail.com']
        send_mail( subject, message, 'library.sagarmatha@gmail.com',[ recipient_email], fail_silently=False )
        return HttpResponseRedirect('/send_email?submitted=True') 
