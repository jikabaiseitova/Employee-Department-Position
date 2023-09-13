from django.contrib.auth import admin
from django.urls import path, include
from employee.views import DepartmentEmployeesAPIView

urlpatterns = [
    path('api/', include('employee.urls')),
path('api/department/<int:department_id>/employees/', DepartmentEmployeesAPIView.as_view(), name='department-employees-api'),
]