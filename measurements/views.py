from django.shortcuts import render
from .logic import logic_measurements as l
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def get_measurements(request):
    measurements = l.get_all_measurements()
    measurements_list = serializers.serialize('json', measurements)
    return HttpResponse(measurements_list, content_type='application/json')

def get_measurement(request, id):
    temp = l.get_a_measurement(id)
    devuelveme = serializers.serialize('json', [temp,])
    return HttpResponse(devuelveme, content_type='application/json')

def del_measurement(request, id):
    l.delete_measurement(id)
    return HttpResponse('[]', content_type='application/json')

def update_measurement(request, id, val):
    l.update_measurement(id, val)
    return HttpResponse('[]', content_type='application/json')
