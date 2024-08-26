"""
ASGI config for impulse_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from . import routing
from channels.routing import URLRouter, ProtocolTypeRouter
from channels.sessions import CookieMiddleware, SessionMiddleware
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'impulse_chat.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': CookieMiddleware(SessionMiddleware(URLRouter(routing.websocket_urlpatterns))),
})


