from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile_user', views.profileUser, name='profile-user'),
    path('profile_edit', views.editProfileUser, name='profile-edit'),
    path('post_create', views.postCreate, name='create-post'),
    path('post_edit/<int:pk>', views.postedit, name='post-edit'),
    path('post_delete/<int:pk>', views.postDelete, name= 'post-delete'),
    path('notification', views.notification, name='notification'),
    path('post_display/<int:pk>', views.postDisplay, name="post-display")
]