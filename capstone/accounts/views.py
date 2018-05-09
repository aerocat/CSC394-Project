from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Allows users to create a new account
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('LandingPage:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Allows users to login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('LandingPage:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Allows users to logout
def logout_view(request):
    # Best practice: using POST requests to log users out
    if request.method == 'POST':
        logout(request)
        return redirect('LandingPage:index')
