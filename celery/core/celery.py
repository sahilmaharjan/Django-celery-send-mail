from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kathmandu')

app.config_from_object(settings, namespace= 'CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-at-2-everyday': {
        'task' : 'sendmail.tasks.send_mail_func',
        'schedule' : crontab(hour=14, minute=17)
    }
    
}
app.autodiscover_tasks()
@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')