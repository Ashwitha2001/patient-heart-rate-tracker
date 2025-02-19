from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),  
    path('login/', views.login_user, name='login_user'), 
    path('patients/<int:user_id>/', views.patient_list, name='patient_list'),  
    path('patients/create/', views.patient_create, name='patient_create'), 
    path('patients/<int:patient_id>/heartrate/', views.heart_rate_list, name='heart_rate_list'),  
    path('patients/<int:patient_id>/heartrate/create/', views.heart_rate_create, name='heart_rate_create'),  
]
