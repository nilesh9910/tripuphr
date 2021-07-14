from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='reg'),
    
    path('logout/', views.Logout_View.as_view(), name='logout1'),
    path('login/', views.Login_View.as_view(), name='login'),
]