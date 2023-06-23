from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                return render(request, 'registration/login.html', {})
        else:
            return render(request, 'registration/login.html', {})
    else:
        return redirect('post_list')
    
def logout_view(request):
    logout(request)
    return redirect('post_list')

def register_view(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f"Account Successfully created for {username} ! Login In Now")
            return redirect('login_view')
        else:
            return render(request, 'registration/register.html', {'user_form': user_form})
    else:
        user_form = RegistrationForm()
        return render(request, 'registration/register.html', {'user_form': user_form})
        

@login_required 
def profile_view(request):
    return render(request, 'registration/profile.html')


@login_required 
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Account Updated Successfully !")
            return redirect('profile_view')  
    else:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'registration/profile_update.html', context)