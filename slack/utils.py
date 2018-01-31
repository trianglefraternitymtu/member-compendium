from django.http import HttpResponse
import os, logging

def verified_token(token):
    app_verification_token = os.environ.get('SLACK_VERIFICATION_TOKEN')
    return app_verification_token == token

def error_msg(msg):
    return {
        'icon_emoji' : ':warning:',
        'response_type' : 'ephemeral',
        'text' : msg
    }

def filter_command(request):
    """
    Processes commands from a slash command.
    https://api.slack.com/slash-commands
    """
    logger = logging.getLogger('basicLogger')
    logger.debug(request.POST)

    if request.POST.get('ssl_check') == '1':
        logger.info("SSL check.")
        return HttpResponse(status=200)

    token = request.POST.get('token')

    if not verified_token(token):
        logger.warning("Token verification failed. ({})".format(token))
        return HttpResponse(status=401)

    if "HTTP_X_SLACK_RETRY_NUM" in request.META:
        logger.info("Received a retry request.")
        if request.META["HTTP_X_SLACK_RETRY_REASON"] != "http_timeout":
            logger.warning('Reason for retry was "{}"'.format(request.META["HTTP_X_SLACK_RETRY_REASON"]))
        return HttpResponse(status=200)

    return None
