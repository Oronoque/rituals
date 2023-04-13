from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group, related_name='app_users', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='app_users', blank=True)

class Ritual(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name 
    
class Step(models.Model):
    ritual = models.ForeignKey(Ritual, on_delete=models.CASCADE, related_name='steps')
    name = models.CharField(max_length=100)
    value = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=10, choices=[
        ('miles', 'Miles'),
        ('reps', 'Reps'),
        ('lbs', 'Lbs'),
        ('minute', 'Minutes')
    ], null=True, blank=True)
    photo = models.ImageField()
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
