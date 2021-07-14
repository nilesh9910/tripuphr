from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.conf import settings
from main.models import Employee, Department
from main.forms import DepartmentForm, EmployeeForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class Index(LoginRequiredMixin,ListView):
    template_name = 'dashboard/index.html'
    login_url = 'main:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['all_dept'] = Department.objects.all()
        context['dept_total'] = Department.objects.all().count()
        context['workers'] = Employee.objects.order_by('-id')
        return context
class Department_New (LoginRequiredMixin,CreateView):
    model = Department
    template_name = 'dashboard/create_department.html'
    form_class = DepartmentForm
    login_url = 'main:login'

class Department_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'dashboard/view_department.html'
    login_url = 'main:login'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context

class Department_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'dashboard/update_department.html'
    form_class = DepartmentForm
    login_url = 'main:login'
    success_url = reverse_lazy('dashboard:index')

class Employee_New(LoginRequiredMixin,CreateView):
    model = Employee  
    form_class = EmployeeForm  
    template_name = 'dashboard/create_employee.html'
    login_url = 'main:login'
    redirect_field_name = 'redirect:'
  
class Employee_View(LoginRequiredMixin,DetailView):
    queryset = Employee.objects.select_related('department')
    template_name = 'dashboard/view_employee.html'
    context_object_name = 'employee'
    login_url = 'main:login'