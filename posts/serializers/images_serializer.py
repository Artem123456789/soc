from rest_framework import serializers

from posts.models import PostImage
from soc_media.serializers import BaseSerializer


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ["id", "image"]
