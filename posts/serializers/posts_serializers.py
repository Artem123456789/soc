from rest_framework import serializers
from soc_media.serializers import BaseSerializer

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "header", "text", "image", "user", "upvotes", "downvotes"]

