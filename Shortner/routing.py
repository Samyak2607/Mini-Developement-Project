from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import shortnerModule.routing

application = ProtocolTypeRouter({
	'websocket': AuthMiddlewareStack(
        URLRouter(
            shortnerModule.routing.websocket_urlpatterns
        )
    ),
})