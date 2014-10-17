from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from ecan.forms import UploadItemForm
from ecan.models import Ecan, Item 
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
		return render(request, 'ecan/home.html')

@csrf_exempt
def upload_item(request):
	if request.method == 'POST':
			form = UploadItemForm(request.POST, request.FILES)
			if form.is_valid():
				print 'valid'
				form.save()
				return HttpResponseRedirect('/success/url/')
	else:
			form = UploadItemForm()
	response_data = {}
	response_data['result'] = 'works'
	return HttpResponse(json.dumps(response_data), content_type="application/json")
