from typing import Any, Dict
from django.views.generic import FormView

from django import forms

#For searching and sending data to URLs
from django.urls import reverse_lazy

#**from django.contrib import messages

#crispy form: help with setting up quicker layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#main: For custom user creation models
from main.models.main.access_forms_models.signup_page_model import CreateSignupForm

#*from django.template.context_processors import csrf
#*from crispy_forms.utils import render_crispy_form

# Create your views here.
class SignupView(FormView):
    template_name = 'forms_html/signup_page.html'
    form_class = CreateSignupForm
    success_url = 'login/'
    #! This fields should be fixed, for some reason
    #! It makes the website run though, 
    #! Make sure to ad the fields when testing
    fields = {'date_of_birth': 'love',}#CreateSignupForm.date_of_birth

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.helper = FormHelper(self)
        
        self.helper.form_id = 'signup-form'

        #Instead of specifying the method (i.e. 'POST' and 'GET')
        #uses htmx to specify post -> target
        #hx-swap: replaces outer html with inner, doesnt reload
        self.helper.form_action = reverse_lazy('signup')
        self.helper.form_method = 'post'
        #self.helper.attrs = {
        #    'hx-post': reverse_lazy('signup-form'),
        #    'hx-target': 'signup-form',
        #    'hx-swap': 'outerHTML'
        #}
        #todo: Helper button not displaying on the front end fix
        print("Adding Submit")
        self.helper.add_input(Submit('submit', 'Submit'))
        
        print("Submit has been added")

    #fyi: To Hide password fields(crispy forms does it)
    #//password = forms.CharField(widget=forms.PasswordInput())
    #//password2 = forms.CharField(widget=forms.PasswordInput())

    #fyi: If you want to add extra key-value pairs 
    #fyi: By default form view already has a key value pair for accessing
    #fyi: data from the database. 
    #def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #Adding aditional key-value pairs to add to the context dictionary then 
    # / Example: context['extra_data'] = 'Additional data for the template'

    # Then returning the dictionary
    #    return super().get_context_data(**kwargs)

    def formValid(self, form):
        if form.is_valid():
            form.save()
            #new_user = form.cleaned_data['username']
            #messages.success(self.request, 'Your account has been created, Lets login ' + new_user)
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 5:
            raise forms.ValidationError("Username is too Short")
        return username
 

   
    