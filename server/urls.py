from django.urls import include, path

from slack import entrypoints
from website import pages
import website

urlpatterns = [
    path('slack/', include(entrypoints)),
    path('', include(pages))
]
