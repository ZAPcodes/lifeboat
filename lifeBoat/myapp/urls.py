from django.urls import path
from . import views 

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.patient_dashboard, name='dashboard'),
    # path('dashboard/patientDetails/', views.patient_details, name='patient_details'),
    path('dashboard/patient/<int:patient_id>/', views.patient_details, name='patient_details'),
    # path('patient/<int:patient_id>/measurements/', views.latest_measurements, name='latest_measurements'),
    # path('register/',views.register,name='register'),
]