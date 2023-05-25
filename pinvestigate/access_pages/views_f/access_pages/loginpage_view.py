from typing import Any
from django.views.generic import FormView
from django.template import Context

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django import forms

#main: For custom user creation models
from access_pages.form_structure.access_pages.login_form import UserLoginForm

# Create your views here.
class UserLoginView(FormView):
    template_name = 'forms_html/login_page.html'
    form_class = UserLoginForm
    success_url = 'index/'
    #!This makes the web work
    fields = {'test':'filler'}
     
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'user-login-form'
        self.helper.form_method = 'post'
        #todo: fix submit button
        self.helper.add_input(Submit('submit','Submit'))
        
    
    def check_validation(self):
        #validate the user
        pass



    
