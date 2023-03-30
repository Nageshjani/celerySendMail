```bash
project/
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


INSTALLED_APPS = [
   
    'app'
]

```
## REDIS CONFIG

## sh 578
```bash
'Open Your Redis File'
'Double Click on redis-server'
'Double Click on redis-cli'
```

## 579
## 580
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
import time
  
@shared_task(bind=True)  
def test_func(self):  
    time.sleep(5)
    for i in range(10):  
        print(i)  
        time.sleep(1)
    return "Completed"  

```   
    
## app/views.py 
```python
from django.shortcuts import render
from django.http import HttpResponse  
from project.tasks import test_func  
  
  
def test(request):  
    test_func.delay()  
    return HttpResponse("Done")
    
```

## project/urls.py  
```python
from app.views import test

urlpatterns = [
    path('',test)
]
```


## ss 581
```bash
celery -A my_project_name worker --pool=solo -l info
```
```bash
'Add Your Project Name in place of my_project_name'
```

```bash
python manage.py runserver
```

```bash
'go to url http://127.0.0.1:8000/
```
## ss 582
## ss 583

celery -A project worker --pool=solo -l info
