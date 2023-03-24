from django.shortcuts import render
from django.http import HttpResponse

#*For user signup
from .static.main.models.main.access_forms_models.signup_page_model import CreateSignupForm

# Create your views here.
def index(response):
    return render(response, "main/index.html", {})

def login(response):
    return render(response, "main/access_forms_html/LoginPage.html", {})

def signup(request):
    form = CreateSignupForm()
    if request.method == 'POST':
        form = CreateSignupForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "main/access_forms_html/SignupPage.html", context)

