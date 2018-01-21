from django.http import HttpResponse
import os, logging

def verified_token(token):
    app_verification_token = os.environ.get('SLACK_VERIFICATION_TOKEN')
    return app_verification_token == token

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

    return None
