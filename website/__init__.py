from django.urls import include, path

from . import views

pages = [
    path('', views.signin, name='sign-in'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('soberdrive', views.soberdrive, name='soberdrive'),
    path('dinner', views.dinner, name='chapter dinner'),
]
