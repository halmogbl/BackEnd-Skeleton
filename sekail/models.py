from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_store = models.BooleanField(default=False)


class Device(models.Model):
    user = models.name = models.ForeignKey(User, related_name='devices', on_delete=models.CASCADE)
    iemi_id = models.CharField(max_length=100, unique=True)    


class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='store')
    phone_number = models.CharField(max_length=30)
  

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone_number = models.CharField(max_length=100)
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.is_store:
        Store.objects.get_or_create(user = instance)
    else:
        Customer.objects.get_or_create(user = instance)
    

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     print('_-----')	
#     if instance.is_store:
#         instance.store.save()
#     else:
#         Customer.objects.get_or_create(user = instance)