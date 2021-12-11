from django.db import models
from django.db.models.expressions import F
from core import settings
from accounts.models import User,MyAccountManager
from django.core.exceptions import ValidationError
# Create your models here.

class Store(models.Model):



    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True,null=False)


    def __str__(self):
        return '{}:{}'.format(self.id,self.name)


