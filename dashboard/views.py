from django.shortcuts import render
from django.contrib.auth.models import User, auth
from userprofile.models import UserProfile
from django.http import HttpResponseRedirect
from django.urls import reverse

def dashboardFunction(request):
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            user_id = request.user.id
            return render(request, 'dashboard.html', {'user_profile': user_profile})
        except UserProfile.DoesNotExist:
            # Handle the case where UserProfile doesn't exist for the user
            # Redirect to a page where user can set up their profile
            return HttpResponseRedirect(reverse('editprofile')) 
    else:
        # Redirect unauthenticated users to the login page
        return HttpResponseRedirect(reverse('login'))