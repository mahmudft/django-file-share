from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf.urls import url
from django.urls import path
import fileshare
from fileshare import consumers

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
            URLRouter(
                [
                    url("drive/(?P<uuid>[^/]+)/$", consumers.CommentsConsumer),
                ]
            )
        )
})