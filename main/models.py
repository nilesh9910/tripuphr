from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    dp = models.ImageField()

class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField(max_length=1000,null=True,blank=True, default='No Description')
    

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("dashboard:dept_detail", kwargs={"pk": self.pk})

class Employee(models.Model):
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    dp = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    address = models.TextField(max_length=100, default='')
    gender = models.CharField(choices=GENDER, max_length=10)
    classification = models.CharField(max_length=50, null=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    acc_no = models.CharField(max_length=10, default='0123456789')
    bank = models.CharField(max_length=25, default='Band')
    salary = models.CharField(max_length=16,default='00,000.00')      
    def __str__(self):
        return self.first_name
        
    def get_absolute_url(self):
        return reverse("dashboard:employee_view", kwargs={"pk": self.pk})