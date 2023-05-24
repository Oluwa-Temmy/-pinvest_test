from django.urls import path
from access_pages.views import IndexView
from access_pages.views_f.access_pages.loginpage_view import LoginView
from access_pages.views_f.access_pages.signuppage_view import SignupView

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
    path('login/', LoginView.as_view(), name= 'login_page'),
    path('signup/', SignupView.as_view(), name= 'signup_page'),
    #path('', AboutView.as_view(), name= 'index'),
    #path('', ForgotView.as_view(), name= 'index'),
    #path('', DonateView.as_view(), name= 'index'),
]
