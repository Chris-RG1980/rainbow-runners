from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


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

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
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
