from rest_framework import serializers

from comments.models import Comment
from comments.serializers.comments_serializers import CommentSerializer

from posts.models import Post, PostImage
from posts.serializers.images_serializer import ImagesSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    def get_comments(self, obj: Post):
        return CommentSerializer(Comment.objects.filter(post=obj), many=True).data

    def get_images(self, obj: Post):
        return ImagesSerializer(PostImage.objects.filter(post=obj), many=True).data

    class Meta:
        model = Post
        fields = ["id", "header", "text", "images", "user", "upvotes", "downvotes", "comments"]
