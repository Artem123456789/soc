from chating.constants import MAX_MESSAGE_TEXT_LEN, MAX_USERNAME_LEN
from chating.entities.chating_entities import SendMessageInputEntity, GetChatInputEntity, SentMessageEntity
from chating.models import SentMessage
from soc_media.serializers import BaseSerializer
from rest_framework import serializers


class SendMessageInputSerializer(BaseSerializer):
    text = serializers.CharField(max_length=MAX_MESSAGE_TEXT_LEN)
    to_username = serializers.CharField(max_length=MAX_USERNAME_LEN)

    def create(self, validated_data) -> SendMessageInputEntity:
        return SendMessageInputEntity(**validated_data)


class GetChatInputSerializer(BaseSerializer):
    chat_user_username = serializers.CharField(max_length=MAX_USERNAME_LEN)

    def create(self, validated_data) -> GetChatInputEntity:
        return GetChatInputEntity(**validated_data)


class SentMessageSerializer(BaseSerializer):
    text = serializers.CharField(max_length=MAX_MESSAGE_TEXT_LEN)
    sender_username = serializers.SerializerMethodField()
    receiver_username = serializers.SerializerMethodField()

    def get_sender_username(self, obj: SentMessage):
        return obj.from_user.username

    def get_receiver_username(self, obj: SentMessage):
        return obj.received_message.to_user.username

    def create(self, validated_data) -> SentMessageEntity:
        return SentMessageEntity(**validated_data)

