from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from boldpredict.models import *

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length = 20,
                               label = 'Username',
                               required = True,
                               widget = forms.TextInput(attrs={'id' : 'id_username','class' : 'form-control'}),
                               error_messages = {'required':'username cannot be none'},
                               )
    password = forms.CharField(max_length = 20,
                               label = "Password",
                               required = True,
                               widget = forms.PasswordInput(attrs= {'id' : 'id_password','class' : 'form-control'}),
                               error_messages = {'required':'password cannot be none'},
                               )
    confirm_pwd = forms.CharField(max_length = 20,
                                  label = 'Confirm',
                                  required = True,
                                  widget = forms.PasswordInput(attrs= {'id':'id_confirm_password','class' : 'form-control'}),
                                  error_messages = {'required':'password cannot be none'},
                                  )
    email = forms.CharField(max_length = 30,
                            label = 'E-mail',
                            required = False,
                            widget = forms.EmailInput(attrs = {'id':'id_email','class' : 'form-control'}),
                            )
    first_name = forms.CharField(max_length = 20,
                                 label = 'First Name',
                                 required = True,
                                 widget = forms.TextInput(attrs = {'id' : 'id_first_name','class' : 'form-control'}),
                                 error_messages = {'required':'first name cannot be none'},
                                 )
    last_name = forms.CharField(max_length = 20,
                                label = 'Last Name',
                                required = True,
                                widget = forms.TextInput(attrs = {'id' : 'id_last_name','class' : 'form-control'}),
                                error_messages = {'required':'last name cannot be none'},
                                )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()

        password = cleaned_data.get('password')
        confirm_pwd = cleaned_data.get('confirm_pwd')
        if password and confirm_pwd and password != confirm_pwd:
            raise forms.ValidationError("Password and confirm password don't match.")
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already exist.")
        if User.objects.filter(email__exact=email):
            raise forms.ValidationError("Email is already registered.")
            
        return cleaned_data