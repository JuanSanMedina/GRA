from django.db import models
from django.contrib.auth.models import User

class Ecan(models.Model):
	address = models.CharField(max_length=255, blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	def __unicode__(self):
		return self.address

class Item(models.Model):
	ecan = models.ForeignKey(Ecan)
	user = models.ForeignKey(User,blank=True, null=True)
	image_color = models.ImageField(upload_to="color_im")
	image_ir = models.ImageField(upload_to="ir_im")
	weight = models.CharField(max_length=255, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	modified = models.DateTimeField(auto_now=True, blank=True, null=True)
	def __unicode__(self):
		return self.created