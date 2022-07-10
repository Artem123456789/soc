from rest_framework import serializers
from soc_media.serializers import BaseSerializer
from registration.entities.registration_entities import RegisterInputEntity


class RegisterInputSerializer(BaseSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    password_repeat = serializers.CharField()

    def create(self, validated_data) -> RegisterInputEntity:
        return RegisterInputEntity(**validated_data)


class RegisterResponseSerializer(BaseSerializer):
    user_id = serializers.IntegerField(source="id")
