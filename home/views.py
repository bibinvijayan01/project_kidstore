from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile

def index(request):
    return render(request, 'homepage/index.html')

def login_register_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password1')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('login_register')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('login_register')

            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                Profile.objects.create(user=user, phone_number=phone_number)
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('index')
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
                return redirect('login_register')

        elif form_type == 'login':
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.username, password=password)
                if user:
                    login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect('index')
                else:
                    messages.error(request, 'Password incorrect!')
                    return redirect('login_register')
            except User.DoesNotExist:
                messages.error(request, 'No account found with that email address.')
                return redirect('login_register')

    return render(request, 'login/login.html')


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login_register')

@login_required
def profile_view(request):
    return render(request, 'account/profile.html', {
        'user': request.user
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)

        # Update user fields
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)

        # Update profile fields
        profile.phone_number = request.POST.get('phone_number', profile.phone_number)

        try:
            user.save()
            profile.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile_view')
        except Exception as e:
            messages.error(request, f'Error updating profile: {str(e)}')
            return redirect('edit_profile')

    return render(request, 'account/edit_profile.html', {
        'user': request.user,
        'profile': Profile.objects.get(user=request.user)
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        if not user.check_password(current_password):
            messages.error(request, 'Current password is incorrect.')
            return redirect('change_password')

        if new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
            return redirect('change_password')

        try:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Your password has been changed successfully. Please log in again.')
            return redirect('login_register')
        except Exception as e:
            messages.error(request, f'Error changing password: {str(e)}')
            return redirect('change_password')

    return render(request, 'account/change_password.html')