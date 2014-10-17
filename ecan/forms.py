from django.forms import ModelForm
from ecan.models import Item

class UploadItemForm(ModelForm):
	class Meta:
		model = Item