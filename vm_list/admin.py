from django.contrib import admin
from .models import Server
from .models import Vm

admin.site.register(Server)
admin.site.register(Vm)
# Register your models here.
