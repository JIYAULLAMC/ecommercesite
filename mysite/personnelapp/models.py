from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Employee model

class Employee(models.Model):
    user = models.ForeignKey(User)
    emp_code = models.IntegerField( unique=True, null=False)
    emp_fname = models.CharField(null=False)
    emp_lname = models.CharField()
    emp_sal = models.FloatField()
    emp_phone = models.PositiveBigIntegerField()
    emp_email = models.EmailField(max_length=30)
    emp_address = models.CharField(max_length=250)


    def __str__(self):
        return f'{self.emp_code}_{self.emp_fname}'

