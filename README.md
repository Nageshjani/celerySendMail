```bash
project/
│
locust/
├── locustfile.py
│
│
├── project/
│   ├── __init__.py 
│   ├── settings.py 
│   ├── celery.py 
│   ├── urls.py
|
├── app/
│   └── views.py
│   └── tasks.py
└── manage.py

```




```bash
pip install redis
```
```bash
pip install celery 
```
```bash
pip install locust
```

```bash
django-admin startproject project
```

```bash
cd project
```

```bash
python manage.py startapp app
```


## settings.py
```python
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379' 
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' 
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json'] 
CELERY_RESULT_SERIALIZER = 'json' 
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


INSTALLED_APPS = [
   
    'app'
]

```
## REDIS CONFIG


```bash
'Open Your Redis File'
'Double Click on redis-server'
'Double Click on redis-cli'
```
('https://user-images.githubusercontent.com/34247973/228630214-928a8264-d6e1-40fb-9ca9-8113a617caaa.png')

```bash
'Type ping in redis-cli'
'You should get PONG in reply'
```

## project/celery.py
```python
import os  
  
from celery import Celery  
from celery.schedules import crontab  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
#os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('project')  
app.config_from_object('django.conf:settings', namespace='CELERY')  
app.autodiscover_tasks()  
  
@app.task(bind=True)  
def debug_task(self):  
    print(f'Request: {self.request!r}')      
```
```bash
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
'add your project name'
```

```bash
app = Celery('project')  
'Your project_name'
```

## project/init.py 
```python
from .celery import app as celery_app
__all__ = ['celery_app']

```

## app/tasks.py 
```python
from celery import shared_task  
from django.core.mail import send_mail
  
@shared_task(bind=True)  
def send_email_task(self,subject, message, from_email, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )
    return 'Email Sent!'


```   
    
## app/views.py 
```python
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
    
```

## project/urls.py  
```python
from django.contrib import admin
from django.urls import path
from app.views import send_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mail/',send_email)
]

```

## locust/locustfile.py
```python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def my_task(self):
        self.client.get('http://127.0.0.1:8000/mail/')
        #self.client.get('/')

```

```bash
locust -f   locustfile.py
```
```bash
http://localhost:8089/
```
![image](https://user-images.githubusercontent.com/34247973/228896827-7296b374-8c54-4927-a32b-0a6a6320dc53.png)
![image](https://user-images.githubusercontent.com/34247973/228896900-757f7121-447d-4b20-b21e-60acfaae39a7.png)


```bash
celery -A my_project_name worker --pool=solo -l info
```


```bash
python manage.py runserver
```

```bash
'go to url http://127.0.0.1:8000/
```


celery -A project worker --pool=solo -l info

![image](https://user-images.githubusercontent.com/34247973/228895097-0f14219a-2167-46b6-a648-fb261ea56f91.png)
![image](https://user-images.githubusercontent.com/34247973/228895332-8ccd981d-25b1-4f0e-aaaf-a90aa7813d8f.png)
![image](https://user-images.githubusercontent.com/34247973/228895683-17f1c4e4-d5db-449d-bb25-43f1923d2d6a.png)



