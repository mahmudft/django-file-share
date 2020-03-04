from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('drive/<uuid:uuid>', consumers.Comments),
]
