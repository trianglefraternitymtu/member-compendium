from django.urls import include, path

from . import auth
from . import actions
from . import events
from . import coe
from . import onboarding
# from . import dinner
# from . import soberdrive

commands = [
    path('coe', coe.command),
    # path('onboarding', onboarding.process, name="slack-onboarding")
]

entrypoints = [
    path('auth', auth.entry, name='slack-auth'),
    # path('actions', actions.entry, name='slack-action'),
    # path('actions/external', actions.external_entry, name='slack-external-action'),
    path('events', events.entry, name='slack-events'),
    # path('webhook/<nonce>', webhooks.entry, name='slack-webhook'),

    path('commands/', include(commands))
]
