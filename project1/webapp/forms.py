from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Record
    


# - Register/Create a user

class createuserform(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class loginform(AuthenticationForm):

   username = forms.CharField(widget=TextInput())
   password = forms.CharField(widget=PasswordInput())
    
#create record
class Addrecordform(forms.ModelForm):
    
    class Meta:
        model =Record
        fields = ("first_name","last_name","email","phone","adress","city","provience","country")

class updaterecordform(forms.ModelForm):
    
    class Meta:
        model =Record
        fields = ("first_name","last_name","email","phone","adress","city","provience","country")

