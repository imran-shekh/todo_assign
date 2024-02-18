from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.BooleanField(default=False)
    
    def __str__(self):
    return self.title


class CustomUser(AbstractUser):
    pass
