import os

import django
from channels.http import AsgiHandler  # type: ignore
from channels.routing import ProtocolTypeRouter  # type: ignore


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jobhuntr.settings")
django.setup()

application = ProtocolTypeRouter({"http": AsgiHandler()})
