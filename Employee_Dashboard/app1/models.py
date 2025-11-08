from django.db import models

class Employees(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_age = models.IntegerField()
    Employee_email = models.EmailField(unique=True)
    Employee_salary = models.IntegerField()
    Employee_mobile = models.BigIntegerField()
    Employee_department = models.CharField(max_length=50)
    Employee_join_date = models.DateField()
    
