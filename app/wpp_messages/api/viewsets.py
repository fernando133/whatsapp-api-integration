from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from wpp_messages.models import (
    WhatsappMessage
)

from wpp_messages.api.serializers import (
    WhatsappMessageSerializer,
    WhatsappMessageListSerializer
)

class WhatsappMessageViewset(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["consumer_system", "is_canceled", "was_sent"]
    pagination_class = None
    queryset = WhatsappMessage.objects.all().order_by("-created_at")
    serializer_class = WhatsappMessageSerializer
    
    def get_serializer_class(self):
        actions = ["list", "retrieve", "cancel"]
        if self.action in actions:
            return WhatsappMessageListSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=["put", "get"])
    def cancel(self, request, pk=None):
        message_obj = self.get_object()
        if message_obj.is_canceled:
            return Response({"Detail":"Message already canceled."}, status=400)
        
        if not message_obj.was_sent:
            message_obj.is_canceled = True
            message_obj.save()
            serializer = self.get_serializer(message_obj)
            return Response(serializer.data)

        return Response({"Detail":"Can't cancel, this message already sent."}, status=400)
