from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from app.models import Comment

from authentications.forms import LoginForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.username = new_form.username.lower()
            new_form.save()
            login(request, new_form)
            return redirect(reverse('profile'))
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'authentications/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        loginUserForm = LoginForm(request.POST)
        if loginUserForm.is_valid():
            data = loginUserForm.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
    else:
        loginUserForm = LoginForm()
        
    context = { 'loginUserForm': loginUserForm }
    return render(request, 'authentications/login.html', context)

class PasswordChange(LoginRequiredMixin,PasswordChangeView):
    fields = '__all__'
    context_object_name = all
    redirect_authenticated_user = True
    success_url = reverse_lazy('password-change-done')
    template_name = 'authentications/password_change.html'


@login_required(login_url="login")
def profile(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    
    
    if request.method == 'POST':
        prof = ProfileForm(data=request.POST, files=request.FILES)
        if prof.is_valid():
            obj = prof.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect(reverse('home'))
    else:
        prof = ProfileForm()
    context = {'prof': prof}
    return render(request, 'authentications/user_profile.html', context)
            