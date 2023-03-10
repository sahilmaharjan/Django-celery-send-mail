from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver



#CONNECTING/REGISTERING RECIEVER FUNCTION using DECORATORS(MOSTLY USED)
@receiver(user_logged_in, sender=User)

#RECIEVER FUNCTION for login
def login_success(sender, request, user, **kwargs):
    print("----------------")
    print("------logged in signal----------")
    print('sender', sender)
    print('request', request)
    print('user', user)
    print(f'kwargs:{kwargs}')

#CONNECTING/REGISTERING RECIEVER FUNCTION using MANUAL CONNECT ROUTE(LESS used) should be written outside the function
# user_logged_in.connect(login_success, sender=User)   


#CONNECTING/REGISTERING RECIEVER FUNCTION using DECORATORS(MOSTLY USED)
@receiver(user_logged_out, sender=User)

#RECIEVER FUNCTION for logout
def logout_success(sender, request, user, **kwargs):
    print("----------------")
    print("------logged out signal----------")
    print('sender', sender)
    print('request', request)
    print('user', user)
    print(f'kwargs:{kwargs}')




#CONNECTING/REGISTERING RECIEVER FUNCTION using DECORATORS(MOSTLY USED)
@receiver(user_login_failed)

#RECIEVER FUNCTION for logout
def login_failed(sender, credentials, request, **kwargs):
    print("----------------")
    print("------login failed signal----------")
    print('sender', sender)
    print('request', request)
    print('credentials', credentials)
    print(f'kwargs:{kwargs}')