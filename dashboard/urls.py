from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add_dept', views.Department_New.as_view(), name='add_dept'),
    path('department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
    path('department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),
    path('employee/new/', views.Employee_New.as_view(), name='employee_new'),
    path('employee/<int:pk>/view/', views.Employee_View.as_view(), name='employee_view'),
    
]