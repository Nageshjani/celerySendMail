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