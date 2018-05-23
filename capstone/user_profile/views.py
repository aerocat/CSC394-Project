from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

# Allows users to retrieve their full profile
@login_required(login_url="/accounts/login/")
def get_profile(request):
    #  TO DO: update information function (uses POST)
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect('user_profile:profile')
    # else:
        # form = UserCreationForm()
    # user = User.objects.get(username=username)
    # return render(request, 'user_profile/profile.html', {'user': user})
    return render(request, 'user_profile/profile.html')

@login_required(login_url="/accounts/login/")
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = UserChangeForm(instance=request.user)
        return render(request, 'user_profile/edit_profile.html', {'form': form})
