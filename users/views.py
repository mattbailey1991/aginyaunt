from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            message = "Username or password is not correct"
            return render(request, 'authentication/login.html', {'message': message})
    else:
        return render(request, 'authentication/login.html', {})

def logout_user(request):
    if request.method == "GET":
        logout(request)
        message = "Logged out"
        return render(request, 'authentication/login.html', {'message': message})

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            message = "Please correct the errors below"
            return render(request, 'authentication/register.html', {'form': form, 'message': message})
    else:
        form = UserCreationForm
        return render(request, 'authentication/register.html', {'form': form})
