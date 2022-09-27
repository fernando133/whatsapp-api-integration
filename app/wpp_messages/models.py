from django.db import models
import uuid

class ConsumerSystem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reference = models.CharField("Consumer Reference", max_length=50)
    
    def __str__(self):
            return self.reference

    class Meta:
        verbose_name = "Consumer System"
        verbose_name_plural = "Consumer Systems"

class WhatsappMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    system = models.ForeignKey(ConsumerSystem, on_delete=models.CASCADE)
    to = models.CharField("Recipient(s) Number", max_length=1500)
    type = models.CharField("Message Type", max_length=5, default="text")
    message_body = models.CharField("Message Body", max_length=1000)
    date_to_send = models.DateTimeField("Date to Send", auto_now_add=True)
    was_sent = models.BooleanField("Was Sent?", default=False)
    
    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Consumer System"
        verbose_name_plural = "Consumer Systems"