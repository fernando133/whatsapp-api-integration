from rest_framework import serializers

from wpp_messages.models import (
    WhatsappMessage
)

class WhatsappMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsappMessage
        exclude = ["was_sent", "type", "is_canceled", "api_return"]

class WhatsappMessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhatsappMessage
        exclude = ["type"]
