from django.shortcuts import render

def login_user(request):
    return render(request, 'authentication/login.html', {})

def register_user(request):
    return render(request, 'authentication/register.html', {})
