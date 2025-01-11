from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Taskdb(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']


class RegisterDB(models.Model):
    Name = models.CharField(max_length=200, null=True, blank=True)
    Password = models.CharField(max_length=200, null=True, blank=True)
    Cpass = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Phone = models.CharField(max_length=20, null=True, blank=True)
