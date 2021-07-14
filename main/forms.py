from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Employee,Department

class RegistrationForm (UserCreationForm):
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={
                                    'class':'form-control','placeholder':'First Name'
                                    }))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={
                                    'class':'form-control','placeholder':'Last Name'
                                    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
                                    'class':'form-control', 'placeholder':'Username'
                                    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                    'class':'form-control','placeholder':'Email Address'
                                    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'class':'form-control', 'placeholder':'Password'
                                    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'class':'form-control', 'placeholder':'Confirm Password'
                                    }))
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name','username','email','password1', 'password2')

class LoginForm(AuthenticationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={
                                    'autofocus':True, 'placeholder':'Username', 'class':'form-control'
                                    }))
   password = forms.CharField(widget=forms.PasswordInput(attrs={
                                    'class':'form-control', 'placeholder':'Password'
                                    }))

class EmployeeForm (forms.ModelForm):
    dp = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    address = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    classification = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Classification'}))
    gender = forms.ChoiceField(choices=Employee.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'mobile','email','salary', 'address','gender','department', 'classification','bank','acc_no','dp')
        widgets={
            'salary':forms.TextInput(attrs={'class':'form-control'}),
            'bank':forms.TextInput(attrs={'class':'form-control'}),
            'acc_no':forms.TextInput(attrs={'class':'form-control'})
        }

class DepartmentForm(forms.ModelForm):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief Department History'}))
    
    class Meta:
        model = Department
        fields = '__all__'