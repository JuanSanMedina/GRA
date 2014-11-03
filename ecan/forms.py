from django.forms import ModelForm
from ecan.models import Item, Ecan

class UploadItemForm(ModelForm):
	class Meta:
		model = Item

class UploadEcanForm(ModelForm):
	class Meta:
		model = Ecan