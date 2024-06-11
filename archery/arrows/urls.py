'''
    URL definitions for the basic homepage app
    including URLs for the user managemenet
'''
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
