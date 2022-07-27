from django.contrib import admin

from chating.models import Message, SentMessage, ReceivedMessage


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["text"]


@admin.register(SentMessage)
class SentMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(ReceivedMessage)
class ReceivedMessageAdmin(admin.ModelAdmin):
    pass
