from chating.constants import MAX_MESSAGE_TEXT_LEN, MAX_USERNAME_LEN
from chating.entities.chating_entities import SendMessageInputEntity
from soc_media.serializers import BaseSerializer
from rest_framework import serializers


class SendMessageInputSerializer(BaseSerializer):
    text = serializers.CharField(max_length=MAX_MESSAGE_TEXT_LEN)
    to_username = serializers.CharField(max_length=MAX_USERNAME_LEN)

    def create(self, validated_data) -> SendMessageInputEntity:
        return SendMessageInputEntity(**validated_data)
