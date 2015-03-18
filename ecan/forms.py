from django.forms import ModelForm
from ecan.models import Item, Ecan, Back_Ground, Sample, Shape, Material, Brand, Description


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


class UploadBrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"


class UploadShapeForm(ModelForm):
    class Meta:
        model = Shape
        fields = "__all__"


class UploadMaterialForm(ModelForm):
    class Meta:
        model = Material
        fields = "__all__"


class UploadDescriptionForm(ModelForm):
    class Meta:
        model = Description
        fields = "__all__"
