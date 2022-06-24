import imp
from django.urls import path
from .views import IndexView


app_name = 'contacts'

urlpatterns = [
    path('',IndexView.as_view(), name="home"),
]