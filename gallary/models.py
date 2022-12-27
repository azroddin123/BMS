from django.db import models


class MakeUpArtist(models.Model):
    first_name    = models.CharField(max_length=256)
    last_name     = models.CharField(max_length=256)
    email         = models.EmailField(max_length=256)
    password      = models.CharField(max_length=256)
    profile       = models.ImageField()
    
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

class NormalImage(models.Model):
    uploaded_by   = models.CharField(max_length=256,blank=True,null=True)
    image         = models.ImageField()
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)


class BAImage(models.Model):
    before_image   = models.ImageField()
    after_image    = models.ImageField()
    uploaded_by    = models.CharField(max_length=256,blank=True,null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
   

class CatagoryImage(models.Model):
    image          = models.ImageField()
    uploaded_by    = models.CharField(max_length=256,blank=True,null=True)
    catagory_name  = models.CharField(max_length=200)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)
   
