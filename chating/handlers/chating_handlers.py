from chating.entities.chating_entities import SendMessageInputEntity, GetChatInputEntity
from django.contrib.auth import get_user_model

from chating.models import SentMessage, ReceivedMessage

User = get_user_model()


class ChatingHandler:

    def send_message(self, input_entity: SendMessageInputEntity, from_user: User):
        received_message = ReceivedMessage(to_user=User.objects.get(username=input_entity.to_username))
        received_message.save()

        sent_message = SentMessage(text=input_entity.text, from_user=from_user, received_message=received_message)
        sent_message.save()

    def get_chat(self, input_entity: GetChatInputEntity, user_sender: User):
        user_receiver = User.objects.get(username=input_entity.chat_user_username)

        messages = SentMessage.objects.filter(from_user=user_sender,
                                              received_message__to_user=user_receiver).union(
            SentMessage.objects.filter(from_user=user_receiver,
                                       received_message__to_user=user_sender)
        ).order_by("created")
        return messages
