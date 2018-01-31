from django.shortcuts import redirect, render

import os, logging

logger = logging.getLogger('basicLogger')

def signin(request):
    url = "https://slack.com/oauth/authorize?scope=identity.basic,identity.email,identity.team&client_id={}".format(os.environ["SLACK_CLIENT_ID"])
    return redirect(url, permanent=True)

def dashboard(request):
    logger.info("Rendering Dashboard")
    return render(request, 'base.html')
