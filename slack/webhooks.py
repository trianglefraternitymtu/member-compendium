from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist

import logging

from website.models import Webhook

logger = logging.getLogger('basicLogger')

@require_POST
def entry(request, nonce=None):
    if not nonce:
        return HttpResponse(status=404)

    try:
        webhook = Webhook.objects.get(nonce=nonce)
    except ObjectDoesNotExist as e:
        return HttpResponse(status=404)

    return HttpResponse(status=200)
