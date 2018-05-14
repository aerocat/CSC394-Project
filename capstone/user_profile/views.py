from django.shortcuts import render
from django.contrib.auth.models import User

# Allows users to retrieve their full profile
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
    print("got here")
    # return render(request, 'user_profile/profile.html', {'user': user})
    return render(request, 'user_profile/profile.html')
