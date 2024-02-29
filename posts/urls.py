from django.urls import path

from . import views


urlpatterns = [
    path('', views.all_posts, name='posts'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
]
