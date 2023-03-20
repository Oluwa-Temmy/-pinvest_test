from django.shortcuts import render
from django.http import HttpResponse

#*For user signup
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(response):
    return render(response, "main/index.html", {})

def login(response):
    return render(response, "main/access_forms_html/LoginPage.html", {})

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, "main/access_forms_html/SignupPage.html", context)

