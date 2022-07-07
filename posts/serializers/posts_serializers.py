from rest_framework import serializers
from posts.entities.posts_entites import VotePostInputEntity

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "header", "text", "image", "creator"]


class VotePostInputSerializer(serializers.HyperlinkedModelSerializer):
    post_id = serializers.IntegerField()

    def save(self, **kwargs):
        return VotePostInputEntity(**kwargs)
