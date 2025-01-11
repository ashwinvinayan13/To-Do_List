from django.urls import path
from baseapp import views

urlpatterns = [

    path('demo/', views.demo, name='demo'),
    path('Login/', views.Log_in, name='Login'),
    path('Logu/', views.Logu, name='Logu'),
    path('Reg_User/', views.Reg_User, name='Reg_User'),
    path('Register/', views.Register, name='Register'),
    path('task/', views.task, name='task'),
    path('Save_task/', views.Save_task, name='Save_task'),
    path('Update_task/<int:t_id>/', views.Update_task, name='Update_task'),
    path('delete/<int:t_id>/', views.delete, name='delete'),
    path('Logout/', views.Logout, name='Logout'),

]