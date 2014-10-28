from django.db import models
from django.contrib.auth.models import User

class Ecan(models.Model):
	address = models.CharField(max_length=255, blank=True, null=True)
	ip = models.CharField(max_length=255, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	def __unicode__(self):
		return self.address

class Item(models.Model):
	ecan = models.ForeignKey(Ecan)
	user = models.ForeignKey(User,blank=True, null=True)
	image_picam = models.ImageField(upload_to="picam_im", blank=True, null=True)
	image_usb = models.ImageField(upload_to="usb_im", blank=True, null=True)
	weight = models.CharField(max_length=255, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	def __unicode__(self):
		return self.weight
	def save(self, *args, **kwargs):
		if self.pk is None:
			saved_image_picam = self.image_picam
			saved_image_usb = self.image_usb
			self.image_picam = None
			self.image_usb = None
			super(Item, self).save(*args, **kwargs)
			self.image_picam = saved_image_picam
			self.image_usb = saved_image_usb
		super(Item, self).save(*args, **kwargs)