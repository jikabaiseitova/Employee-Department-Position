from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . models import Department, Position, Employee
from .serializers import DepartmentSerializer, PositionSerializer, EmployeeSerializer


# @api_view(http_method_names=['GET', ])
# def department_list_api_view(request):
#     if request.method == 'GET':
#         departments = Department.objects.all()
#         serializer = DepartmentSerializer(departments, many=True)
#         return Response(serializer.data)


# @action(methods=['GET'], detail=False, url_path='employees')
# def department_employees(self, request, pk=None):
#     departments_queryset = Department.objects.all()
#     departments = []
#     for department in departments_queryset:
#         departments.append(department.code)


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionViewSet(ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



