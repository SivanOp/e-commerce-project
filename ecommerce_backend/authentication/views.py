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
        form = CustomUserCreationForm(request.POST)
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                #return redirect('home')  # Replace 'home' with the name of your home page URL
            return render(request, self.template_name, {'error_message': 'Invalid login credentials'})
        return render(request, self.template_name, {'form': form})
