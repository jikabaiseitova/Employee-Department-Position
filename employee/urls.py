from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('department', views.DepartmentViewSet)
router.register('position', views.PositionViewSet)
router.register('employee', views.EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('department/<int:pk>/employees/', views.department_employees),
]
