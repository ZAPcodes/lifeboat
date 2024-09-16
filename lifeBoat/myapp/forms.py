# from django import forms
# from django.contrib.auth.models import User
# from .models import Profile, Doctor, Nurse
# from django.core.exceptions import ValidationError

# class UserForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }

#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if len(password) < 8:
#             raise ValidationError('Password must be at least 8 characters long.')
#         return password

#     def clean_confirm_password(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise ValidationError('Passwords do not match.')
#         return confirm_password

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['profession']

#     def clean_profession(self):
#         profession = self.cleaned_data.get('profession')
#         if profession not in ['Doctor', 'Nurse']:
#             raise ValidationError('Invalid profession selected.')
#         return profession

# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         exclude = ['user']

#     def clean_contact_number(self):
#         contact_number = self.cleaned_data.get('contact_number')
#         if not contact_number.isdigit() or len(contact_number) != 10:
#             raise ValidationError('Contact number must be 10 digits.')
#         return contact_number

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if "doctor" not in email.lower():
#             raise ValidationError('Email must contain "doctor".')
#         return email

# class NurseForm(forms.ModelForm):
#     class Meta:
#         model = Nurse
#         exclude = ['user']

#     def clean_contact_number(self):
#         contact_number = self.cleaned_data.get('contact_number')
#         if not contact_number.isdigit() or len(contact_number) != 10:
#             raise ValidationError('Contact number must be 10 digits.')
#         return contact_number

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if "nurse" not in email.lower():
#             raise ValidationError('Email must contain "nurse".')
#         return email
