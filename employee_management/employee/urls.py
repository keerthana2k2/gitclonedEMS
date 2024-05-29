from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_home, name='employee_home'),
    path('department/<path:department_name>/', views.employees_in_department, name='employees_in_department'),
    path('payroll/', views.payroll_cost_per_department, name='payroll_cost_per_department'),
    path('salary_history/<int:employee_id>/', views.salary_history, name='salary_history'),
    path('all_employees/', views.all_employees, name='all_employees'),
    path('search_employee_by_id/', views.search_employee_by_id, name='search_employee_by_id'),
    # path('employee_leave_attendance/<int:employee_id>/', views.employee_leave_attendance, name='employee_leave_attendance'),
    path('employee_leave_attendance/<int:employee_id>/', views.employee_leave_attendance, name='employee_leave_attendance'),
]


