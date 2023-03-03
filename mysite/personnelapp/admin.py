from django.contrib import admin
from .models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["emp_code","emp_fname", "emp_lname","emp_sal","emp_phone","emp_email", "emp_address"]


admin.site.register(Employee, EmployeeAdmin)