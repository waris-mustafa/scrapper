import os

import apps.email_sender.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = ProtocolTypeRouter({'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(apps.email_sender.routing.websocket_urlpatterns)), })
