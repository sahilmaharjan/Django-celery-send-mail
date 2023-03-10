from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from core import settings
from django.utils import timezone
from datetime import timedelta

# SEND MAIL TO ALL USERS INSTANTLY
@shared_task(bind = True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    # timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Hi! Celery Testing"
        mail_message = "mail send in mailtrap latest. schedule mail"
        to_email = user.email
        send_mail(
            subject= mail_subject,
            message= mail_message,
            from_email= settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently= True,
        )
    return 'Done'

