from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model


User = get_user_model()


class ReceivedMessage(TimeStampedModel):

    to_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class SentMessage(TimeStampedModel):

    text = models.TextField(null=True, blank=True)
    from_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    received_message = models.ForeignKey(ReceivedMessage, on_delete=models.CASCADE, null=True)
