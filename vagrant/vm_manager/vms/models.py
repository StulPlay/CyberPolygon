
from django.db import models

class VirtualMachine(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=100, default='stopped')

    def __str__(self):
        return self.name