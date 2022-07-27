from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model


User = get_user_model()


class Message(TimeStampedModel):
    def __str__(self):
        return self.text

    text = models.TextField(null=True, blank=True)


class SentMessage(TimeStampedModel):
    def __str__(self):
        return self.message.text + " from " + self.user.username

    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class ReceivedMessage(TimeStampedModel):
    def __str__(self):
        return self.message.text + " to " + self.user.username

    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
