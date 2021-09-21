from django import forms
from django.forms import TextInput, EmailInput, ClearableFileInput 
from rexeonapp.models import Get_in_touch
from rexeonapp.models import Apply

class Get_in_touchForm(forms.ModelForm):
    class Meta:
        model = Get_in_touch
        fields = '__all__'
        widgets = {
            'Name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 90%;',
                'placeholder': 'Name'
                }),
            'Email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 90%;',
                'placeholder': 'Email'
                }),
            'Contact_no': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 90%;',
                 'placeholder': 'Contact No'
                }),
            'Queries': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 90%;',
                'placeholder': 'Write your query'
                })
        }

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__' 
        widgets = {
            'First_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 90%;',
                'placeholder': 'Enter your First Name'
                }),
                'Last_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 90%;',
                'placeholder': 'Enter Your Last Name'
                }),
            'Email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 90%;',
                'placeholder': 'Enter Your Email'
                }),
            'Contact_no': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 90%;',
                 'placeholder': 'Enter Your Contact No'
                }),
            'Resume': ClearableFileInput(attrs={ 
                'class': "form-control", 
                'style': 'max-width: 90%;',
                'placeholder': 'Upload Your Resume'
                })
        }
