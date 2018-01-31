from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from slackclient import SlackClient

import logging, os

from website.models import Member

logger = logging.getLogger('basicLogger')

@require_GET
def entry(request):
    logger.debug(request.GET)

    auth_code = request.GET.get('code')
    auth_state = request.GET.get('state')

    sc = SlackClient("")

    client_id = os.environ["SLACK_CLIENT_ID"]
    client_secret = os.environ["SLACK_CLIENT_SECRET"]

    # Request the auth tokens from Slack
    auth_response = sc.api_call(
        "oauth.access",
        client_id=client_id,
        client_secret=client_secret,
        code=auth_code
    )

    logger.debug(auth_response)

    if auth_response.get('ok'):
        return redirect('dashboard')
    else:
        logger.warning("Unauthorized")
        return HttpResponse(status=401)
