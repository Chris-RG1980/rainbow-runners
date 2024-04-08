from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm, DeactivateUserForm


# Create your views here.


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


""" Credit getup8 https://stackoverflow.com/questions/
38047408/how-to-allow-user-to-delete-account-in-django-allauth """


@login_required
def deactivate_account(request):
    """
    Deactivates the currently signed-in user by setting is_active to False.
    """

    if request.method == 'POST':
        deactivate_form = DeactivateUserForm(request.POST)
        if deactivate_form.is_valid():
            request.user.is_active = False
            request.user.save()
            logout(request)
            messages.success(request, 'Account successfully deactivated')
            return redirect(reverse('home'))

    deactivate_form = DeactivateUserForm
    template = 'profiles/profile.html'
    context = {
        'deactivate_form': deactivate_form,
    }
    return render(request, template, context)
