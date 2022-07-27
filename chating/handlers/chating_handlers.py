from chating.entities.chating_entities import SendMessageInputEntity
from django.contrib.auth import get_user_model

from chating.models import Message, SentMessage, ReceivedMessage

User = get_user_model()


class ChatingHandler:

    def send_message(self, input_entity: SendMessageInputEntity, from_user: User):
        message = Message(text=input_entity.text)
        message.save()

        sent_message = SentMessage(message=message, user=from_user)
        sent_message.save()

        received_message = ReceivedMessage(message=message, user=User.objects.get(username=input_entity.to_username))
        received_message.save()
