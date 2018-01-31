from django.urls import include, path

from . import views

pages = [
    path('', views.signin, name='sign-in'),
    path('dashboard', views.dashboard, name='dashboard')
]
