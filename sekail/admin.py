from django.contrib import admin
from .models import User, Customer, Store, Device
from django.conf import settings

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Device)
