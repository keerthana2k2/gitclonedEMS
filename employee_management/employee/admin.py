from django.contrib import admin
from .models import Department, Employee, Payroll, Attendance, LeaveRecord

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Payroll)
admin.site.register(Attendance)
admin.site.register(LeaveRecord)
