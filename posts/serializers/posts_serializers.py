from rest_framework import serializers

from comments.models import Comment
from comments.serializers.comments_serializers import CommentSerializer

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj: Post):
        return CommentSerializer(Comment.objects.filter(post=obj), many=True).data

    class Meta:
        model = Post
        fields = ["id", "header", "text", "image", "user", "upvotes", "downvotes", "comments"]
