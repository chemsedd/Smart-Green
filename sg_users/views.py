from django.shortcuts import render, redirect
from .form import UserSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def profile(request):
    return render(request, 'sg_users/profile.html')


#
#   Sign up view
#
def signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(
                request, f'Your account has been created. You can now log in!')
            return redirect('sg-signin')
    else:
        form = UserSignUpForm()
    return render(request, 'sg_users/signup.html', {'form': form})


#
#   Sign In view
#
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(
                request,
                username=credentials['username'],
                password=credentials['password'])
            if user != None:
                login(request, user)
                messages.success(request, f'Welcome back!')
                return redirect('sg-dashboard')
        else:
            print("It's not valid")
    else:
        form = AuthenticationForm()
    return render(request, 'sg_users/signin.html', {'form': form})


def signout(request):
    pass
