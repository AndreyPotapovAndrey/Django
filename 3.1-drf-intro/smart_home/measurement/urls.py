from django.contrib import admin
from django.urls import path, include
from measurement.views import SensorsView, MeasurementView, SensorView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls')),
    path("sensors/", SensorsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measures/<pk>/', MeasurementView.as_view())
]
