
from django.shortcuts import render
from django.http import HttpResponse
from app.tasks import send_email_task 

def send_email(request):
    subject = 'Test email'
    message = 'This is a test email sent using Django Celery Redis'
    from_email = 'nsemcxgod@gmail.com'
    
    recipient_list = ['nsemcxgod@gmail.com']
                              
    send_email_task.delay(subject, message, from_email, 
                                               recipient_list)
    return HttpResponse("Email has been sent!")