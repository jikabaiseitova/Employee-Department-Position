from employee.models import *

### a ###
employees = Employee.objects.all().values('fullname', 'salary').order_by('-salary')
employees
str(employees.query)

### b ###
e1 = Employee.objects.create(
    fullname='Madina Son',
    birth_date='1980-03-03',
    salary=35000,
    receipt_date='2017-09-12',
    department_id=2,
    position_id=4)
e1.save()
e1
e1.department.name

e2 = Employee.objects.create(
    fullname='Navuhodonosor',
    birth_date='1980-01-01',
    salary=50000,
    receipt_date='2010-01-01',
    department_id=2,
    position_id=3)
e2.save()
e2
e2.department.name

e3 = Employee.objects.create(
    fullname='Yacob',
    birth_date='1990-01-01',
    salary=50000,
    receipt_date='2010-01-01',
    department_id=2,
    position_id=3)
e3.save()
e3
e3.department.name

### c ###
employees = Employee.objects.all().values('fullname', 'birth_date', 'receipt_date').order_by('-birth_date', 'receipt_date')
employees
str(employees.query)

### d ###
from django.db.models import Q, F, Sum, Case, FloatField

employees = Employee.objects.filter(Q(salary__lt=50000) & Q(salary__gt=20000))
employees
str(employees.query)

### e ###
employees = Employee.objects.filter(
    department__name__icontains='accounting_department').order_by('fullname')
employees
str(employees.query)

### f ###
from django.db.models import Count

departments = Department.objects.annotate(
    employee_count=Count('employee')).order_by('employee_count')
departments

employees = Employee.objects.values('department_id').annotate(
    department_count=Count('department'),
)
employees


### g ###
from django.db.models import Avg

employees = Employee.objects.filter(department_id=1).aggregate(Avg('salary'))
employees = Employee.objects.filter(department_id=2).aggregate(Avg('salary'))
employees = Employee.objects.filter(department_id=3).aggregate(Avg('salary'))
employees = Employee.objects.filter(department_id=4).aggregate(Avg('salary'))
employees


employees = Employee.objects.values('department_id').annotate(
    salary_count=Avg('salary'),
)
employees

### посмотреть ###
from django.db.models import Q, F, Sum, Case, When, FloatField

employees = Employee.objects.values('fullname', 'salary', 'receipt_date').annotate(
    bonus=Case(
        When(receipt_date__gte='2018-01-01', then=F('salary') * 0.08),
        When(department__name='IT_department', then=F('salary') * 0.10),
        default=F('salary') * 0.05,
        output_field=FloatField()
    )
)

today = datetime.date.today()
employee = Employee.objects.get(fullname='Навуходоно́сор')

receipt_date = employee.receipt_date
new_date = receipt_date.replace(year=today.year)

vacation_date = new_date + datetime.timedelta(days=11 * 30.4)
result_in_days = vacation_date - today
print(f"До отпуска осталось {result_in_days.days} дней")




