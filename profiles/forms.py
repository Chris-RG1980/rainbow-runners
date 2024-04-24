from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from allauth.account.forms import SignupForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postal Code'
        }
        aria_labels = {
            'default_full_name': 'Enter your full name',
            'default_phone_number': 'Enter your phone number',
            'default_street_address1': 'Enter your street address 1',
            'default_street_address2': 'Enter your street address 2',
            'default_town_or_city': 'Enter your town or city',
            'default_county': 'Enter your county',
            'default_postcode': 'Enter your postal code'
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs[
                    'aria-label'] = aria_labels[field]
            self.fields[field].widget.attrs['class'] = 'border-black'
            self.fields[field].label = False


""" Credit https://stackoverflow.com/questions/
38047408/how-to-allow-user-to-delete-account-in-django-allauth """


class DeactivateUserForm(forms.ModelForm):
    """
    Simple form that provides a checkbox that signals deactivation.
    """
    class Meta:
        model = User
        fields = ['is_active']

        def __init__(self, *args, **kwargs):
            super(DeactivateUserForm, self).__init__(*args, **kwargs)

            msg = "To deactivate this account tick the box."

            self.fields['is_active'].help_text = msg


class UserSignupForm(SignupForm):
    """
    Stop help text on Django Allauth displaying on page load.
    """
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
