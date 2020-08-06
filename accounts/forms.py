from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm (UserCreationForm):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={
        'class':'form-control mb-2'
    }))

    email=forms.CharField(max_length=255,required=False,widget=forms.EmailInput(attrs={
   'class':'form-control mb-2'
    }))
    password1=forms.CharField(label='password',required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control mb-2'
    }))
    password2=forms.CharField(label=' confirm password',required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control mb-2'
    }))
    class Meta:
     model=User
     fields =['username','email','password1','password2']


class loginForm (forms.Form):
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={
        'class':'form-control mb-2','name':'username'
    }))

  
    password=forms.CharField(label='password',required=True,widget=forms.PasswordInput(attrs={
        'class':'form-control mb-2','name':'password'
    }))
  
    class Meta:
     model=User
     fields =['username','password']
