from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_a_measurement( num ):
    devuelveme = Measurement.objects.get(pk=num)
    return devuelveme

def delete_measurement( num ):
    Measurement.objects.filter(pk=num).delete()