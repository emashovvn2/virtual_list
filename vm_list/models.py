from django.db import models
from django.conf import settings

# Create your models here.

class Server(models.Model):
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(default='1.1.1.1')
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Vm(models.Model):
    server = models.ForeignKey('Server', on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    ip = models.GenericIPAddressField(default='1.1.1.1')
    state = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
