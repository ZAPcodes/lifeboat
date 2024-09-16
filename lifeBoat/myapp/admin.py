from django.contrib import admin
from .models import *

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email')  # Display these fields in list view

class NurseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'email')
admin.site.register(Profile)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Measurement)
admin.site.register(Device)