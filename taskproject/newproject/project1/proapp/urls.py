from . import views
from django.urls import path, include

app_name='proapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.login, name='login'),
    path('form/', views.form, name='form'),
    path('thanks/',views.thanks,name='thanks'),
    path('register/',views.register,name='register'),
    ]