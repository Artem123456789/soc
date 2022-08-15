from rest_framework import serializers

from soc_media.serializers import BaseSerializer


class ImagesSerializer(BaseSerializer):
    images = serializers.FileField()
