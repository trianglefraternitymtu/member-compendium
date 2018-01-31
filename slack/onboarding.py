import logging
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from .utils import filter_command

logger = logging.getLogger('basicLogger')

@require_POST
def process(request):
    pass
