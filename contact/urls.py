from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact_us'),
    path('view_questions/', views.view_questions, name='view_questions'),
]
