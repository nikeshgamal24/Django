from django.contrib import admin
from .models import Item

# Register your models here.
#we register the model that we want to show in the superuser/ superadmin panel

admin.site.register(Item)