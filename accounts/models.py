from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class MyUser(AbstractBaseUser):
    email      = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    fullname    = models.CharField(max_length=256,null=True,blank=True)
    is_admin    = models.BooleanField(default=False)
    is_manager  = models.BooleanField(default=False)
    profile_pic = models.ImageField(null=True,blank=True)
    contact_no  = models.CharField(max_length=256)
    whatsapp_no = models.CharField(max_length=256) 
    created_at  = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at  = models.DateTimeField(auto_now=True)
    password    = models.CharField(max_length=256)
    objects     = UserManager()
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

class Banner(models.Model):
    title        = models.CharField(max_length=256)
    image        = models.ImageField()
    description  = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at   = models.DateTimeField(auto_now=True)


class Testimonials(models.Model):
    name           = models.CharField(max_length=256)
    profile_pic    = models.ImageField()
    address        = models.CharField(max_length=256)
    description    = models.TextField()
    created_at     = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at     = models.DateTimeField(auto_now=True)


class Product(models.Model):
    product_name          = models.CharField(max_length=256)
    product_price         = models.CharField(max_length=256)
    product_image         = models.ImageField()
    created_at            = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at            = models.DateTimeField(auto_now=True)


