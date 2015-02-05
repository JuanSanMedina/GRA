# sudo du -sh /
# python manage.py shell_plus --notebook
# python manage.py runserver 128.122.72.105:8000
# https://docs.djangoproject.com/en/1.7/topics/db/queries/#field-lookups-intro
# http://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/
# https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding
#  python manage.py reset_db
# python ../../../manage.py shell_plus --notebook
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
	user = models.ForeignKey(User,blank=True, null=True)
	im = models.ImageField(upload_to='back_ground/')
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	def __unicode__(self):
		return str(self.pk)

class Item(models.Model):
	ecan = models.ForeignKey(Ecan)
	bg = models.ForeignKey(Back_Ground, null = True)
	user = models.ForeignKey(User,blank=True, null=True)
	im = models.ImageField(upload_to='pi_cam/')
	weight = models.CharField(max_length=255, blank=True, null=True)
	item_class = models.CharField(max_length=255, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	# image_usb = models.ImageField(upload_to="usb_im", blank=True, null=True)
	def __unicode__(self):
		return str(self.pk)

class Sample(models.Model):
	ecan = models.ForeignKey(Ecan)
	user = models.ForeignKey(User,blank=True, null=True)
	im = models.ImageField(upload_to='sample/', blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	def __unicode__(self):
		return str(self.pk)











# def get_path(instance, filename):
# 	if not instance.id:
# 		instance.save()
# 	return 'picam/%s/.jpg' % instance.id


	# def save(self, *args, **kwargs):
	# 	if self.pk is None:
	# 		saved_image = self.image_picam
	# 		print saved_image
	# 		self.image_picam= None
	# 		super(Item, self).save(*args, **kwargs)
	# 		self.image_picam = saved_image
	# 		print saved_image
	# 	super(Item, self).save(*args, **kwargs)
	# def save(self, *args, **kwargs):
	# 	if self.pk is None:
	# 		saved_image_picam = self.image_picam
	# 		saved_image_usb = self.image_usb
	# 		self.image_picam = None
	# 		self.image_usb = None
	# 		super(Item, self).save(*args, **kwargs)
	# 		self.image_picam = saved_image_picam
	# 		self.image_usb = saved_image_usb
	# 	super(Item, self).save(*args, **kwargs)
