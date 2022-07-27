from chating.entities.chating_entities import SendMessageInputEntity, GetChatInputEntity
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

    def get_chat(self, input_entity: GetChatInputEntity):
        user_sender = User.objects.get(username=input_entity.sender_username)
        user_receiver = User.objects.get(username=input_entity.receiver_username)

        messages_by_sender = SentMessage.objects.filter(user=user_sender)
        messages_by_receiver = ReceivedMessage.objects.filter(user=user_receiver)
        pass
