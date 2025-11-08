from django.contrib import admin
from app1.models import Employees
# Register your models here.

class employees_Admin(admin.ModelAdmin):
    list_display=['Employee_name','Employee_age','Employee_email','Employee_salary','Employee_mobile','Employee_department','Employee_join_date']
    
admin.site.register(Employees,employees_Admin)
    
    
    
    
    
    
    
    
    
    
    #     Employee_name = models.CharField(max_length=50)
    # Employee_age = models.IntegerField()
    # Employee_email = models.EmailField(unique=True)
    # Employee_salary = models.IntegerField()
    # Employee_mobile = models.BigIntegerField()
    # Employee_department = models.CharField(max_length=50)
    # Employee_join_date = models.DateField()
    