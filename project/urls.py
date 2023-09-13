from django.contrib.auth import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('employee.urls')),
]
