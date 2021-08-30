from measurements.logic.logic_measurements import get_a_measurement
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementsList'),
    path('<int:id>', views.get_measurement, name='specificmeasurement'),
    path('del/<int:id>', views.del_measurement, name='delmeasurement'),
    path('update/<int:id>/<val>', views.update_measurement, name='updatemeasurement')
]