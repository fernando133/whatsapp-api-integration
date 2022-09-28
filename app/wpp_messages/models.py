from django.db import models
import uuid
import requests
import json
import os

class ConsumerSystem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference = models.CharField("Consumer Reference", max_length=50)
    
    def __str__(self):
            return str(self.id)

    class Meta:
        verbose_name = "Consumer System"
        verbose_name_plural = "Consumer Systems"

class WhatsappMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    consumer_system = models.ForeignKey(ConsumerSystem, on_delete=models.CASCADE)
    to = models.CharField("Recipient(s) Number", max_length=1500)
    type = models.CharField("Message Type", max_length=5, default="text")
    message_body = models.TextField("Message Body", max_length=1000)
    send_now = models.BooleanField("Send Now?", default=True)
    date_to_send = models.DateTimeField("Date to Send", null=True)
    was_sent = models.BooleanField("Was Sent?", default=False)
    is_canceled = models.BooleanField("Is Canceled?", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        
    def set_sent(self):
        self.was_sent = True
        self.save()
    
    def send_message(self):
        url = "https://graph.facebook.com/v14.0/"+os.environ['NUMBER_ID']+"/messages"

        payload = json.dumps({
            "messaging_product": "whatsapp",
            "to": self.to,
            "type": self.type,
            "text": {
                "preview_url": False,
                "body": self.message_body
            }
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + os.environ['BEARER_TOKEN']
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response

