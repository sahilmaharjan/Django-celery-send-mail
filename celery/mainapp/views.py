from django.shortcuts import render, HttpResponse
from .tasks import test_func
from sendmail.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse('Done')

def send_mail(request):
    send_mail_func.delay()
    return HttpResponse('sent')

def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 10, minute=49)
    task = PeriodicTask.objects.create(crontab =schedule, name='schedule_mail'+'7',task= 'sendmail.tasks.send_mail_func')
    return HttpResponse('DONE')