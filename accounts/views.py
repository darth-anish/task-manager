from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from .forms import LoginForm

def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('tasks:home')

    return render(request, 'accounts/login.html', {'title':'Login','form':form})

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')