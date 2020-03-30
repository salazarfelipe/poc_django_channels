from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import django_channels_demo.domain.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            django_channels_demo.domain.routing.websocket_urlpatterns
        )
    ),
})
