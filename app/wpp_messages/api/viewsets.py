from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from wpp_messages.models import (
    WhatsappMessage
)

from wpp_messages.api.serializers import (
    WhatsappMessageSerializer
)

class WhatsappMessageViewset(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["consumer_system", "is_canceled", "was_sent"]
    pagination_class = None
    queryset = WhatsappMessage.objects.all().order_by("-created_at")
    serializer_class = WhatsappMessageSerializer

    @action(detail=True, methods=["put", "get"])
    def cancel(self, request, pk=None):
        message_obj = self.get_object()
        if not message_obj.was_sent:
            message_obj.is_canceled = True
            message_obj.save()
        serializer = self.get_serializer(message_obj)
        return Response(serializer.data)
