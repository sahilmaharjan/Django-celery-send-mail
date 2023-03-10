from django.db.models.signals import pre_init, post_init, pre_save, pre_delete, post_delete, post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.backends.signals import connection_created

@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("----------------")
    print("PRE SAVE signal----------")
    print('sender', sender)
    print('instance', instance)
    print(f'kwargs:{kwargs}')

@receiver(post_save, sender=User)
def at_end_save(sender, created, instance, **kwargs):
    if created:
        print("----------------")
        print("POST SAVE signal NEW RECORD----------")
        print('sender', sender)
        print('instance', instance)
        print('created', created)
        print(f'kwargs:{kwargs}')
    else: 
        print("----------------")
        print("POST SAVE signal UPDATE----------")
        print('sender', sender)
        print('created', created)
        print(f'kwargs:{kwargs}')   



@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("----------------")
    print("Pre delete signal ----------")
    print('sender', sender)
    print('instance', instance)
    print(f'kwargs:{kwargs}')

@receiver(post_delete, sender=User)
def at_end_delete(sender, instance, **kwargs):
    print("----------------")
    print("Post delete signal ----------")
    print('sender', sender)
    print('instance', instance)
    print(f'kwargs:{kwargs}')



@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("----------------")
    print("Pre delete signal ----------")
    print('sender', sender)
    print('args', args)
    print(f'kwargs:{kwargs}')

@receiver(post_init, sender=User)
def at_end_init(sender, *args, **kwargs):
    print("----------------")
    print("Post init signal ----------")
    print('sender', sender)
    print('args', args)
    print(f'kwargs:{kwargs}')


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print('------------------------------------------')
    print('Initial connection to the database ....')
    print('sender', sender)
    print('connection', connection)
    print(f'kwargs: {kwargs}')