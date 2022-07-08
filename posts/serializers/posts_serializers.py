from rest_framework import serializers
from posts.entities.posts_entites import VotePostInputEntity
from soc_media.serializers import BaseSerializer

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "header", "text", "image", "creator", "upvotes", "downvotes"]


class VotePostInputSerializer(BaseSerializer):
    post_id = serializers.IntegerField()

    def create(self, validated_data: dict) -> VotePostInputEntity:
        return VotePostInputEntity(**validated_data)
