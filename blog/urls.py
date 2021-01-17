from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name = 'blog-home'),
    path ('<str:kk>', views.greet, name = 'greet'), 
]