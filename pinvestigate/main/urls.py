from django.urls import path
from . import views

urlpatterns = [
    #*General Non Access
    path("", views.index, name="index"),
    path("login", views.loginPage, name="login"),
    path("signup", views.signup, name="signup"),
    path("about", views.about_us, name="about_us"),

    #*Access Pages
    path("homepage", views.homepage, name="homepage"),

    #*Test urls
    path("test",views.test_page,name="tests")
]