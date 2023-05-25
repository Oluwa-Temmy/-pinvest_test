from django import forms
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(min_length=5, max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date','max':datetime.now().date()
                                      }))

