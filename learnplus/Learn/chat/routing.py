from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    # WebSocket pour les messages de groupe des instructeurs
    re_path(r'^ws/instructor/messages/(?P<classe>\w+)/$', consumers.ChatConsumer.as_asgi()),

    # WebSocket pour les messages de groupe des étudiants
    re_path(r'^ws/student/messages/(?P<classe>\w+)/$', consumers.ChatConsumer.as_asgi()),

    # WebSocket pour les messages privés
    re_path(r'^ws/private-chat/(?P<receiver>\d+)/$', consumers.PrivateChatConsumer.as_asgi()),
]
