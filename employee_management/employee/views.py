from django.shortcuts import render
from .models import Department, Payroll, Employee
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from .models import Employee, LeaveRecord, Attendance

def employee_home(request):
    departments = Department.objects.all()
    recent_payrolls = Payroll.objects.order_by('-pay_date')[:10]  # Display last 10 payroll entries
    return render(request, 'employee_home.html', {'departments': departments, 'recent_payrolls': recent_payrolls})

def employees_in_department(request, department_name):
    department = Department.objects.get(name=department_name)
    employees = department.employees.all()
    return render(request, 'employees_in_department.html', {'employees': employees, 'department': department})

def payroll_cost_per_department(request):
    departments = Department.objects.all()
    department_payrolls = {}
    for department in departments:
        total_payroll = Payroll.objects.filter(employee__department=department).aggregate(total=Sum('basic_salary'))['total']
        department_payrolls[department.name] = total_payroll if total_payroll is not None else 'N/A'
    return render(request, 'payroll_cost_per_department.html', {'department_payrolls': department_payrolls})

def salary_history(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    salary_history = employee.payrolls.all()
    return render(request, 'salary_history.html', {'employee': employee, 'salary_history': salary_history})

def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'all_employees.html', {'employees': employees})

def search_employee_by_id(request):
    query = request.GET.get('id')
    employees = Employee.objects.filter(id=query) if query else None
    return render(request, 'search_results.html', {'employees': employees, 'query': query})


def employee_leave_attendance(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    leave_records = LeaveRecord.objects.filter(employee=employee)
    attendance_records = Attendance.objects.filter(employee=employee)
    return render(request, 'employee_leave_attendance.html', {
        'employee': employee,
        'leave_records': leave_records,
        'attendance_records': attendance_records
    })

