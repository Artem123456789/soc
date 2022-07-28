from django.contrib import admin

from chating.models import SentMessage, ReceivedMessage


@admin.register(SentMessage)
class SentMessageAdmin(admin.ModelAdmin):
    pass


@admin.register(ReceivedMessage)
class ReceivedMessageAdmin(admin.ModelAdmin):
    pass
