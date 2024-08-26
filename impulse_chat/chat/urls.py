from django.urls import path

from chat.views import LobbyView, ChatView

urlpatterns = [
    path('lobby/', LobbyView.as_view()),
    path('chat/<uuid:uuid>', ChatView.as_view(), name='chat' )
]