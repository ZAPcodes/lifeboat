from django.shortcuts import render, redirect,get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Measurement, Patient
import plotly.graph_objects as go

import json

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user exists
        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid password.')
        else:
            messages.error(request, 'User not registered.')

    return render(request, 'login.html')

@csrf_exempt

def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)

    # Check if the request is an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX request
        latest_measurement = Measurement.objects.filter(patient=patient).order_by('-timestamp').first()
        if latest_measurement:
            data = {
                'heart_rate': latest_measurement.heart_rate,
                'spo2': latest_measurement.spo2,
                'timestamp': latest_measurement.timestamp.isoformat(),  # Convert timestamp to ISO format
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'No measurement found'}, status=404)
    
    # Handle regular request
    latest_measurement = Measurement.objects.filter(patient=patient).order_by('-timestamp').first()
    context = {
        'patient': patient,
        'latest_measurement': latest_measurement,
    }
    return render(request, 'patientDetails.html', context)






# Example data - replace with actual database query
patients = [
    {
        'patient_id': 1,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'ok',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
        
    },{
        'patient_id': 2,
        'name': 'John Doe',
        'heart_rate': 120,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'critical',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },{
        'patient_id': 3,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 50,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'critical',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },{
        'patient_id': 4,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'ok',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },{
        'patient_id': 5,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'ok',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },{
        'patient_id': 6,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'ok',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },{
        'patient_id': 7,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'ok',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },{
        'patient_id': 8,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'ok',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },{
        'patient_id': 9,
        'name': 'John Doe',
        'heart_rate': 75,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'ok',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
    },
]
patient = [
    {
        'name': 'John Doe',
        'heart_rate': 12,
        'spo2': 98,
        'bp': '120/80',
        'resp_rate': 16,
        'body_temp': 98.6,
        'condition':'critical',
        'ward_number': '5A',
        'bed_number': '12',
        'doctor': 'Dr. Smith',
        'illness': 'Pneumonia'
        
    }]
# @login_required
def patient_dashboard(request):
    return render(request, 'dashboard.html', {'patients': patients,'user':User})



# def patient_detail(request, patient_id):
#     patient = get_object_or_404(Patient, pk=patient_id)
#     measurements = Measurement.objects.filter(patient=patient).order_by('-timestamp')

#     # Process data for charts
#     heart_rate_data = {
#         'timestamps': [m.timestamp.strftime('%Y-%m-%d %H:%M:%S') for m in measurements],
#         'values': [m.heart_rate for m in measurements]
#     }
#     spo2_data = {
#         'timestamps': [m.timestamp.strftime('%Y-%m-%d %H:%M:%S') for m in measurements],
#         'values': [m.spo2 for m in measurements]
#     }
#     bp_data = {
#         'timestamps': [m.timestamp.strftime('%Y-%m-%d %H:%M:%S') for m in measurements],
#         'values': [m.blood_pressure_systolic for m in measurements]  # Customize for systolic/diastolic
#     }
#     resp_rate_data = {
#         'timestamps': [m.timestamp.strftime('%Y-%m-%d %H:%M:%S') for m in measurements],
#         'values': [m.respiratory_rate for m in measurements]
#     }
#     body_temp_data = {
#         'timestamps': [m.timestamp.strftime('%Y-%m-%d %H:%M:%S') for m in measurements],
#         'values': [m.body_temperature for m in measurements]
#     }

#     context = {
#         'patient': patients,
#         'heart_rate_data': heart_rate_data,
#         'spo2_data': spo2_data,
#         'bp_data': bp_data,
#         'resp_rate_data': resp_rate_data,
#         'body_temp_data': body_temp_data,
#     }
#     return render(request, 'patientDetails.html', context)

# def register(request):
#     profession = None

#     if request.method == 'POST':
#         user_form = UserForm(request.POST)
#         profile_form = ProfileForm(request.POST)
#         doctor_form = DoctorForm(request.POST)
#         nurse_form = NurseForm(request.POST)

#         if profile_form.is_valid():
#             profession = profile_form.cleaned_data.get('profession')

#         if user_form.is_valid() and profile_form.is_valid():
#             try:
#                 user = user_form.save()  # Save User and handle potential errors
#                 profile = profile_form.save(commit=True)  # Commit Profile save
#                 profile.user = user
#                 profile.save()

#                 if profession == 'Doctor' and doctor_form.is_valid():
#                     doctor = doctor_form.save(commit=False)
#                     doctor.user = user
#                     doctor.save()
#                     return redirect('success_page')
#                 elif profession == 'Nurse' and nurse_form.is_valid():
#                     nurse = nurse_form.save(commit=False)
#                     nurse.user = user
#                     nurse.save()
#                     return redirect('success_page')
#                 else:
#                     messages.error(request, 'There was an error with your registration.')
#             except Exception as e:
#                 messages.error(request, f'Registration failed: {e}')

#     else:
#         user_form = UserForm()
#         profile_form = ProfileForm()
#         doctor_form = DoctorForm()
#         nurse_form = NurseForm()

#     return render(request, 'register.html', {
#         'user_form': user_form,
#         'profile_form': profile_form,
#         'doctor_form': doctor_form,
#         'nurse_form': nurse_form,
#         'profession': profession,  # Pass the profession to the template
#     })




