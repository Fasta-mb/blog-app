from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    path('password_change', views.PasswordChange.as_view(), name='password-change'),
    path('password_change/done', auth_view.PasswordChangeDoneView.as_view(template_name='authentications/password_change_done.html'), name='password-change-done'),
]