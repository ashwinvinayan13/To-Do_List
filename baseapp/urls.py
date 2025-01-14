from django.urls import path
from baseapp import views

urlpatterns = [

    path('demo/', views.demo, name='demo'),
    path('Login/', views.log_in, name='Login'),
    path('Logu/', views.logu, name='Logu'),
    path('Reg_User/', views.register_user, name='Reg_User'),
    path('Register/', views.register_user, name='Register'),
    path('task/', views.task, name='task'),
    path('Save_task/', views.save_task, name='Save_task'),
    path('Update_task/<int:t_id>/', views.update_task, name='Update_task'),
    path('delete/<int:t_id>/', views.delete, name='delete'),
    path('Logout/', views.logout_view, name='Logout'),

]