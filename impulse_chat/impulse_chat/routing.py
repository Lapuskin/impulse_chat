from django.urls import path

from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/<uuid:uuid>', ChatConsumer.as_asgi())
]