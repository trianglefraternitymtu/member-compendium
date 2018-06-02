from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from slackclient import SlackClient

import logging
import uuid
import os

from website.models import Webhook

logger = logging.getLogger('basicLogger')

hook_url = "/slack/webhook/{nonce}".format

@require_POST
def entry(request, nonce=None):
    if not nonce:
        return HttpResponse(status=404)

    hook = get_object_or_404(Webhook, nonce=nonce)

    payload = json.loads(request.body.decode())
    logger.debug(payload)

    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    sc.api_call(
      "chat.postMessage",
      **payload
    )

    return HttpResponse(status=200)

def make_webhook(channel):
    new_nonce = str(uuid.uuid4())

    hook, created = Webhook.objects.get_or_create(channel=channel,
                                                  defaults={'nonce':new_nonce})

    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    sc.api_call(
      "chat.postMessage",
      channel=hook.channel,
      text="A webhook URL has been configured for this channel.\n" + hook_url(nonce=hook.nonce)
    )

def remove_webhook(channel):
    try:
        hook = Webhook.objects.get(channel=channel)
        hook.delete()
    except ObjectDoesNotExist:
        pass

    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    sc.api_call(
      "chat.postMessage",
      channel=channel,
      text="The webhook for this channel has been removed."
    )

@require_POST
def list(request):
    hooks = Webhook.objects.filter(channel__istartswith="C")
    attachments = [{ "title":"<#{}>".format(h.channel), "text":hook_url(nonce=h.nonce) } for h in hooks]
    logger.debug(attachments)

    if hooks:
        return JsonResponse({
            "text":"These are all of the webhooks that are managed by this application.",
            "attachments": attachments
        })
    else:
        return JsonResponse({"text":"There doesn't seem to be any webhooks managed by this app. Try inviting <@{}> to a channel?".format(os.environ.get('BOT_USER_ID'))})
