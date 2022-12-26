from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class MyUser(AbstractBaseUser):
    email      = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_admin   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    password   = models.CharField(max_length=256)
    objects    = UserManager()
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Admin(models.Model):
    email = models.EmailField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name   = models.CharField(max_length=256)
    