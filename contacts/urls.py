import imp
from django.urls import path
from .views import (
        IndexView,
        ContactDetailView, 
        ContactCreateView, 
        ManageContactList,
        ContactUpdateView,
        ContactDeleteView
        )    


app_name = 'contacts'

urlpatterns = [
    path('',IndexView.as_view(), name="home"),
    path('contact/<int:pk>/',ContactDetailView.as_view(), name="detail"),
    path('contact/create/',ContactCreateView.as_view(), name="create"),
    path('contact/manage/',ManageContactList.as_view(), name="manage"),
    path('contact/update/<int:pk>/',ContactUpdateView.as_view(), name="update"),
    path('contact/delete/<int:pk>/',ContactDeleteView.as_view(), name="delete"),

]