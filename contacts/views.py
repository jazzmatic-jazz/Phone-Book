import imp
from .models import Contacts
from django.views.generic import ListView

class IndexView(ListView):
    model = Contacts
    template_name = 'contacts/index.html'
