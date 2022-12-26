from django.db import models

# Create your models here.
class Client(models.Model):
    client_name     = models.CharField(max_length=200)
    whatsapp_no     = models.CharField(max_length=200)
    makeup_catagory = models.CharField(max_length=200)
    have_siders     = models.BooleanField(default=False)
    sider_count     = models.IntegerField(default=False)
    created_by      = models.CharField(max_length=256)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    pass

class Sider(models.Model):
    pass

class Payment(models.Model):
    total_amount      = models.CharField(max_length=200)
    paid_amount       = models.CharField(max_length=200)
    remaining_amount  = models.CharField(max_length=200)
    payment_method    = models.CharField(max_length=200)
    pass

