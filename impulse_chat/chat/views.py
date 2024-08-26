from django.contrib.sessions.backends.db import SessionStore
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Create your views here.
class LobbyView(TemplateView):
    template_name = 'lobby.html'

    def post(self, request):
        if request.session.get('username', None):
            username = request.POST['username']
            session = SessionStore()
            session.create()
            session_id = session.session_key
            session['username'] = username
            session.save()
        else:
            session_id = request.COOKIES.get('session_id', None)
        return redirect('chat', session_id=session_id)


class ChatView(TemplateView):
    template_name = 'chat.html'
