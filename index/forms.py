from django import forms
from django.forms.widgets import PasswordInput, EmailInput
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username            = forms.CharField()
    password            = forms.CharField(widget=PasswordInput)


class UserRegistrationForm(forms.Form):
    username            = forms.CharField()
    email               = forms.EmailField(widget=EmailInput)
    password            = forms.CharField(widget=PasswordInput)
    password2           = forms.CharField(label='Confirm password', widget=PasswordInput)

    def clean_username(self):
        username        = self.cleaned_data.get('username')
        qs              = User.objects.filter(username=username)
        
        print("checking if user exists")
        if qs.exists():
            raise forms.ValidationError("Username is taken.")

        print("returning username")
        return username

    def clean_email(self):
        email           = self.cleaned_data.get('email')
        qs              = User.objects.filter(email=email)
        
        print("checking if user exists")
        if qs.exists():
            raise forms.ValidationError("Email already exists.")

        print("returning email")
        return email


    def clean(self):
        cleaned_data    = super(UserRegistrationForm, self).clean()
        print("clean is called")
        password        = cleaned_data.get("password")
        password2       = cleaned_data.get("password2")

        if password != password2:
            print("passwords did not match")
            raise forms.ValidationError("Passwords must match.")
        
        print("returning cleaned_data")
        return cleaned_data