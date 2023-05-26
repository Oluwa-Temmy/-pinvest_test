from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


#*For user signup
from .models.main.access_forms_models.signup_page_model import CreateSignupForm
#from django.contrib.auth.forms import UserCreationForm

#*Create user login
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(response):
    return render(response, "main/index.html", {})

#fyi: login page
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request,"Incorrect username or password")
    context = {}
    return render(request, "main/access_forms_html/LoginPage.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#fyi: signup page
def signup(request):
    if request.method == 'POST':
        form = CreateSignupForm(request.POST)
        if form.is_valid():
            form.save()
            new_user = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created, Lets login ' + new_user)
            return redirect('login')
    else:
        form = CreateSignupForm()
    context = {'form': form}
    return render(request, "main/access_forms_html/SignupPage.html", context)

#fyi: About us page
def about_us(response):
    return render(response, "main/supplements_html/general_html/AboutUs.html", {})

#fyi: Home page
def homepage(response):
    return render(response, "main/homepage_html/homepage.html", {})

#*Test view
def test_page(response):
    return render(response, "main/test.html", {})