from celery import shared_task
from .models import WhatsappMessage
from datetime import date

@shared_task(name = "send_scheduled_messages")
def send_scheduled_messages():
    print("run")
    day_messages = WhatsappMessage.objects.filter(date_to_send=date.today())
    for message in day_messages:
        if not message.was_sent:
            response = message.send_message()
            if response.status_code == 200:
                message.set_sent()
            print(response.text, message)
