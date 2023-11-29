from form import form
from django import forms
from destiny.models import *
from django.forms import ModelForm
from  .models import Booking, Plan

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        labels={
            'firstName': 'Enter your First Name',
            'lastName': 'Enter your Last Name',
            'mobileNo': 'Enter your Phone Number',
            'email': 'Enter Your Email Address',
            'adult': 'Enter The Total Number of intended Adults to Travel',
            'kid ': 'Enter Total Number of Kids You will Travel with Them',
            'specialRequest': 'Accomodations/Meals',
            'checkIn': 'Check in',
            'checkOut': 'Check Out'
        }
        widgets = {
            'firstName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kenneth'}),
            'lastName':forms.TextInput(attrs={'class':'form-control','placeholder':'Cheruiyot'}),
            'mobileNo':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'+254746589039'}),
            'email':forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'cheruiyotk134@gmail.com'}),
            'adult' :forms.NumberInput(attrs={'class':'form-control' ,'placeholder':'2'}),
            'kid ' :forms.NumberInput(attrs={'class':'form-control' ,'placeholder':'2'}),
            'specialRequest':forms.TextInput(attrs={'class':'form-control' ,'placeholder':'accommodations'}),
            'checkIn':forms.DateInput(attrs={'class':'form-control' ,'placeholder':'12/04/2021 12:00p.m'}),
            'checkOut': forms.DateInput(attrs={'class': 'form-control' ,'placeholder':'12/04/2023 1:40p.m'})
        }

class PlanForm(forms.ModelForm):
    class Meta:
          model = Plan
          fields = '__all__'
class AddDestForm(forms.ModelForm):
    class Meta:
        model=popular
        fields='__all__'

class EditDestForm(forms.ModelForm):
    class Meta:
        model = popular
        fields = '__all__'

        class PlanForm(forms.ModelForm):
            class Meta:
                model = Plan
                fields = '__all__'
                labels = {
                    'firstName': 'Enter your First Name',
                    'lastName': 'Enter your Last Name',
                    'mobileNo': 'Enter your Phone Number',
                    'email': 'Enter Your Email Address',
                    'adult': 'Enter The Total Number of intended Adults to Travel',
                    'kid ': 'Enter Total Number of Kids You will Travel with Them',
                    'specialRequest': 'Accomodations/Meals',
                    'checkIn': 'Check in',
                    'checkOut': 'Check Out'
                }
                widgets = {
                    'firstName': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Kenneth'}),
                    'lastName': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Cheruiyot'}),
                    'mobileNo': forms.TextInput(attrs={'class': 'form-control','placeholder': '+254746589039'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'cheruiyotk134@gmail.com'}),
                    'adult': forms.NumberInput(attrs={'class': 'form-control','placeholder': '2'}),
                    'kid ': forms.NumberInput(attrs={'class': 'form-control','placeholder': '2'}),
                    'specialRequest': forms.TextInput(attrs={'class': 'form-control','placeholder': 'accommodations'}),
                    'checkIn': forms.DateInput(attrs={'class': 'form-control','placeholder': '12/04/2021 12:00p.m'}),
                    'checkOut': forms.DateInput(attrs={'class': 'form-control','placeholder': '12/04/2023 1:40p.m'})
                }
