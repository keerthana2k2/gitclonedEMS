from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    head = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='headed_departments')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    job_title = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    employment_type = models.CharField(max_length=20)
    ssn = models.CharField(max_length=20)
    emergency_contact_name = models.CharField(max_length=50)
    emergency_contact_relationship = models.CharField(max_length=20)
    emergency_contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payrolls')
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2)
    bank_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)
    pay_frequency = models.CharField(max_length=20)
    pay_date = models.DateField()

    def __str__(self):
        return f'Payroll for {self.employee}'

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    clock_in = models.TimeField()
    clock_out = models.TimeField()
    work_hours = models.DecimalField(max_digits=5, decimal_places=2)
    overtime = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'Attendance for {self.employee} on {self.date}'

class LeaveRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_records')
    leave_type = models.CharField(max_length=20)
    leave_balance = models.IntegerField()
    leave_start_date = models.DateField()
    leave_end_date = models.DateField()
    approval_status = models.CharField(max_length=20)

    def __str__(self):
        return f'Leave Record for {self.employee}'

