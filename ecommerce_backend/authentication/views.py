from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponseNotAllowed
from .forms import CustomUserCreationForm

def success_signup_view(request):
        return render(request, 'success_signup.html')

class SignUpView(View):
    template_name = 'authentication/signup.html'

    def get(self, request, *args, **kwargs):
        # Respond with a method not allowed for GET requests
        return HttpResponseNotAllowed(['POST'])

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                # Redirect the user to a success page
                return redirect('success_signup')
            else:
                # Form is not valid, render the form with errors
                return render(request, self.template_name, {'form': form})

        # If the request method is not POST, render the form with an empty form
        return render(request, self.template_name, {'form': form})



class LoginView(View):
    template_name = 'authentication/login.html'

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #return redirect('home')  # Replace 'home' with the name of your home page URL
        return render(request, self.template_name, {'error_message': 'Invalid login credentials'})
