from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    ward_number = models.IntegerField()  # Added for details
    bed_number = models.IntegerField()  # Added for details
    illness = models.CharField(max_length=255)  # Added for details

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.patient_id}"

class Measurement(models.Model):
     measurement_id = models.AutoField(primary_key=True)
     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
     heart_rate = models.IntegerField()
     blood_pressure_systolic = models.IntegerField()
     blood_pressure_diastolic = models.IntegerField()
     spo2 = models.FloatField()
     respiratory_rate = models.FloatField()
     body_temperature = models.FloatField()
     timestamp = models.DateTimeField()
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return f"Measurement {self.measurement_id} for {self.patient}"
class Device(models.Model):
     device_id = models.AutoField(primary_key=True)
     device_serial_number = models.CharField(max_length=100, unique=True)
     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
     device_type = models.CharField(max_length=50, choices=[
         ('wearable', 'Wearable'),
         ('implantable', 'Implantable')
     ])
     assigned_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.device_serial_number
# class HeartAttackPrediction(models.Model):
#     prediction_id = models.AutoField(primary_key=True)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
#     prediction_result = models.BooleanField()
#     prediction_confidence = models.FloatField()
#     predicted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Prediction {self.prediction_id} for {self.patient}"


class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Doctor: {self.first_name} {self.last_name}"
    
class Nurse(models.Model):
    nurse_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Nurse: {self.first_name} {self.last_name}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PROFESSION_CHOICES = (
        ('Doctor', 'Doctor'),
        ('Nurse', 'Nurse'),
    )
    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.profession}"

