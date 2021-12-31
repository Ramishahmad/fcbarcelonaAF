from django.contrib import admin

from message.models import Conversation, Messages

# Register your models here.

admin.site.register(Conversation)
admin.site.register(Messages)