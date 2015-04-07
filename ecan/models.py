# sudo du -sh /
# https://docs.djangoproject.com/en/1.7/topics/db/queries/#field-lookups-intro
# http://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/
# https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding

from django.db import models
from django.contrib.auth.models import User
import os
from picklefield.fields import PickledObjectField
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import numpy as np
from PIL import Image
from cStringIO import StringIO
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from contextlib import closing


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


class Logo(models.Model):
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


class Common_Name(models.Model):
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
    logo = models.ForeignKey(Logo, blank=True, null=True)
    shape = models.ForeignKey(Shape, blank=True, null=True)
    material = models.ForeignKey(Material, blank=True, null=True)
    common_name = models.ForeignKey(Common_Name, blank=True, null=True)

    # Automatic
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    im = models.ImageField(upload_to='pi_cam/')
    thumb = models.ImageField(upload_to='thumbs/', blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)

    # User input
    transparency = models.CharField(max_length=255, blank=True, null=True)

    def create_thumbnail(self):
        # If there is no image associated with this.
        # do not create thumbnail
        if not self.im:
            return

        THUMBNAIL_SIZE = (80, 60)
        PIL_TYPE = 'jpeg'
        FILE_EXTENSION = 'jpg'

        # Open original photo which we want to thumbnail using PIL's Image
        with io.BytesIO(self.im.read()) as oim:
            image = Image.open(oim)
            image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)

            # Save the thumbnail
            with closing(StringIO()) as temp_handle:
                image.save(temp_handle, PIL_TYPE)
                temp_handle.seek(0)
                # Save image to a SimpleUploadedFile which can be saved into
                # ImageField
                suf = SimpleUploadedFile(os.path.split(self.im.name)[-1],
                                         temp_handle.read())
                # Save SimpleUploadedFile into image field
                self.thumb.save('%s_thumbnail.%s' % (
                                os.path.splitext(suf.name)[0],
                                FILE_EXTENSION), suf, save=False)

    def save(self):
        # create a thumbnail
        self.create_thumbnail()
        super(Item, self).save()

        with io.BytesIO(self.thumb.read()) as temp_handle:
            image = Image.open(temp_handle).convert('L')
            ft = np.array(image).flatten()
            d = {'scale': "1:8", "shape": [80, 60]}
            name = 'thumb_1:8'
            feat = Feature(
                name=name,
                description=d,
                feature=ft,
                item=self
            )
            feat.save(force_insert=True)

    def __unicode__(self):
        return str(self.pk)


class Feature(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)
    item = models.ForeignKey(Item)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = PickledObjectField()
    feature = PickledObjectField()

    def __unicode__(self):
        return str(self.pk)


@receiver(pre_delete, sender=Item)
def item_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.im.delete(False)
    instance.thumb.delete(False)
    instance.bg.im.delete(False)
