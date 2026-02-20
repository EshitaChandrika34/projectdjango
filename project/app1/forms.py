from django import forms
#class SignupForm(forms.Form):
    #username=forms.CharField(label="Enter the username",
                            # min_length=8,
                            # error_messages={"required":"please enter your name",
                                            # "min_length":"enter atleast 8 characters"})
   # password=forms.CharField(label="enter your password")
   
from django.forms import ModelForm   
from .models import hello

from .models import LoginUser

class LoginForm(forms.ModelForm):
    password = forms.IntegerField(widget=forms.PasswordInput)

    class Meta:
        model = LoginUser
        fields = ['username', 'password']

class SignupForm(ModelForm):
    class Meta:
        model=hello
        #exclude=['name']
        fields=['name','age','branch']
       

