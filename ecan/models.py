# sudo du -sh /
# https://docs.djangoproject.com/en/1.7/topics/db/queries/#field-lookups-intro
# http://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/
# https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding

from django.db import models
from django.contrib.auth.models import User
import os


class Ecan(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return self.address


class Back_Ground(models.Model):
    ecan = models.ForeignKey(Ecan)
    user = models.ForeignKey(User, blank=True, null=True)
    im = models.ImageField(upload_to='back_ground/')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)


class Sample(models.Model):
    ecan = models.ForeignKey(Ecan)
    user = models.ForeignKey(User, blank=True, null=True)
    im = models.ImageField(upload_to='sample/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)


class Brand(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)


class Shape(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)


class Material(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)


class Description(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)


class Item(models.Model):
    # Foreing
    ecan = models.ForeignKey(Ecan)
    bg = models.ForeignKey(Back_Ground, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    brand = models.ForeignKey(Brand, blank=True, null=True)
    shape = models.ForeignKey(Shape, blank=True, null=True)
    material = models.ForeignKey(Material, blank=True, null=True)
    description = models.ForeignKey(Description, blank=True, null=True)

    # Automatic
    im = models.ImageField(upload_to='pi_cam/')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)

    # User input
    identifier = models.CharField(max_length=255, blank=True, null=True)
    transparency = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return str(self.pk)
