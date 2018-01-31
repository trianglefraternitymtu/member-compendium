import logging, json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from .utils import verified_token, filter_header

logger = logging.getLogger('basicLogger')

@require_POST
def entry(request):
    logger.info('Received an event')

    payload = json.loads(request.body.decode())
    logger.debug(payload)

    if not verified_token(payload['token']):
        return HttpResponse(status=401)

    if filter_header(request.META):
        return HttpResponse(status=200)

    if payload['type'] == "url_verification":
        logger.debug("URL Verification")
        return JsonResponse({'challenge':payload['challenge']})

    return HttpResponse(status=200)
