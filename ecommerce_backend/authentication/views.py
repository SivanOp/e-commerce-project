from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
from .forms import CustomUserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def home_view(request):
    # Add any additional logic you need for the home page view
    return render(request, 'authentication/home.html')

def success_signup_view(request):
    return render(request, 'authentication/success_signup.html')

class SignUpView(View):
    template_name = 'authentication/signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)        
        if request.method == "POST":
            if form.is_valid():
                user = form.save(commit=False) 
                user.is_active = True
                form.save()
                # Redirect the user to a success page
                success_url = reverse_lazy('success_signup')
                return redirect(success_url)
            else:
                print(form.errors)
        return render(request, self.template_name, {'form': form})


class LoginView(View):
    template_name = 'authentication/login.html'

    def post(self, request, *args, **kwargs):
        print(request)
        if request.method == "POST":
            custom_username = request.POST.get('custom_username')
            custom_password = request.POST.get('custom_password')
            print(custom_username)
            print(custom_password)
            if custom_username is not None and custom_password is not None:
                user = authenticate(request, custom_username=custom_username, custom_password=custom_password) 
                print(user)
                if user is not None:
                    # User credentials are valid, log in the user
                    login(request, user)
                    return redirect('home')  # Replace 'home' with the name of your home page URL
                
        # If authentication fails or required data is missing, display an error message
        return render(request, self.template_name, {'error_message': 'Invalid login credentials'})
