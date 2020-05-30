from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


#
#   Form form user Sign in
#
class UserSignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


#
#   Form form user Sign up (registration)
#
class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
