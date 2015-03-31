from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from ecan.forms import UploadItemForm, UploadEcanForm, UploadBack_GroundForm, UploadSampleForm
from ecan.forms import UploadLogoForm, UploadShapeForm, UploadMaterialForm, UploadCommon_NameForm
from ecan.models import Item, Ecan, Back_Ground, Sample, Shape, Material, Logo, Common_Name
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import RequestContext
import os
from django.conf import settings
import subprocess


# Create your views here.
def home(request):
    return render(request, 'ecan/home.html')


def index(request):
    return render(request, 'ecan/index.html')


def show_sample(request):
    pks = [e.pk for e in Sample.objects.all()]
    sample = get_object_or_404(Sample, pk=max(pks))
    print sample.pk
    return render(request,
                  'ecan/sample.html',
                  {'sample': sample},
                  context_instance=RequestContext(request))


@csrf_exempt
def upload_item(request):
    if request.method == 'POST':
        form = UploadItemForm(request.POST, request.FILES)

        # print form
        if form.is_valid():
            print 'valid'
            a = form.save()

            # do the processing here
            response_data = {}
            response_data['result'] = 'valid'
            # response_data['id'] = str(a.pk)
            response_data['w'] = str(a.weight)
            response_data['sh'] = str(a.shape.value)
            response_data['mat'] = str(a.material.value)
            response_data['cn'] = str(a.common_name.value)
            response_data['bg'] = str(a.bg.pk)
            response_data['lg'] = str(a.logo.value)
            response_data['tr'] = str(a.transparency)

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
        else:
            print form
            response_data = {}
            response_data['result'] = 'not valid'
            response_data['id'] = ''
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
    else:
        print 'get'
        form = UploadItemForm()
    response_data = {}
    response_data['result'] = 'get'
    response_data['id'] = ''
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


@csrf_exempt
def upload_bg(request):
    if request.method == 'POST':
        form = UploadBack_GroundForm(request.POST, request.FILES)

        # print form
        if form.is_valid():
            print 'valid'
            a = form.save()

            # do the processing here
            response_data = {}
            response_data['result'] = 'valid'
            response_data['id'] = str(a.pk)
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
        else:
            print form
            response_data = {}
            response_data['result'] = 'not valid'
            response_data['id'] = ''
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
    else:
        print 'get'
        form = UploadItemForm()
    response_data = {}
    response_data['result'] = 'get'
    response_data['id'] = ''
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


@csrf_exempt
def upload_ecan(request):
    if request.method == 'POST':
        form = UploadEcanForm(request.POST, request.FILES)
        if form.is_valid():
            instance = get_object_or_404(Ecan, pk=request.POST['pk'])
            form = UploadEcanForm(request.POST or None, instance=instance)
            form.save()

            # do the processing here
            response_data = {}
            response_data['result'] = 'is valid'
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
    else:
        form = UploadEcanForm()
    response_data = {}
    response_data['result'] = 'get'
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


@csrf_exempt
def upload_sample(request):
    if request.method == 'POST':
        form = UploadSampleForm(request.POST, request.FILES)
        # print form
        if form.is_valid():
            print 'valid'
            a = form.save()

            # do the processing here
            response_data = {}
            response_data['result'] = 'valid'
            response_data['id'] = str(a.pk)
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
        else:
            print form
            response_data = {}
            response_data['result'] = 'not valid'
            response_data['id'] = ''
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
    else:
        print 'get'
        form = UploadSampleForm()
    response_data = {}
    response_data['result'] = 'get'
    response_data['id'] = ''
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


def view_item(request):
    print request.GET.get('id')
    item = Item.objects.get(pk=1)
    response_data = {}
    response_data['image_url'] = item.image_color.url
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


def view_ip(request):
    ecan = get_object_or_404(Ecan, pk=request.GET['pk'])
    response_data = {}
    response_data['ip'] = ecan.ip
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


def delete_object(request):
    try:
        oto_del = Item.objects.filter(identifier=request.GET['identifier'])
        print len(oto_del)
        mr = settings.MEDIA_ROOT
        oto_bg = oto_del[0].bg
        os.system('rm %s' % os.path.join(mr,
                  oto_bg.im.path.encode('ascii', 'replace')))
        oto_bg.delete()
        print "bg deleted"
        print len(oto_del)
        for e in oto_del:
            path = os.path.join(mr, e.im.path.encode('ascii', 'replace'))
            print path
            os.remove(path)
        print "ims deleted"
        [e.delete() for e in oto_del]
        print "objects deleted"
        response_data = {'result': 'valid'}
    except Exception as e:
        response_data = {'result':  str(e)}
    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


@csrf_exempt
def insert_attribute(request):
    attributes = {
        'material': {
            'form': UploadMaterialForm,
            'model': Material
        },
        'logo': {
            'form': UploadLogoForm,
            'model': Logo
        },
        'shape': {
            'form': UploadShapeForm,
            'model': Shape
        },
        'common_name': {
            'form': UploadCommon_NameForm,
            'model': Common_Name
        }
    }

    if request.method == 'POST':
        att_key = request.POST['att_key']
        post_dict = attributes[att_key]
        form = post_dict['form'](request.POST, request.FILES)
        model = post_dict['model']

        if form.is_valid() and request.POST['action'] == 'save':
            form.save()

        objects = model.objects.all()
        response_data = {}
        keys = [str(e.value) for e in objects]
        values = [str(e.pk) for e in objects]
        d = str(dict(zip(keys, values)))
        response_data['dictionary'] = d
        response_data['result'] = 'valid'

        if form.is_valid() and request.POST['action'] == 'save':
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")

        elif request.POST['action'] == 'view':
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
        else:
            response_data = {'result': 'not valid', 'id': ''}
            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json")
    else:

        response_data = {}
        response_data['result'] = 'nothing to get'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json")
