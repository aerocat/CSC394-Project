from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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
