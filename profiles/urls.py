from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.profile,
        name='profile'
    ),
    path(
        'deactivate_account',
        views.deactivate_account,
        name='deactivate_account'
    )
]
