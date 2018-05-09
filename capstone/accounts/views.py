from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Allows users to create a new account
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log user in
            return redirect('LandingPage:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Allows users to login
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('LandingPage:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
