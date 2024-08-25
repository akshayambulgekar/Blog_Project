# blog_project/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from blog.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



    
@login_required
def blog_list_view(request):
    # Your logic for listing blogs
    return render(request, 'post_list.html') 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('post_list')  # Redirect to the home page or any other page
        else:
            # Optionally, you can use Django's messages framework to provide feedback
            messages.error(request, "Invalid login credentials")
            return render(request, 'login.html')  # Render the login page again with an error
    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})