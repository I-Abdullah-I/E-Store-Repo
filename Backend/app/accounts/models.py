from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
    # We're passing the two required fields after 'self' which are 'email' and 'username'
    # For any other required field you should pass in those other fields  
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address!')
        # if not username:
        #     raise ValueError('Users must have a username!')
        # What is 'user?'
        user = self.model(
                email=self.normalize_email(email)
                # username=username,
            ) 

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
            # username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email               = models.EmailField(verbose_name='email', max_length=50, unique=True)
    full_name            = models.CharField(max_length=30)
    # first_name          = models.CharField(max_length=50, blank=True, null=True)
    # last_name           = models.CharField(max_length=50, blank=True, null=True)
    # address             = models.CharField(max_length=255, blank=True, null=True)
    # credit_card_number  = models.CharField(max_length=16, blank=True, null=True)
    ENDUSER, VENDOR, ADMIN = 'E', 'V', 'A'

    TYPES               = [(ENDUSER, 'End-user'), (VENDOR, 'Vendor'), (ADMIN, 'Admin')]
    type                = models.CharField(max_length=1, choices=TYPES, default='A')
    balance             = models.IntegerField(blank=True, null=True)
    # The following attributes are required for any custom user model 
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # These two functions can be just copied without careful thought
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta():
        verbose_name = 'Users'
        verbose_name_plural = 'Users'


# The following code snippet is responsible for saving a token for every new user 
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)