import logging, json, os
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST

from .utils import verified_token, filter_header
from .webhooks import make_webhook, remove_webhook

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

    if payload['event']['type'] == 'member_joined_channel':
        if payload['event']['user'] == os.environ.get('BOT_USER_ID'):
            make_webhook(payload['event']['channel'])

    if payload['event']['type'] == 'member_left_channel':
        if payload['event']['user'] == os.environ.get('BOT_USER_ID'):
            remove_webhook(payload['event']['channel'])

    return HttpResponse(status=200)
