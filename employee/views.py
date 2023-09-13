from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from . models import Department, Position, Employee
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer


class DepartmentEmployeesAPIView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer


    def get_queryset(self):
        department_id = self.kwargs.get('department_id')
        return Employee.objects.filter(department_id=department_id)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



