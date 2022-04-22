from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdminTable

class AdminForm(UserCreationForm):
    class Meta:
        model=AdminTable
        fields=('first_Name','last_Name','email','password1','password2')
        widgets={
            'password1':forms.CharField(),
            'password2':forms.CharField(),
        }
