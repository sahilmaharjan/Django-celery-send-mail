from django.urls import path, include
from .views import test, send_mail, schedule_mail

urlpatterns = [
    path('', test, name='test'),
    path('send-mail', send_mail, name='sendmail'),
    path('schedule-mail', schedule_mail, name='schedulemail'),
]
