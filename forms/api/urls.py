from django import views
from .views import *
from api import views
from django.urls import path

urlpatterns = [
    
    path('form/', views.InformationList.as_view()),
]