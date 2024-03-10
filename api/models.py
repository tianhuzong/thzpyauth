from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class SuperUsers(AbstractUser): 
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128, default='123456') 
    
    class Meta:
        verbose_name = 'Super User'
        verbose_name_plural = 'Super Users'

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )