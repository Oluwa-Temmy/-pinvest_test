from django.urls import path
from access_pages.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name= 'index'),
]
