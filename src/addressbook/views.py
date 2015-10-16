from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import get_template #finds where templates are present using settings.py
from django.shortcuts import render_to_response
from django.template import Context
from addressbook.models import createNewContactForm
from django.views.generic.edit import FormView
# Create your views here.


def home (request):
	return render(request, "home.html")

#display template with the form
class newContactView (FormView):
	template_name = "newcontact.html"
	form_class = createNewContactForm
	success_url = '/newcontact/'

