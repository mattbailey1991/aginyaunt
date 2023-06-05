from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

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
        pass
    else:
        return render(request, 'authentication/register.html', {})
