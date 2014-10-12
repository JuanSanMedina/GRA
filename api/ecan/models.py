from django.db import models
from django.contrib.auth.models import User

class Ecan(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

class Item(models.Model):
    ecan = models.ForeignKey(Ecan)
    user = models.ForeignKey(User,blank=True, null=True)
    image_color = models.ImageField(upload_to="items")
    image_ir = models.ImageField(upload_to="recognition")
    weight = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)