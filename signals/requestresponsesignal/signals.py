# from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.signals import request_started, request_finished, got_request_exception

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('-----------------------------------------')
    print('at beginning request signal')
    print('sender', sender)
    print('Environ',environ)
    print(f'kwargs : {kwargs}')

@receiver(request_finished)
def at_end_request(sender, **kwargs):
    print('-----------------------------------------')
    print('at end request signal')
    print('sender', sender)
    # print('Environ',environ)
    print(f'kwargs : {kwargs}')

@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print('-----------------------------------------')
    print('at request exception')
    print('sender', sender)
    print('request',request)
    print(f'kwargs : {kwargs}')