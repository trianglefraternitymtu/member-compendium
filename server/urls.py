from django.urls import include, path

from slack import entrypoints
import website

urlpatterns = [
    path('slack/', include(entrypoints))
]
