from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from wpp_messages.models import (
    WhatsappMessage
)

from wpp_messages.api.serializers import (
    WhatsappMessageSerializer
)

class WhatsappMessageViewset(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["consumer_system"]
    pagination_class = None
    queryset = WhatsappMessage.objects.all().order_by("-created_at")
    serializer_class = WhatsappMessageSerializer