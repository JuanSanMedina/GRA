from django.forms import ModelForm
from ecan.models import Item, Ecan, Back_Ground, Sample

class UploadItemForm(ModelForm):
	class Meta:
		model = Item
		fields = "__all__" 

class UploadBack_GroundForm(ModelForm):
	class Meta:
		model = Back_Ground
		fields = "__all__" 

class UploadEcanForm(ModelForm):
	class Meta:
		model = Ecan
		fields = "__all__" 

class UploadSampleForm(ModelForm):
	class Meta:
		model = Sample
		fields = "__all__" 