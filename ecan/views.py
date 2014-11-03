from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from ecan.forms import UploadItemForm, UploadEcanForm
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

			#do the processing here
			response_data = {}
			response_data['result'] = 'is valid'
			return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		form = UploadItemForm()
	response_data = {}
	response_data['result'] = 'get'
	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def upload_ecan(request):
	if request.method == 'POST':
		form = UploadEcanForm(request.POST, request.FILES)
		if form.is_valid():
			instance = get_object_or_404(Ecan, pk=request.POST['pk'])
			form = UploadEcanForm(request.POST or None, instance=instance)
			form.save()
			# #do the processing here
			# return "name = coke can"
			response_data = {}
			response_data['result'] = 'is valid'
			return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		form = UploadEcanForm()
	response_data = {}
	response_data['result'] = 'get'
	return HttpResponse(json.dumps(response_data), content_type="application/json")


def view_item(request):
	print request.GET.get('id')
	item = Item.objects.get(pk=1)
	response_data = {}
	response_data['image_url'] = item.image_color.url
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def view_ip(request):
	ecan = get_object_or_404(Ecan, pk=request.GET['pk'])
	response_data = {}
	response_data['ip'] = ecan.ip
	return HttpResponse(json.dumps(response_data), content_type="application/json")
