from .models import Contacts
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from .forms import ContactForm

class IndexView(ListView):
    model = Contacts
    template_name = 'contacts/index.html'
    context_object_name = 'index'

# class ContactDetailView(DetailView):
#     model = Contacts
#     template_name = 'contacts/detail.html'
#     context_object_name = 'contact'

class ContactCreateView(CreateView):
    model = Contacts
    form_class = ContactForm
    template_name = 'contacts/create.html'
    success_url = '/'

class ManageContactList(ListView):
    model = Contacts
    template_name = 'contacts/manage.html'
    context_object_name = 'manage_list'

class ContactUpdateView(UpdateView):
    model = Contacts
    form_class = ContactForm
    pk_url_kwarg = 'pk'
    template_name = 'contacts/update.html'
    success_url = '/contact/manage/'

class ContactDeleteView(DeleteView):
    model = Contacts
    pk_url_kwarg = 'pk'
    template_name = 'contacts/delete.html'
    success_url = '/contact/manage/'