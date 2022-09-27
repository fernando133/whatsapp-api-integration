from django.contrib import admin
from wpp_messages.models import (
    ConsumerSystem, 
    WhatsappMessage
)

@admin.register(ConsumerSystem)
class ConsumerSystemAdmin(admin.ModelAdmin):
    list_display = ["id", "reference"]

@admin.register(WhatsappMessage)    
class WhatsappMessage(admin.ModelAdmin):
    list_display = ["id", "system", "date_to_send", "was_sent"]
    

