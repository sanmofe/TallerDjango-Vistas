from ..models import Measurement
from django.db.models import F

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_a_measurement( num ):
    devuelveme = Measurement.objects.get(pk=num)
    return devuelveme

def delete_measurement( num ):
    Measurement.objects.filter(pk=num).delete()

def update_measurement(id,val):
    Measurement.objects.filter(pk=id).update(unit=val)
    