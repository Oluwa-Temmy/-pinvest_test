from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from datetime import datetime

#NOTE: this is not connected to a database, migrations will not work
class CreateSignupForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date','max':datetime.now().date()
                                      }))
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        
        
        