from celery import shared_task
from .models import WhatsappMessage
from datetime import date

@shared_task(name = "send_scheduled_messages")
def send_scheduled_messages():
    day_messages = WhatsappMessage.objects.filter(date_to_send=date.today())
    for message in day_messages:
        if message.able_to_send():
            response = message.send_message()
            if response.status_code == 200:
                message.set_sent()
            message.set_return(response.text)
